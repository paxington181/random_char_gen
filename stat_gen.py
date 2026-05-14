import random

def standard_set():
    return [15, 14, 13, 12, 10, 8]

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
    fdssix_list: int = []
    for i in range(0, 6):
        fdssix_list.append(tdsix_roll())
        i += 1

    fdssix_sorted: int = sorted(fdssix_list)    
    fdssix_flipped: int = fdssix_sorted[::-1]
    fdssix_sum: int = sum(fdssix_list)
    fdssix_rounded: float = round((fdssix_sum / 72), 2)
    
    print(f"Your stats are {fdssix_flipped}")
    print(f"The sum of your stats: {fdssix_sum}")
    print(f"The sum of rolled stats are {int(fdssix_rounded * 100)}% of the sum of the standard array.")
    
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

    fdssix_stats()

main()
