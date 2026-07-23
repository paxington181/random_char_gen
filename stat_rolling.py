import random
import math

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
        roll = fdsix()
        fdsix_set_list.append(roll)
        sum += roll[0]
        i +=1
    fds_set_sorted = sorted(fdsix_set_list)
    fds_set_flipped = fds_set_sorted[::-1]
    fds_set_flipped.append(sum)
    return fds_set_flipped

def mdsix_set():
    mdsix_set_list: list[list[int]] = []
    sum = 0
    for i in range(0, 3):
        roll = tdsix()
        mdsix_set_list.append(roll)
        sum += roll[0]
        i +=1
    for i in range(0, 3):
        roll = fdsix()
        mdsix_set_list.append(roll)
        sum += roll[0]
        i +=1
    mds_set_sorted = sorted(mdsix_set_list)
    mds_set_flipped = mds_set_sorted[::-1]
    mds_set_flipped.append(sum)
    return mds_set_flipped

def mdsix_set_shuffle():
    mdsix_set_list: list[list[int]] = []
    sum = 0
    for i in range(0, 6):
        rolling_methods: list[function] = [tdsix(), fdsix()]
        dice = rolling_methods[random.randrange(0, len(rolling_methods))]
        roll = dice
        mdsix_set_list.append(roll)
        sum += roll[0]
        i += 1
    mds_set_sorted = sorted(mdsix_set_list)
    mds_set_flipped = mds_set_sorted[::-1]
    mds_set_flipped.append(sum)
    return mds_set_flipped

def hc_tdsix_set():
    hc_tdsix_set_list : list[list[int]] = []
    sum = 0
    for i in range(0, 6):
        roll = tdsix()
        hc_tdsix_set_list.append(roll)
        sum += roll[0]
        i += 1
    hc_tdsix_set_list.append(sum)
    return hc_tdsix_set_list

def hc_fdsix_set():
    hc_fdsix_set_list : list[list[int]] = []
    sum = 0
    for i in range(0, 6):
        roll = fdsix()
        hc_fdsix_set_list.append(roll)
        sum += roll[0]
        i += 1
    hc_fdsix_set_list.append(sum)
    return hc_fdsix_set_list

def hc_mdsix_set():
    hc_mdsix_set_list: list[list[int]] = []
    sum = 0
    for i in range(0, 6):
        rolling_methods: list[function] = [tdsix(), fdsix()]
        dice = rolling_methods[random.randrange(0, len(rolling_methods))]
        roll = dice
        hc_mdsix_set_list.append(roll)
        sum += roll[0]
        i += 1
    hc_mdsix_set_list.append(sum)
    return hc_mdsix_set_list

def standard():
    return [[15, 5, 5, 5], [14, 5, 5, 4], [13, 5, 5, 3], [12, 4, 4, 4], [10, 4, 3, 3], [8, 4, 2, 2]]

def modifier_calc(current_stat):
        mod = math.floor((current_stat - 10) / 2)
        if mod >= 0:
            return f"+{mod}"
        return mod