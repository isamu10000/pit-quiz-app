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
        "active": False,
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
    {
        "id": "pit-2",
        "active": True,
        "week_label": "Reading: Ostrom (1990), Chapters 1-2",
        "title": "PIT-2: Beyond Leviathan and Privatization",
        "assigned_date": "2026-10-14",
        "due_date": "2026-10-20 12:00",  # JST
        "reading": (
            "Elinor Ostrom. 1990. Governing the Commons: The Evolution of "
            "Institutions for Collective Action. Cambridge University Press, "
            "pp. 1-28 (Ch. 1) and pp. 29-57 (Ch. 2)."
        ),
        "scenario": (
            "Ostrom starts from three influential models that predict the overuse "
            "of shared resources: Hardin's **tragedy of the commons**, the "
            "**prisoner's dilemma**, and Olson's **logic of collective action**. "
            "In each, individuals who act rationally on their own produce an "
            "outcome that is bad for all of them.\n\n"
            "From these models, analysts have drawn two opposite policy "
            "prescriptions, each presented as the *only* way out:\n"
            "- **Leviathan**: a central government should take control of the "
            "resource, decide who may use it and how much, and punish violators.\n"
            "- **Privatization**: the commons should be divided and turned into "
            "private property, so that each owner bears the costs and benefits "
            "of their own use.\n\n"
            "Ostrom rejects both as universal solutions. She points to communities "
            "of fishers, herders, and irrigators that have designed and enforced "
            "their own rules for long periods, and in Chapter 2 she asks how a "
            "group of resource users can organize themselves to solve the problems "
            "of supplying institutions, making credible commitments, and "
            "monitoring one another."
        ),
        "question": (
            "Ostrom rejects both 'Leviathan' and 'privatization' as solutions to "
            "the commons dilemma. What assumption do these two solutions share, "
            "and why does Ostrom think it is wrong?"
        ),
        "word_limit": (100, 120),
        "concepts": [
            ("Tragedy of the commons / prisoner's dilemma / logic of collective action",
             "Three models in which individually rational behavior leads to "
             "collectively irrational outcomes such as overgrazing or free riding."),
            ("Leviathan solution",
             "Central (external) authority owns or regulates the resource and "
             "imposes rules and sanctions on users."),
            ("Privatization solution",
             "The commons is divided into private property rights, so each owner "
             "internalizes the costs of their own use."),
            ("Common-pool resource (CPR)",
             "A resource system where excluding users is costly and one person's "
             "use subtracts from what is left for others."),
            ("Resource system vs. resource units",
             "The stock (e.g., a fishing ground) vs. the flow appropriated from it "
             "(e.g., tons of fish caught)."),
            ("Appropriators and providers",
             "Those who withdraw resource units vs. those who arrange for the "
             "provision or maintenance of the resource."),
            ("Self-organization",
             "Users themselves devise, monitor, and enforce rules, e.g., via a "
             "binding agreement they enforce or pay for themselves."),
            ("Three puzzles (Ch. 2)",
             "The supply of new institutions, credible commitment to follow the "
             "rules, and mutual monitoring."),
        ],
        "opening_message": (
            "Hello! I'm your tutor for this week's quiz on Ostrom's *Governing the "
            "Commons* (Chapters 1-2). I won't write the answer for you, but I'll "
            "help you build your argument.\n\n"
            "To start: Leviathan and privatization look like opposites, state vs. "
            "market. **In each solution, who designs and enforces the rules?** "
            "And where are the resource users themselves in that picture?"
        ),
        "tutor_extra": (
            "Guide the student through these steps, roughly in order, adapting to "
            "where they are:\n"
            "1. Get the student to describe each solution concretely: who decides "
            "the rules, who monitors, who sanctions. Leviathan relies on a central "
            "authority; privatization also needs someone to define, assign, and "
            "enforce property rights.\n"
            "2. Lead them to the shared assumption. The core answer: both treat "
            "the resource users as trapped in the dilemma and unable to change "
            "their own situation, so the institutional solution must be designed "
            "and imposed from outside (by the state or by an externally enforced "
            "property-rights regime). A related, acceptable layer: both rest on "
            "the models' assumptions that users cannot communicate, build trust, "
            "or make binding agreements among themselves, and both take for "
            "granted that the external designer has accurate information and can "
            "monitor and sanction at low cost.\n"
            "3. Push them to explain WHY Ostrom thinks this is wrong, using the "
            "reading: (a) empirically, many groups of appropriators (e.g., the "
            "inshore fishers she discusses who allocate fishing spots among "
            "themselves) have crafted and enforced their own rules for long "
            "periods; (b) the models fit only some settings. Real CPR users often "
            "interact repeatedly, can talk, and can change their rules; "
            "(c) external solutions have their own costs and failure points: a "
            "central agency with incomplete information can impose the wrong "
            "rules and sanctions, and some resources (e.g., moving fish stocks, "
            "uncertain rainfall on pastures) cannot easily be divided into "
            "private parcels; (d) users can reach a better outcome through a "
            "self-designed and self-enforced agreement.\n"
            "4. Ask them to connect the critique to Chapter 2: self-organization "
            "is possible but not automatic, which is why Ostrom poses the puzzles "
            "of supplying institutions, credible commitment, and mutual monitoring.\n"
            "Common misunderstandings to correct gently:\n"
            "- Saying the shared assumption is simply 'people are selfish' or "
            "'people are rational'. Ostrom keeps rational, self-interested actors "
            "in her own analysis. Ask what, beyond self-interest, the models "
            "assume about users' ability to communicate and change rules.\n"
            "- Reading Ostrom as anti-state, anti-market, or as claiming that "
            "communities always succeed. She rejects any single panacea, accepts "
            "that tragedies do happen, and notes that real institutions often "
            "mix public and private elements. Her question is under what "
            "conditions self-organization works.\n"
            "- Confusing a common-pool resource with a pure public good. Use of a "
            "CPR is subtractable.\n"
            "- Listing the problems of Leviathan and of privatization separately "
            "without identifying what they have in common. The question asks for "
            "the shared assumption."
        ),
    },
]
