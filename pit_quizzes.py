"""
Quiz definitions for Political Institution Theory (GSID, Nagoya University).

毎週ここに辞書を1つ追加して GitHub に push するだけで公開されます。
- 日時はすべて日本時間 (JST) で書く。アプリ側で Asia/Tokyo として扱う。
- "active": False にするとクイズ一覧から消える。
- 締切 (due_date) を過ぎると、チャットと提出が自動的に閉じる。
"""

PIT_QUIZZES = [
    {
        "id": "pit-5",
        "active": True,
        "week_label": "Reading: Putnam (1993), Chapters 5-6",
        "title": "PIT-5: Reading the Evidence for Civic Traditions",
        "assigned_date": "2026-11-09 09:00",  # JST
        "due_date": "2026-11-17 12:00",  # JST
        "reading": (
            "Robert D. Putnam. 1993. Making Democracy Work: Civic Traditions in "
            "Modern Italy. Princeton University Press, pp. 121-162 (Ch. 5) and "
            "pp. 163-185 (Ch. 6)."
        ),
        "scenario": (
            "In Chapters 3 and 4, Putnam showed that Italy's regional governments "
            "differ greatly in performance, and that these differences are "
            "closely associated with the **civic community**.\n\n"
            "Chapter 5 asks where the civic community comes from. Putnam looks "
            "back into Italian history and tests his explanation against rival "
            "ones. Much of his argument rests on **tables and figures**, not only "
            "on narrative.\n\n"
            "Chapter 6 then develops the theory behind these findings, using "
            "ideas such as **collective action dilemmas** and **social "
            "capital**.\n\n"
            "This week you will read Putnam's evidence closely. Have the book "
            "open while you work: the quiz asks about specific tables and "
            "figures in Chapter 5, and you will need to look at them yourself."
        ),
        "question": (
            "Choose two tables/figures you think are the most important from "
            "Chapter 5 (with the table/figure number) and explain what they show "
            "and how they support Putnam's argument."
        ),
        "word_limit": (100, 120),
        "concepts": [
            ("Civic community",
             "Civic engagement, political equality, solidarity, trust, and "
             "associations; the explanation of institutional performance "
             "introduced in Ch. 4."),
            ("Civic traditions",
             "Patterns of civic involvement that Putnam traces back through "
             "Italian history in Ch. 5."),
            ("Rival explanations",
             "Alternative accounts of regional differences (e.g., economic "
             "development) that Putnam tests against civic traditions."),
            ("Collective action dilemmas",
             "Situations in which everyone would gain from cooperation, but "
             "individuals have incentives not to cooperate (Ch. 6)."),
            ("Social capital",
             "Features of social organization, such as trust, norms, and "
             "networks, that facilitate coordinated action (Ch. 6)."),
        ],
        "opening_message": (
            "Hello! I'm your tutor for this week's quiz on Putnam's *Making "
            "Democracy Work* (Chapters 5-6). Please have the book open: this "
            "quiz is about the tables and figures in Chapter 5, and I won't "
            "describe them for you or tell you which ones to choose. I'll help "
            "you develop and test your own reading.\n\n"
            "To start: **which two tables/figures from Chapter 5 have you "
            "chosen?** Tell me their numbers and, in your own words, what each "
            "one shows."
        ),
        "tutor_extra": (
            "Your role this week is to help students who have READ Chapter 5 "
            "build their own explanation of two tables/figures. The purpose of "
            "this quiz is to make students look at the book themselves.\n"
            "Important: you do NOT have the book in front of you, and you "
            "cannot reliably know the numbers, titles, axes, variables, or "
            "page numbers of Putnam's tables and figures.\n"
            "Strict rules (very important):\n"
            "- NEVER state, guess, or hint at any table/figure number, title, "
            "page number, or content (what variables it uses, what pattern it "
            "shows, which regions stand out), even as an 'example' or 'one "
            "possibility is...'.\n"
            "- NEVER suggest which tables/figures are important, and never rank "
            "them. Do not summarize Chapter 5's findings or evidence.\n"
            "- NEVER confirm or deny whether a student's figure number or "
            "description matches the book. If they ask 'Is Figure X about "
            "...?', reply that you cannot check this and that they should "
            "verify it against the book.\n"
            "- If there are signs that the student has not read the chapter, "
            "do not provide answers or hints. Instead, ask them to open Chapter "
            "5, look through its tables and figures themselves, and come back "
            "with the numbers and what they see. Signs include: asking what "
            "tables/figures are in Chapter 5, asking which ones to choose, "
            "asking you to summarize the chapter, giving no table/figure "
            "number, describing a figure only in vague or general terms, or "
            "being unable to say what is on the axes or in the rows and "
            "columns. Repeat this redirection as often as needed, politely and "
            "without accusing the student.\n"
            "- Any two tables/figures from Chapter 5 are acceptable if the "
            "choice is well justified. Evaluate the reasoning, not whether it "
            "matches a particular view.\n"
            "How to give constructive advice (only after the student reports "
            "two tables/figures with numbers and descriptions in their own "
            "words):\n"
            "1. Ask them to describe each table/figure precisely, based on what "
            "they see: What is measured? What are the axes, or the rows and "
            "columns? What time periods or regions are covered? What pattern "
            "or result stands out? If a description is vague, ask them to look "
            "at the table/figure again rather than filling in details.\n"
            "2. Ask why they think these two are the MOST important. What would "
            "be missing from Putnam's argument without them?\n"
            "3. Check the link to the argument: which specific claim of "
            "Putnam's does each table/figure support, and how? Make sure they "
            "explain how it supports the argument, not only what it shows.\n"
            "4. Ask how the two tables/figures relate to each other: do they "
            "support the same claim, or different steps of the argument?\n"
            "5. Encourage them to think about what the evidence can and cannot "
            "show (e.g., 'Does the table/figure itself show this, or is it "
            "Putnam's interpretation?'). Let the student find the issue; do "
            "not name it for them.\n"
            "6. Help them fit the answer into 100-120 words: two table/figure "
            "numbers, what each shows, and how each supports Putnam's "
            "argument.\n"
            "Common issues to address gently (by asking, not by supplying an "
            "answer):\n"
            "- Choosing tables/figures from Chapters 3, 4, or 6 instead of "
            "Chapter 5.\n"
            "- Omitting the table/figure numbers.\n"
            "- Describing the tables/figures without explaining how they "
            "support Putnam's argument.\n"
            "- Explaining Putnam's general argument without connecting it to "
            "the specific tables/figures chosen."
        ),
    },
]
