import random
import math

def fdsix():
    fds_list: list[int] = []
    for i in range(0, 4):
        fds_list.append(random.randrange(1, 7))
        i += 1
    fds_sorted: list[int] = sorted(fds_list)
    fds_sum: int = sum(fds_sorted[1:])
    fds_sorted.append(fds_sum)
    fds_flipped = fds_sorted[::-1]
    return fds_flipped

def main():
    test = fdsix()
    print(test)
    
main()
