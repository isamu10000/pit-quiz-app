"""
Political Institution Theory — AI-tutored weekly quiz (Streamlit).

クイズ内容は pit_quizzes.py で管理。このファイルは基本的に触らない。
"""

import datetime as dt
import json
import os
import re
from zoneinfo import ZoneInfo

import anthropic
import streamlit as st

from pit_quizzes import PIT_QUIZZES

# ---------------------------------------------------------------- settings
COURSE_NAME = "Political Institution Theory"
MODEL = "claude-opus-4-6"   # 例: "claude-sonnet-5-5" に変えるとコストを抑えられる
MAX_EXCHANGES = 7
MIN_EXCHANGES = 3
MAX_TOKENS = 700
TZ = ZoneInfo("Asia/Tokyo")  # Streamlit Cloud は UTC で動くため明示する
SHEET_HEADERS = [
    "Timestamp (JST)", "Student Name", "Quiz ID", "Quiz Title", "Final Answer",
    "Word Count", "Exchange Count", "Conversation Log",
]
CELL_LIMIT = 49000  # Google Sheets の1セル上限 (50,000字) 対策

st.set_page_config(page_title=f"{COURSE_NAME} Quiz", page_icon="🏛️", layout="centered")


# ---------------------------------------------------------------- helpers
def get_secret(key, default=None):
    try:
        if key in st.secrets:
            return st.secrets[key]
    except Exception:  # ローカルで secrets.toml が無い場合
        pass
    return os.environ.get(key, default)


def get_gsheet_creds():
    from google.oauth2.service_account import Credentials

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    secret = get_secret("GOOGLE_CREDENTIALS")
    if secret is not None:
        # Streamlit の Secrets オブジェクトは dict ではないので hasattr で判定
        if hasattr(secret, "items"):
            info = {k: v for k, v in secret.items()}
        else:
            info = json.loads(str(secret))
        if "private_key" in info:
            info["private_key"] = info["private_key"].replace("\\n", "\n")
        return Credentials.from_service_account_info(info, scopes=scopes)

    path = os.environ.get("GOOGLE_CREDENTIALS_FILE")
    if path:
        return Credentials.from_service_account_file(path, scopes=scopes)
    return None


def save_to_sheet(record):
    import gspread

    creds = get_gsheet_creds()
    sheet_id = get_secret("GOOGLE_SHEET_ID")
    if creds is None or not sheet_id:
        raise RuntimeError("GOOGLE_CREDENTIALS / GOOGLE_SHEET_ID が設定されていません。")

    sh = gspread.authorize(creds).open_by_key(sheet_id)
    try:
        ws = sh.worksheet(record["quiz_id"])
    except gspread.WorksheetNotFound:
        ws = sh.add_worksheet(title=record["quiz_id"], rows=1000, cols=len(SHEET_HEADERS))
        ws.append_row(SHEET_HEADERS)

    ws.append_row(
        [
            record["timestamp"],
            record["student_name"],
            record["quiz_id"],
            record["quiz_title"],
            record["final_answer"][:CELL_LIMIT],
            record["word_count"],
            record["exchange_count"],
            record["conversation_log"][:CELL_LIMIT],
        ],
        value_input_option="RAW",
    )


def parse_due(quiz):
    return dt.datetime.strptime(quiz["due_date"], "%Y-%m-%d %H:%M").replace(tzinfo=TZ)


def count_words(text):
    return len(text.split())


def conversation_log(messages):
    label = {"assistant": "[TUTOR]", "user": "[STUDENT]"}
    return "\n\n".join(f"{label[m['role']]} {m['content']}" for m in messages)


def build_system_prompt(quiz, exchange_no):
    concepts = "\n".join(f"- {name}: {desc}" for name, desc in quiz["concepts"])
    last_turn_note = (
        "This is the student's FINAL exchange. Briefly summarize what they have "
        "worked out and name the one thing they should strengthen in their written answer."
        if exchange_no >= MAX_EXCHANGES
        else ""
    )
    return f"""You are a Socratic AI tutor for the graduate course "{COURSE_NAME}" \
at the Graduate School of International Development (GSID), Nagoya University. \
Students are international graduate students writing short answers in English.

Your job is to help the student think, not to answer for them.
Rules:
- Never write the answer, a model answer, or sentences the student could paste into their submission.
- Each turn: respond to what the student said, then ask ONE (at most two) focused question(s).
- Keep each reply under about 150 words. Plain, friendly academic English.
- If the student writes in another language, you may reply briefly in that language but encourage them to formulate their ideas in English.
- Ground the discussion in the assigned reading. If the student misreads a concept, correct it clearly and briefly.
- If the student goes off topic or asks you to write the answer, politely redirect.
- The student has up to {MAX_EXCHANGES} exchanges with you and needs at least {MIN_EXCHANGES} before submitting. This is exchange {exchange_no} of {MAX_EXCHANGES}. {last_turn_note}

Assigned reading: {quiz.get("reading", "")}

Background given to the student:
{quiz["scenario"]}

Question the student must answer ({quiz["word_limit"][0]}-{quiz["word_limit"][1]} words):
{quiz["question"]}

Key concepts:
{concepts}

You opened the session with this message:
{quiz.get("opening_message", "")}

Additional instructions from the instructor:
{quiz.get("tutor_extra", "")}
"""


