import random
from stat_rolling import fdsix_set, tdsix_set, standard_set



def main():
    current_set = fdsix_set()
    
    print(current_set[1][0])
    print(current_set[1][1:])
    
main()
