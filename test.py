import random
from stat_rolling import *
import math

score = 12
base_barb_sub: list[str] = ["berserker", "wild heart", "world tree", "zealot"]
eberron_arti_sub: list[str] = ["alchemist", "armorer", "artillerist", "battle smith", "cartographer"]
base_wiza_sub: list[str] = ["abjurer", "diviner", "evoker", "illusionist"]

nested_list = [base_barb_sub, eberron_arti_sub, base_wiza_sub]

flat_list = [string for sublist in nested_list for string in sublist]

def main():
    print(nested_list)
    print(flat_list)
    
main()
