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
        print("usage: python3 myr.py <analysis> [tgtImg]")
        sys.exit()

    # defining which operation you're executing
    if sys.argv[1] == "checkImage":
        print("aho")
    else:
        if sys.argv[1] == "analysis":
            if sys.argv[2] == "dbAnalyse":
                myr_classify()
            else:
                print("option not found")

main()
