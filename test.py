import random
from stat_rolling import fdsix_set, tdsix_set

current_stats = [15, 14, 13, 12, 10, 8]


def main():
    print(f" {int(round((sum(current_stats) / 72), 2) * 100)}%")
    
main()
