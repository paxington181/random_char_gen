import random

base_races: str = []


base_classes: str = []


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




    main()