from myrGendb import *
import sys
#
# SCC0561 - MIR implementation
# author: Henrique F. M. Freitas
#

from gym import gymTest

def main():
    generateDict()

    if len(sys.argv) < 2:
        print("insuficient nargs\n")
        print("usage: python3 myr.py <analysis>  || checkImg [tgtImg]")
        sys.exit()

    # defining which operation you're executing
    if sys.argv[1] == "checkImage":
        # couldn't implement it properly
        myrCheckImage(sys.argv[2])
    else:
        if sys.argv[1] == "analysis":
            myr_classify()
        else:
            print("option not found")

main()
