import random

def standard_set():
    return [8, 10, 12, 13, 14, 15]

def fdsix_roll():
    fds_list: int = []
    for i in range(0, 4):
        fds_list.append(random.randrange(1, 7))
        i += 1
    fds_sorted: int = sorted(fds_list)
    fds_flipped: int = fds_sorted[::-1]
    fds_three: int = fds_flipped[:3]
    print(fds_three)
    fds_sum: int = sum(fds_three)
    print(fds_sum)
    return fds_sum

def fdssix_stats():
    stats_sum: int = []
    for i in range(0, 6):
        stats_sum.append(fdsix_roll())
        i += 1

    print(stats_sum)
    sum_stats: int = sum(stats_sum)
    sum_rounded: float = round((sum_stats / 72), 2)
        

    print(f"The sum of your stats: {sum(stats_sum)}")
    print(f"The sum of rolled stats are {int(sum_rounded * 100)}% of the sum of the standard array.")
    
def tdsix_roll():
    tds_list: int = []
    for i in range(0, 3):
        tds_list.append(random.randrange(1, 7))
        i += 1
    tds_sorted: int = sorted(tds_list)
    tds_flipped: int = tds_sorted[::-1]
    print(tds_flipped)
    tds_sum = sum(tds_flipped)
    print(tds_sum)
    return tds_sum

def tdssix_stats():
    tdssix_list: int = []
    for i in range(0, 6):
        tdssix_list.append(tdsix_roll())
        i += 1

    tdssix_sorted: int = sorted(tdssix_list)    
    tdssix_flipped: int = tdssix_sorted[::-1]
    tdssix_sum: int = sum(tdssix_list)
    tdssix_rounded: float = round((tdssix_sum / 72), 2)
    
    print(f"Your stats are {tdssix_flipped}")
    print(f"The sum of your stats: {tdssix_sum}")
    print(f"The sum of rolled stats are {int(tdssix_rounded * 100)}% of the sum of the standard array.")


def main():

    tdssix_stats()

main()
