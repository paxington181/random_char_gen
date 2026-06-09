import random


def tdsix():
    tds_list: list[int] = []
    for i in range(0, 3):
        tds_list.append(random.randrange(1, 7))
        i += 1
    tds_sorted: list[int] = sorted(tds_list)
    tds_sum: int = sum(tds_sorted)
    tds_sorted.append(tds_sum)
    tds_flipped: list[int] = tds_sorted[::-1]
    return tds_flipped

def fdsix():
    fds_list: list[int] = []
    for i in range(0, 4):
        fds_list.append(random.randrange(1, 7))
        i += 1
    fds_sorted: list[int] = sorted(fds_list)
    fds_sum: int = sum(fds_sorted[1:])
    fds_sorted.append(fds_sum)
    fds_flipped: list[int] = fds_sorted[::-1]
    return fds_flipped

def tdsix_set():
    tdsix_set_list: list[list[int]] = []
    sum = 0
    for i in range(0, 6):
        roll = tdsix()
        tdsix_set_list.append(roll)
        sum += roll[0]
        i +=1
    tds_set_sorted = sorted(tdsix_set_list)
    tds_set_flipped = tds_set_sorted[::-1]
    tds_set_flipped.append(sum)
    return tds_set_flipped

def fdsix_set():
    fdsix_set_list: list[list[int]] = []
    sum = 0
    for i in range(0, 6):
        roll = fdsix
        fdsix_set_list.append(roll)
        sum += roll[0]
        i +=1
    fds_set_sorted = sorted(fdsix_set_list)
    fds_set_flipped = fds_set_sorted[::-1]
    fds_set_flipped.append(sum)
    return fds_set_flipped
