import random

def main():
    four_rolls = []
    for i in range(0, 4):
        four_rolls.append(random.randrange(1, 7))
        i += 1
    print(four_rolls)

    four_sorted = sorted(four_rolls)
    print(four_sorted)

    four_flipped = four_sorted[::-1]
    print(four_flipped)

    three_rolls = four_flipped[:3]
    print(three_rolls)

    rolls_sum = sum(three_rolls)
    print(rolls_sum)

main()