def ask_tutor(quiz, messages, exchange_no):
    client = anthropic.Anthropic(api_key=get_secret("ANTHROPIC_API_KEY"))
    # 先頭の挨拶 (assistant) は system に含めているので、API には user から始まる履歴を送る
    api_messages = [m for m in messages if not m.get("opening")]
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=build_system_prompt(quiz, exchange_no),
        messages=[{"role": m["role"], "content": m["content"]} for m in api_messages],
    )
    return "".join(b.text for b in resp.content if b.type == "text").strip()


def reset_session(quiz):
    st.session_state.quiz_id = quiz["id"]
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": quiz.get("opening_message", "Hello! Let's think through this question together."),
            "opening": True,
        }
    ]
    st.session_state.exchanges = 0
    st.session_state.submitted = None


# ---------------------------------------------------------------- UI
active = [q for q in PIT_QUIZZES if q.get("active")]

st.sidebar.title(f"🏛️ {COURSE_NAME}")
if not active:
    st.title(COURSE_NAME)
    st.info("There is no open quiz right now.")
    st.stop()

quiz = st.sidebar.selectbox(
    "Quiz",
    active,
    format_func=lambda q: q["title"],
    index=len(active) - 1,
)
student_name = st.sidebar.text_input("Your full name", placeholder="e.g., Yuki Tanaka").strip()

if st.session_state.get("quiz_id") != quiz["id"]:
    reset_session(quiz)

due = parse_due(quiz)
now = dt.datetime.now(TZ)
closed = now > due

st.sidebar.markdown(f"**Due:** {due:%a, %b %d, %Y %H:%M} (JST)")
if closed:
    st.sidebar.error("This quiz is closed.")
else:
    left = due - now
    st.sidebar.caption(f"Time left: {left.days} days {left.seconds // 3600} hours")
st.sidebar.markdown(
    f"**Tutor exchanges:** {st.session_state.exchanges} / {MAX_EXCHANGES}  \n"
    f"(at least {MIN_EXCHANGES} required to submit)"
)

st.caption(quiz["week_label"])
st.title(quiz["title"])
if quiz.get("reading"):
    st.markdown(f"📖 *{quiz['reading']}*")

with st.expander("Background", expanded=True):
    st.markdown(quiz["scenario"])

st.markdown("#### Question")
st.info(quiz["question"])
lo, hi = quiz["word_limit"]
st.caption(f"Answer length: {lo}–{hi} words")

with st.expander("Key concepts"):
    for name, desc in quiz["concepts"]:
        st.markdown(f"- **{name}**: {desc}")

# ---- tutor chat
st.markdown("### 💬 Discuss with the AI tutor")
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

chat_disabled = closed or st.session_state.submitted is not None \
    or st.session_state.exchanges >= MAX_EXCHANGES
if st.session_state.exchanges >= MAX_EXCHANGES and not st.session_state.submitted:
    st.caption("You have used all tutor exchanges. Please write and submit your answer below.")

prompt = st.chat_input("Type your thoughts here…", disabled=chat_disabled)
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    exchange_no = st.session_state.exchanges + 1
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            try:
                reply = ask_tutor(quiz, st.session_state.messages, exchange_no)
            except Exception as e:
                st.session_state.messages.pop()
                st.error(f"The tutor could not respond. Please try again. ({e})")
                st.stop()
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.exchanges = exchange_no
    st.rerun()

# ---- final answer
st.markdown("### ✍️ Your final answer")
answer = st.text_area(
    "Final answer",
    height=220,
    key=f"answer_{quiz['id']}",
    label_visibility="collapsed",
    disabled=closed or st.session_state.submitted is not None,
)
wc = count_words(answer)
st.caption(f"Word count: {wc} (required: {lo}–{hi})")

problems = []
if not student_name:
    problems.append("enter your full name in the sidebar")
if st.session_state.exchanges < MIN_EXCHANGES:
    problems.append(f"have at least {MIN_EXCHANGES} exchanges with the tutor "
                    f"(now {st.session_state.exchanges})")
if not (lo <= wc <= hi):
    problems.append(f"keep your answer within {lo}–{hi} words")

if st.session_state.submitted:
    rec = st.session_state.submitted
    st.success(f"Submitted at {rec['timestamp']} (JST). Thank you!")
    st.download_button(
        "Download a copy of your submission (JSON)",
        data=json.dumps(rec, ensure_ascii=False, indent=2),
        file_name=f"{rec['quiz_id']}_{re.sub(r'[^A-Za-z0-9]+', '_', rec['student_name'])}.json",
        mime="application/json",
    )
elif closed:
    st.warning("The deadline has passed. Submissions are closed.")
else:
    if problems:
        st.caption("To submit, please: " + "; ".join(problems) + ".")
    if st.button("Submit", type="primary", disabled=bool(problems)):
        record = {
            "timestamp": dt.datetime.now(TZ).strftime("%Y-%m-%d %H:%M:%S"),
            "student_name": student_name,
            "quiz_id": quiz["id"],
            "quiz_title": quiz["title"],
            "final_answer": answer.strip(),
            "word_count": wc,
            "exchange_count": st.session_state.exchanges,
            "conversation_log": conversation_log(st.session_state.messages),
        }
        with st.spinner("Saving your submission…"):
            try:
                save_to_sheet(record)
            except Exception as e:
                st.error(
                    "Your answer could not be saved. Please do not close this page; "
                    "copy your answer and contact the instructor. "
                    f"(Details: {e})"
                )
                st.stop()
        st.session_state.submitted = record
        st.rerun()
