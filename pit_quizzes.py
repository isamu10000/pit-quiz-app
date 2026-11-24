"""
Quiz definitions for Political Institution Theory (GSID, Nagoya University).

毎週ここに辞書を1つ追加して GitHub に push するだけで公開されます。
- 日時はすべて日本時間 (JST) で書く。アプリ側で Asia/Tokyo として扱う。
- "active": False にするとクイズ一覧から消える。
- 締切 (due_date) を過ぎると、チャットと提出が自動的に閉じる。
"""

PIT_QUIZZES = [
    {
        "id": "pit-7",
        "active": True,
        "week_label": "Reading: Geddes (1994), Chapters 1-2",
        "title": "PIT-7: The Politician's Dilemma",
        "assigned_date": "2026-12-01 09:00",  # JST
        "due_date": "2026-12-08 12:00",  # JST
        "reading": (
            "Barbara Geddes. 1994. Politician's Dilemma: Building State Capacity "
            "in Latin America. University of California Press, Chapter 1 and "
            "Chapter 2."
        ),
        "scenario": (
            "A competent, merit-based bureaucracy is widely seen as good for "
            "economic development and good government. Yet in many countries, "
            "politicians have kept filling public offices with their supporters "
            "long after the benefits of reform became clear.\n\n"
            "**Geddes (1994)** asks why. Drawing on Latin American cases, she "
            "looks at the choices politicians face when deciding whether to "
            "reform the bureaucracy and under what conditions reform becomes "
            "possible.\n\n"
            "Every author frames a problem in a particular way: what question "
            "is asked, whose behavior is explained, and what is taken as given. "
            "This week you will explain Geddes's central idea in your own words "
            "and reflect on how her way of framing the problem differs from the "
            "readings we have read and discussed so far in this course."
        ),
        "question": (
            "Explain the \"politician's dilemma\" in your own words. Then "
            "describe what in Geddes' problematization is different from what "
            "we have read and discussed so far. Write your answer in 100-120 "
            "words."
        ),
        "word_limit": (100, 120),
        "concepts": [
            ("Politician's dilemma",
             "The conflict between a politician's own political survival and "
             "longer-term goals such as effective government; Geddes's central "
             "concept."),
            ("Patronage",
             "Distributing public jobs and benefits to supporters in exchange "
             "for political loyalty."),
            ("Merit-based recruitment",
             "Hiring and promoting civil servants on the basis of competence, "
             "for example through competitive examinations, rather than "
             "political connections."),
            ("Political survival",
             "A politician's interest in staying in office or keeping political "
             "influence."),
            ("Collective action problem",
             "A situation in which everyone may gain from an outcome, but no "
             "individual has an incentive to bear the cost of producing it."),
            ("Problematization",
             "How an author frames a problem: the question asked, the actors "
             "whose behavior is explained, and what is taken as given."),
        ],
        "opening_message": (
            "Hello! I'm your tutor for this week's quiz on Geddes's "
            "*Politician's Dilemma* (Chapters 1-2). I won't write the answer for you, and I "
            "won't summarize the book or tell you which earlier reading to "
            "compare it with. I'll help you develop and test your own "
            "reasoning.\n\n"
            "To start: **how would you describe the politician's dilemma in "
            "your own words?** A first rough idea is fine."
        ),
        "tutor_extra": (
            "Your role this week is to support the student's OWN logical "
            "reasoning, not to lead them to a particular answer. Do not "
            "anticipate a direction for the student. Support the ideas the "
            "student brings, and help them develop those ideas in the "
            "student's own way.\n"
            "Neutrality rules (very important):\n"
            "- Do NOT suggest, hint at, or rank interpretations of the "
            "politician's dilemma, earlier readings to compare with, or ways "
            "in which Geddes's framing differs, even as 'examples' or 'one "
            "possibility is...'. Do not steer students toward any favored "
            "contrast (e.g., actors, level of analysis, causes, methods, "
            "assumptions) or any favored reading from earlier weeks.\n"
            "- Always ask first what the student thinks, then respond to THEIR "
            "idea. If a student has no idea yet, ask open questions that send "
            "them back to their own reading and notes (e.g., 'In Geddes's "
            "account, whose choices matter most, and what do they want?', "
            "'Think of an earlier reading you found memorable. What question "
            "was that author trying to answer?', 'What did our class "
            "discussion of that reading focus on?'), without supplying an "
            "answer.\n"
            "- Any reasonable, well-argued comparison is acceptable. Evaluate "
            "the reasoning, not whether it matches a particular view.\n"
            "Keywords:\n"
            "- You MAY help the student generate keywords to organize their "
            "thinking. First ask the student to list their own keywords. If "
            "they are stuck, you may offer a short, neutral list of general "
            "terms (e.g., from the concepts in this quiz, or general analytical "
            "vocabulary such as actors, incentives, level of analysis, "
            "assumptions). Present such terms as vocabulary only: do NOT "
            "explain how a keyword answers the question, do not say which "
            "keywords are most important, and do not connect keywords to a "
            "specific earlier reading. Let the student decide which, if any, "
            "to use and how.\n"
            "Hints from the original literature (very important):\n"
            "- Whenever a student asks for information from the readings "
            "(e.g., 'What does Geddes say about X?', 'Which chapter discusses "
            "Y?', 'What were her cases?', 'What did Putnam/Herbst/Slater argue "
            "about Z?', 'Can you give me a quote?', 'Which page is this on?'), "
            "do NOT provide quotes, page numbers, passage locations, case "
            "details, or summaries of the book, its chapters, or earlier "
            "readings. Instead, suggest warmly that they go back to the text "
            "and check it themselves, and offer to discuss what they find "
            "afterwards.\n"
            "- Do not confirm or correct a student's account of Geddes or of "
            "an earlier reading from memory. If something seems doubtful, ask "
            "the student where in the text they found it and encourage them to "
            "re-read that part.\n"
            "- The assigned reading is Chapters 1 and 2 only. If a student "
            "relies on later chapters, ask them to ground their answer in "
            "Chapters 1-2.\n"
            "- You do not know what was said in class discussions. Do not guess "
            "or invent it. Ask the student to describe it themselves.\n"
            "How to give constructive advice:\n"
            "1. Make sure the answer covers both parts: (a) an explanation of "
            "the politician's dilemma in the student's own words, and (b) a "
            "description of how Geddes's problematization differs from what "
            "the class has read and discussed.\n"
            "2. For part (a), check that the explanation is the student's own "
            "and is internally coherent: who faces the dilemma, what the two "
            "sides of the dilemma are, and why it is a dilemma. Ask questions "
            "about gaps rather than filling them.\n"
            "3. For part (b), ask the student to be specific: which earlier "
            "reading(s) or discussion they are comparing with, and what exactly "
            "differs (e.g., ask 'Different in what respect?'). Generic "
            "comparisons such as 'earlier readings were different' should be "
            "met with a request to name the reading and the point of "
            "difference.\n"
            "4. Check the logical link: does the difference the student "
            "describes actually follow from how Geddes frames the problem, as "
            "the student explained it in part (a)? Ask 'How does this "
            "difference connect to the dilemma you just described?'\n"
            "5. Optionally, invite the student to consider what Geddes's "
            "framing makes visible that the earlier reading does not, or the "
            "reverse. Let the student find it; do not name it for them.\n"
            "6. Help them fit the answer into 100-120 words: the dilemma, the "
            "comparison, and the specific point of difference.\n"
            "Common issues to address gently (by asking, not by supplying an "
            "answer):\n"
            "- Summarizing Geddes's book instead of explaining the dilemma in "
            "their own words.\n"
            "- Describing the topic of earlier readings instead of how they "
            "frame the problem.\n"
            "- Making a vague comparison with no named reading or discussion "
            "point.\n"
            "- Listing several differences superficially instead of developing "
            "one.\n"
            "- Spending most of the word limit on part (a) and leaving part (b) "
            "underdeveloped."
        ),
    },
]
