"""
Quiz definitions for Political Institution Theory (GSID, Nagoya University).

毎週ここに辞書を1つ追加して GitHub に push するだけで公開されます。
- 日時はすべて日本時間 (JST) で書く。アプリ側で Asia/Tokyo として扱う。
- "active": False にするとクイズ一覧から消える。
- 締切 (due_date) を過ぎると、チャットと提出が自動的に閉じる。
"""

PIT_QUIZZES = [
    {
        "id": "pit-1",
        "active": True,
        "week_label": "Reading: Hall & Taylor (1996)",
        "title": "PIT-1: Calculus vs. Cultural Approaches to Institutions",
        "assigned_date": "2026-10-07",
        "due_date": "2026-10-13 12:00",  # JST
        "reading": (
            'Peter A. Hall and Rosemary C. R. Taylor. 1996. "Political Science and '
            'the Three New Institutionalisms." Political Studies 44: 936-957.'
        ),
        "scenario": (
            "Hall and Taylor (1996) distinguish three 'new institutionalisms' "
            "(historical, rational choice, and sociological) and show that they "
            "rest on different answers to a basic question: how do institutions "
            "affect the behavior of individuals?\n\n"
            "In the **calculus approach**, people are instrumental and strategic. "
            "Institutions matter because they change expectations about what "
            "others will do: they provide information, enforcement mechanisms, and "
            "penalties for defection. People follow a rule because, given what "
            "they expect of others, following it pays.\n\n"
            "In the **cultural approach**, behavior is not fully strategic but is "
            "bounded by a person's worldview. Institutions supply moral and "
            "cognitive templates (routines, scripts, familiar patterns) that define "
            "what action is appropriate, and sometimes what action is even "
            "imaginable.\n\n"
            "The two approaches also explain why institutions persist: as an "
            "equilibrium that no one gains by leaving, or as conventions so taken "
            "for granted that they are rarely questioned."
        ),
        "question": (
            'Hall and Taylor distinguish a "calculus approach" and a "cultural '
            'approach" to explaining how institutions shape behavior. Choose one '
            "rule that people in your country tend to follow (or ignore), and "
            "explain which approach accounts for it better."
        ),
        "word_limit": (100, 120),
        "concepts": [
            ("Calculus approach",
             "Actors maximize goals instrumentally; institutions shape behavior by "
             "reducing uncertainty about others' actions (information, enforcement, "
             "sanctions)."),
            ("Cultural approach",
             "Behavior is bounded by worldview; institutions provide moral and "
             "cognitive templates that shape interpretation, preferences, and even "
             "identity."),
            ("Institutional persistence",
             "Calculus: rules persist as equilibria that individuals would lose by "
             "abandoning. Cultural: rules persist because they are taken for "
             "granted and rarely become objects of choice."),
            ("Historical institutionalism",
             "Eclectic: draws on both the calculus and cultural approaches."),
            ("Rational choice institutionalism",
             "Builds mainly on the calculus approach."),
            ("Sociological institutionalism",
             "Builds mainly on the cultural approach; emphasizes appropriateness "
             "and legitimacy over efficiency."),
        ],
        "opening_message": (
            "Hello! I'm your tutor for this week's quiz on Hall and Taylor (1996). "
            "I won't write the answer for you, but I'll help you sharpen your "
            "argument.\n\n"
            "To start: **which rule** are you thinking about, and **in which "
            "country**? Do people there mostly follow it or ignore it?"
        ),
        "tutor_extra": (
            "Guide the student through these steps, roughly in order, adapting to "
            "where they are:\n"
            "1. Pin down ONE concrete rule (formal law or informal norm) and whether "
            "people follow or ignore it. Push vague choices ('culture of "
            "punctuality') toward a specific rule.\n"
            "2. Ask what each approach would say is the mechanism behind the "
            "behavior: what costs, benefits, and expectations about others "
            "(calculus) vs. what sense of appropriateness or taken-for-granted "
            "routine (cultural).\n"
            "3. Push for observable evidence that distinguishes the two: Do people "
            "comply when no one is watching or enforcement is absent? Does behavior "
            "change when penalties or incentives change? Do people describe the "
            "rule as 'just what one does', or do they weigh the odds of being "
            "caught? How do newcomers or foreigners behave?\n"
            "4. Require a justified comparison ('which approach accounts for it "
            "better'), not a list of both. It is fine to concede that the other "
            "approach captures part of the story, as historical institutionalists "
            "would.\n"
            "Common misunderstandings to correct gently:\n"
            "- Treating the cultural approach as 'national character' or "
            "stereotype. It is about institutions supplying cognitive and moral "
            "templates, not fixed traits of a people.\n"
            "- Treating the calculus approach as applying only to formal laws. "
            "Informal norms enforced by social sanctions (shame, exclusion, "
            "reputation) can be explained in calculus terms. Ask the student "
            "whether the social pressure they describe works as a sanction "
            "(calculus) or as an internalized sense of what is right or normal "
            "(cultural).\n"
            "- Explaining the rule's origin when the question asks why people "
            "follow or ignore it now."
        ),
    },
]
