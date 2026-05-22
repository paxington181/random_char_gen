import random
import math

def set_bonus(stat):
    return math.floor((stat - 10) / 2)

def main():
    
    stat = int(input("Enter stat:"))
    print(set_bonus(stat))

main()
