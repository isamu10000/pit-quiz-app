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
        "active": False,
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
            "performance** from twelve indicators. They cover three aspects of "
            "government: the **policy process** (e.g., cabinet stability, budget "
            "promptness, statistical and information services), **policy "
            "pronouncements** (e.g., reform legislation, legislative innovation), "
            "and **policy implementation** (e.g., day care centers, family "
            "clinics, industrial policy instruments, agricultural spending "
            "capacity, local health unit expenditures, housing and urban "
            "development, bureaucratic responsiveness). Putnam argues that a good "
            "measure should be comprehensive, internally consistent, reliable "
            "over time, and consistent with the judgments of the regions' own "
            "constituents, and he checks the index against surveys of community "
            "leaders and ordinary citizens.\n\n"
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
    {
        "id": "pit-5",
        "active": True,
        "week_label": "Reading: Herbst (1990); Slater (2008)",
        "title": "PIT-5: Criticizing Theories of State-Building",
        "assigned_date": "2026-11-17 09:00",  # JST
        "due_date": "2026-11-24 12:00",  # JST
        "reading": (
            "Jeffrey Herbst. 1990. \"War and the State in Africa.\" International "
            "Security 14 (4), pp. 117-139.\n"
            "Dan Slater. 2008. \"Can Leviathan be Democratic? Competitive "
            "Elections, Robust Mass Politics, and State Infrastructural Power.\" "
            "Studies in Comparative International Development 43 (3-4), "
            "pp. 252-272."
        ),
        "scenario": (
            "Why do some states in the Global South manage to tax, administer, "
            "and reach into their territories while others do not? This week's "
            "two readings offer different answers.\n\n"
            "**Herbst (1990)** starts from the European experience, in which war "
            "has long been seen as a driving force of state formation, and asks "
            "what happens to state-building in Africa, where states have rarely "
            "fought interstate wars and boundaries have remained largely "
            "unchanged.\n\n"
            "**Slater (2008)** asks whether democratic politics can strengthen "
            "states. Drawing on evidence from Southeast Asia, he examines how "
            "competitive elections and mass political mobilization relate to "
            "state **infrastructural power**.\n\n"
            "Every theory rests on claims that can be questioned. This week you "
            "will pick one specific claim in the readings, criticize it, and "
            "support your criticism with evidence from a country you know."
        ),
        "question": (
            "Choose any passage from the assigned literature (not from the "
            "abstract, introduction, or conclusion; give the page number) and "
            "criticize it. In doing so, present an empirical example from a "
            "country you know that supports your criticism. Write your answer in "
            "100 to 120 words."
        ),
        "word_limit": (100, 120),
        "concepts": [
            ("State-building",
             "The development of a state's capacity to control its territory, "
             "extract resources, and implement decisions."),
            ("War and state-making",
             "The argument, associated with Charles Tilly and others, that war "
             "drove the formation of European states. Herbst asks whether this "
             "applies in Africa."),
            ("Infrastructural power",
             "Michael Mann's term for the state's capacity to penetrate society "
             "and implement decisions throughout its territory."),
            ("Despotic power",
             "Michael Mann's term for the range of actions state elites can take "
             "without routine negotiation with society."),
            ("Competitive elections and mass mobilization",
             "The two democratic features whose effects on infrastructural power "
             "Slater examines."),
            ("Criticizing a passage",
             "Identifying a specific claim, explaining why it is wrong, "
             "incomplete, or limited in scope, and backing that judgment with "
             "evidence."),
        ],
        "opening_message": (
            "Hello! I'm your tutor for this week's quiz on Herbst (1990) and "
            "Slater (2008). I won't write the answer for you, and I won't point "
            "you to passages or tell you what to criticize. I'll help you "
            "develop and test your own argument.\n\n"
            "To start: **which passage caught your attention while reading, "
            "and what about it made you doubt it?** A first rough idea is fine."
        ),
        "tutor_extra": (
            "Your role this week is to draw out and strengthen the student's OWN "
            "criticism. Do not anticipate a direction for the student. Support "
            "the ideas the student brings, and help them develop those ideas "
            "in the student's own way.\n"
            "Neutrality rules (very important):\n"
            "- Do NOT suggest, hint at, or rank passages, criticisms, countries, "
            "or empirical examples, even as 'examples' or 'one possibility "
            "is...'. Do not steer students toward any favored author, claim, "
            "line of critique, or case.\n"
            "- Always ask first what the student thinks, then respond to THEIR "
            "idea. If a student has no idea yet, ask open questions that send "
            "them back to their own reading (e.g., 'While reading, where did you "
            "find yourself disagreeing or wanting to add \"but...\"?', 'Which "
            "claim would you most like to test against a country you know "
            "well?'), without supplying an answer.\n"
            "- Any reasonable, well-argued criticism is acceptable. Evaluate the "
            "reasoning, not whether it matches a particular view.\n"
            "Hints from the original literature (very important):\n"
            "- Whenever a student asks for a hint from the readings (e.g., "
            "'Which passage should I use?', 'What does Herbst say about X?', "
            "'Where does Slater discuss Y?', 'Can you give me a quote?', 'Which "
            "page is this on?'), do NOT provide quotes, page numbers, passage "
            "locations, or summaries of specific sections. Instead, suggest "
            "warmly that they go back to the text and check it themselves, and "
            "offer to discuss what they find afterwards.\n"
            "- Do not confirm or correct the wording or page number of a quote "
            "from memory. Ask the student to double-check it against the PDF "
            "themselves.\n"
            "- Do not tell students where the abstract, introduction, or "
            "conclusion begins or ends. If it is unclear, ask them which section "
            "of the article their passage comes from and how they know.\n"
            "How to give constructive advice:\n"
            "1. Make sure the answer covers all parts: a specific passage with a "
            "page number, a criticism of it, and an empirical example from a "
            "country that supports the criticism.\n"
            "2. Check that the student is criticizing the passage rather than "
            "summarizing it. Ask 'What exactly is wrong, incomplete, or too "
            "narrow in this claim?'\n"
            "3. Check that the criticism targets what the passage actually says. "
            "Ask the student to restate the author's claim in their own words "
            "before criticizing it. If the restatement seems to stretch the "
            "text, ask them to re-read the passage rather than correcting it for "
            "them.\n"
            "4. Check the logical link: does the empirical example actually "
            "support the criticism? Ask 'How exactly does this case show that "
            "the claim is wrong or limited?'\n"
            "5. Ask the student to make the example concrete: which country, "
            "which period, what happened, and what evidence (data, events, "
            "sources) shows it. Encourage them to verify any facts or figures "
            "themselves; do not supply or confirm facts about the case.\n"
            "6. Optionally, invite the student to consider whether the author "
            "might have an answer to their criticism, and how they would "
            "respond. Let the student look for it in the text; do not point to "
            "where or what it is.\n"
            "7. Help them fit the answer into 100-120 words: passage and page, "
            "criticism, empirical example, and why the example supports the "
            "criticism.\n"
            "Common issues to address gently (by asking, not by supplying an "
            "answer):\n"
            "- Choosing a passage from the abstract, introduction, or "
            "conclusion, or giving no page number.\n"
            "- Summarizing or agreeing with the passage instead of criticizing "
            "it.\n"
            "- Criticizing the author's general topic or conclusion instead of "
            "the specific passage chosen.\n"
            "- Giving an example that is unrelated to the criticism, too vague "
            "to check (no country, period, or evidence), or that actually "
            "supports the author.\n"
            "- Listing several criticisms superficially instead of developing "
            "one."
        ),
    },
]
