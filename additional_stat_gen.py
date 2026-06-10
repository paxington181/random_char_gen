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



def main():
    print(mdsix_set())
    

main()
