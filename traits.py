import random

align_law_chaos: list[str] = ["lawful", "neutral", "chaotic"]
lc_weight: list[int] = [30, 30, 30]
align_good_evil: list[str] = ["good", "neutral", "evil"]
ge_weight: list[str] = [50, 50, 30]
align_chaos: list[str] = ["boastful", "impulsive", "rebellious", "self-absorbed"]
align_good: list[str] = ["compassionate", "helpful", "honest", "kind"]
align_evil: list[str] = ["dishonest", "vengeful", "cruel", "greedy"]
align_lawful: list[str] = ["cooperative", "loyal", "judgemental", "methodical"]
align_neutral: list[str] = ["selfish", "disinterested", "laconic", "pragmatic"]

virtues: list[str] = ["humility", "charity", "patience", "kindness", "chastity", "temperance", "diligence"]
bond: list[str] = ["self", "familial", "organizational", "community", "region", "country"]
flaw: list[str] = ["prideful", "greedy", "wrathful", "envious", "lustful", "gluttonous", "slothful"]

family: list[str] = ["child", "children", "sister", "brother", "multiple siblings", "parent", "both parents"]
mentor: list[str] = ["relative", "wandering stranger", "school", "family", "military"]
mentor_attitude: list[str] = ["friendly", "neutral", "hostile"]


generic_events: list[str] = ["party member death", 
                             "near party wipe", 
                             "player leaves group", 
                             "class specific magic item", 
                             "character ability saves day", 
                             "ability proved useless", 
                             "overshadowed by others", 
                             "backstory plothook used", 
                             "player changes character", 
                             "major character injury"
                             ]
tier_one_events: list[str] = ["character idea doesn't fit campaign"]
tier_two_events: list[str] = []
tier_three_events: list[str] = ["campaign focus changed"]
tier_four_events: list[str] = []
tier_five_events: list[str] = []

party_members: list[str] = []
