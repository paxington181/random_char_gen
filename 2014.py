import random

base_races: str = []


base_classes: str = []


alignment: str = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]

def stat_roll():
    four_rolls: int = []
    for i in range(0, 4):
        four_rolls.append(random.randrange(1, 7))
        i += 1
    four_sorted: int = sorted(four_rolls)
    four_flipped: int = four_sorted[::-1]
    three_rolls: int = four_flipped[:3]
    print(three_rolls)
    rolls_sum: int = sum(three_rolls)
    print(rolls_sum)
    return rolls_sum


def main():

    stats_sum: int = []
    for i in range(0, 6):
        stats_sum.append(stat_roll())
        i += 1

    sum_stats: int = sum(stats_sum)
    sum_rounded:float = round((sum_stats / 72), 2)
        

    print(f"The sum of your stats: {sum(stats_sum)}")
    print(f"The sum of rolled stats are {int(sum_rounded * 100)}% of the sum of the standard array.")
    
    random_alignment = alignment[random.randrange(0, len(alignment))]
    print(f"Alignment selected: {random_alignment}")


main()