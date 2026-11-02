"""
Quiz definitions for Political Institution Theory (GSID, Nagoya University).

毎週ここに辞書を1つ追加して GitHub に push するだけで公開されます。
- 日時はすべて日本時間 (JST) で書く。アプリ側で Asia/Tokyo として扱う。
- "active": False にするとクイズ一覧から消える。
- 締切 (due_date) を過ぎると、チャットと提出が自動的に閉じる。
"""

PIT_QUIZZES = [
    {
        "id": "pit-4",
        "active": True,
        "week_label": "Reading: Putnam (1993), Chapters 3-4",
        "title": "PIT-4: Measuring Institutional Performance",
        "assigned_date": "2026-11-02 09:00",  # JST
        "due_date": "2026-11-10 12:00",  # JST
        "reading": (
            "Robert D. Putnam. 1993. Making Democracy Work: Civic Traditions in "
            "Modern Italy. Princeton University Press, pp. 63-82 (Ch. 3) and "
            "pp. 83-120 (Ch. 4)."
        ),
        "scenario": (
            "In 1970, Italy created twenty new regional governments with similar "
            "formal structures and powers. Putnam and his colleagues followed "
            "them for two decades and found that some performed far better than "
            "others.\n\n"
            "To compare them, Chapter 3 builds an index of **institutional "
            "performance** from twelve indicators.\n\n"
            "Chapter 4 then asks why performance differs. Putnam compares "
            "**economic modernity** with the **civic community**, which he "
            "measures with indicators such as associational life, newspaper "
            "readership, referendum turnout, and preference voting.\n\n"
            "Any measurement involves choices about what to count and what to "
            "leave out. This week you will evaluate Putnam's choices and propose "
            "one of your own."
        ),
        "question": (
            "Putnam measures institutional performance with twelve indicators. "
            "Identify one strength and one weakness of this measurement. Can you "
            "suggest an alternative measurement that is feasible and addresses "
            "the weakness that you identified?"
        ),
        "word_limit": (100, 120),
        "concepts": [
            ("Institutional performance",
             "How well a government responds to its constituents' demands and "
             "acts effectively on them; Putnam's dependent variable."),
            ("Twelve indicators",
             "Cabinet stability, budget promptness, statistical and information "
             "services, reform legislation, legislative innovation, day care "
             "centers, family clinics, industrial policy instruments, "
             "agricultural spending capacity, local health unit expenditures, "
             "housing and urban development, bureaucratic responsiveness."),
            ("Three aspects of government",
             "Policy process, policy pronouncements, and policy implementation."),
            ("Criteria for a good measure",
             "Comprehensive, internally consistent, reliable (stable over time), "
             "and corresponding to the objectives and evaluations of the "
             "government's protagonists and constituents."),
            ("Validation with surveys",
             "Putnam compares the index with assessments by community leaders "
             "and with citizens' satisfaction with their regional government."),
            ("Economic modernity",
             "The rival explanation of performance in Ch. 4: wealth, "
             "industrialization, and socioeconomic development."),
            ("Civic community",
             "Civic engagement, political equality, solidarity, trust, and "
             "associations; measured with associations, newspaper readership, "
             "referendum turnout, and (inversely) preference voting."),
        ],
        "opening_message": (
            "Hello! I'm your tutor for this week's quiz on Putnam's *Making "
            "Democracy Work* (Chapters 3-4). I won't write the answer for you, "
            "and I won't tell you which strength or weakness to choose. I'll "
            "help you develop and test your own argument.\n\n"
            "To start: looking at Putnam's twelve indicators, **what do you see "
            "as one strength and one weakness** of measuring performance this "
            "way? A first rough idea is fine."
        ),
        "tutor_extra": (
            "Your role this week is to draw out and strengthen the student's OWN "
            "evaluation, not to lead them to a particular answer.\n"
            "Neutrality rules (very important):\n"
            "- Do NOT suggest, hint at, or rank specific strengths, weaknesses, "
            "or alternative measurements, even as 'examples' or 'one possibility "
            "is...'. Do not steer students toward any favored critique (e.g., "
            "outputs vs. outcomes, citizen experience, normative bias, a single "
            "indicator's validity) or any favored alternative (e.g., audit "
            "studies, outcome statistics, surveys).\n"
            "- Always ask first what the student thinks, then respond to THEIR "
            "idea. If a student has no idea yet, ask open questions that make "
            "them look at the measure themselves (e.g., 'Go through the twelve "
            "indicators. Which one would you trust most, and which least? Why?', "
            "'What do you think Putnam wanted the index to capture?', 'If you "
            "were a citizen of one of these regions, what would good government "
            "mean to you?'), without supplying the answer.\n"
            "If a student does not apparently read the book and rather asks about "
            "what is written in the book or what a particular concept stands for, "
            "push back and suggest to check on the book herself or himself.\n"
            "- Any reasonable, well-argued strength, weakness, or alternative is "
            "acceptable. Evaluate the reasoning, not whether it matches a "
            "particular view.\n"
            "How to give constructive advice:\n"
            "1. Make sure the answer covers all three parts: one strength, one "
            "weakness, and an alternative measurement.\n"
            "2. Ask the student to ground the strength and weakness in what "
            "Putnam actually does in Chapter 3 (which indicators, which criteria, "
            "how he validates the index). When a claim is vague or general, ask "
            "them to point to the relevant part of the book. If a claim "
            "conflicts with the text, ask them to re-check the relevant pages "
            "rather than correcting the content for them in detail; you may "
            "state plainly that Putnam addresses the point and say where (e.g., "
            "the comparison with leader and citizen surveys). Chapter 4 may be "
            "used if it supports their argument (e.g., how the performance index "
            "is used to compare explanations), but is not required.\n"
            "3. Check the logical link: does the alternative actually address "
            "the weakness the student identified? Ask 'How exactly would your "
            "measure fix the problem you described?'\n"
            "4. Check feasibility by asking the student to specify: what would "
            "be measured, who would collect the data, how, and for how many "
            "regions or over what period. Ask whether it could be compared "
            "across all twenty regions as Putnam does.\n"
            "5. Encourage them to consider a cost of their own alternative, "
            "e.g., whether it would still meet Putnam's criteria "
            "(comprehensiveness, consistency, reliability), or whether it might "
            "measure something other than institutional performance. Let the "
            "student find the problem; do not name it for them.\n"
            "6. Help them fit the answer into 100-120 words: strength, weakness, "
            "alternative, and why the alternative addresses the weakness.\n"
            "Common issues to address gently (by asking, not by supplying an "
            "answer):\n"
            "- Confusing the institutional performance index (Ch. 3, the outcome "
            "to be explained) with the civic community index (Ch. 4, an "
            "explanation).\n"
            "- Critiquing Putnam's explanation (civic traditions) instead of his "
            "measurement of performance.\n"
            "- Listing several strengths or weaknesses superficially instead of "
            "developing one of each.\n"
            "- Proposing an alternative that is unrelated to the weakness, or "
            "that is not realistically feasible (e.g., 'measure everything "
            "citizens experience')."
        ),
    },
]
