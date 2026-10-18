# Political Institution Theory Quiz App — プロジェクト概要

## このプロジェクトについて
名古屋大学大学院（GSID）の授業「Political Institution Theory」向けのAI搭載クイズWebアプリ。
学生は指定文献を読んだ後、AIチューター（Claude）とソクラテス式対話をしてから短い回答を提出する。
回答（会話ログ＋最終回答）はGoogle Sheetsに自動保存される。
Comparative Methods Quiz App（`cm_quiz_app.py`）と同じ仕組みで、別リポジトリ・別アプリとして運用する。

## ファイル構成

| ファイル | 役割 |
|---|---|
| `pit_quiz_app.py` | Streamlitメインアプリ（画面構成を変えるとき以外は触らない） |
| `pit_quizzes.py` | クイズ定義ファイル（毎週ここだけ編集） |
| `requirements.txt` | Pythonパッケージ一覧 |
| `.gitignore` | 認証情報（secrets.toml, *.json）をコミットしないための設定 |

## アプリの仕様

- **フレームワーク**: Streamlit
- **AIモデル**: `MODEL` 定数（初期値 claude-opus-4-6）
- **最大会話往復数**: 7回（`MAX_EXCHANGES`）／ **提出に必要な最低往復数**: 3回（`MIN_EXCHANGES`）
- **時刻**: すべて日本時間（`Asia/Tokyo`）。Streamlit Cloud は UTC で動くためコード側で固定
- **締切**: `due_date`（JST）を過ぎるとチャットと提出が自動で閉じる
- **保存先**: Google Sheets（クイズIDごとに別タブを自動作成）
- **保存内容**: Timestamp (JST)、Student Name、Quiz ID、Quiz Title、Final Answer、Word Count、Exchange Count、Conversation Log
- 提出後、学生は自分の提出内容をJSONでダウンロードできる

## 画面構成（上から順）

1. **サイドバー**: クイズ選択、氏名入力、締切と残り時間、チューターとの往復数
2. **冒頭**: 文献、「How this quiz works」（Step 1 → Step 2 の流れを1行で説明）、Background、Question、Key concepts
3. **STEP 1（青いバナー）: Discuss with the AI tutor**
   - 枠内に進捗バー、高さ固定のスクロール式会話欄、入力欄を配置
   - 入力欄（`st.chat_input`）はコンテナ内に置いているため、画面最下部に固定されない。トップレベルに置くと画面下に固定され、回答欄より下に表示されて順序が分かりにくくなるので注意
   - 3往復に達すると「Step 2 へ進んでください」という緑のメッセージを表示
4. **STEP 2（緑のバナー）: Write and submit your final answer**
   - 回答欄、語数カウント、提出条件の案内、Submit ボタン
   - 提出条件: 氏名入力済み、3往復以上、語数が `word_limit` の範囲内

バナーの色や文言は `pit_quiz_app.py` の `STEP_CSS` と `step_banner()` で変更できる。

## Secrets（Streamlit Cloud, TOML）
Comparative Methods と同じサービスアカウントを流用し、`GOOGLE_SHEET_ID` だけ新しいシートのIDにする。

```toml
ANTHROPIC_API_KEY = "sk-ant-..."
GOOGLE_SHEET_ID = "PIT用スプレッドシートのID"

[GOOGLE_CREDENTIALS]
type = "service_account"
# ...（CMアプリと同じ値）
```

## 毎週のクイズ追加手順
1. `pit_quizzes.py` の `PIT_QUIZZES` リストに辞書を追加する（`"active": True`）。
2. 前週のクイズは `"active": False` にする（一覧から消える。エントリ自体は記録として残す）。
3. GitHub に push すると Streamlit Cloud に自動で反映される。

キー: `id`, `active`, `week_label`, `title`, `assigned_date`, `due_date`（"YYYY-MM-DD HH:MM", JST）,
`reading`, `scenario`, `question`, `word_limit`, `concepts`, `opening_message`, `tutor_extra`。

`tutor_extra` には、チューターの誘導手順・想定される正答の核・よくある誤解の訂正方法を書く。

## 現在登録済みのクイズ

| ID | タイトル | 文献 | 締切（JST） | 状態 |
|---|---|---|---|---|
| pit-1 | Calculus vs. Cultural Approaches to Institutions | Hall & Taylor (1996) | 2026-10-13 12:00 | inactive |
| pit-2 | Beyond Leviathan and Privatization | Ostrom (1990), Ch. 1–2 (pp. 1–57) | 2026-10-20 12:00 | active |

## 更新履歴

- 2026-10-07: アプリ公開、pit-1 を登録
- 2026-10-18: pit-2 を追加し pit-1 を非公開化。画面を STEP 1（チューターとの対話）→ STEP 2（回答提出）の順に再構成し、色付きバナーで区別
