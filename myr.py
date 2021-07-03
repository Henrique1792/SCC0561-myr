from myrAnalyse import *
from  myrGendb  import *

#
# SCC0561 - MIR implementation
# author: Henrique F. M. Freitas
#


def main():

    if len(sys.argv) < 2:
        print("insuficient nargs\n")
        print("usage: python3 myr.py <genDict||analysis> [tgtImg]")
        sys.exit()

    # defining which operation you're executing
    if sys.argv[1] == "genDict":
        print("Generate dictionary using 10 files - outputing into db.txt")
        generateDict()

    else:
        if sys.argv[1] == "analysis":
            analyzeImg(sys.argv[2])
        else:
            if sys.argv[1] == "dbAnalyse":
                print("2")
            else:
                print("option not found")

main()
