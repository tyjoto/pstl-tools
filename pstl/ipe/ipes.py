import argparse as arg

import loop as lp

parser = arg.ArgumentParser()
parser.add_argument("-f","--filename",
                    help="Path to date file to use",
                    type=str)
parser.add_argument("-s","--savename",
                    help="Save plot and new csv with this name",
                    type=str),
parser.add_argument("-r","--skiprows",
                    help="Skip # of rows",
                    type=int)
parser.add_argument("-d","--delimiter",
                    help="Deliminator for csv file (default is ',')",
                    type=str)
args = parser.parse_args()

# define variables based on passed in arguments
fname = args.filename
sname = args.savename

if args.delimiter is not None:
    delimiter = args.delimiter
else:
    delimiter = ","
if args.skiprows is not None:
    skiprows = args.skiprows
else:
    skiprows = 0

def readCSV(fname,delimiter,skiprows):
    with open(fname) as f:
        data = np.loadtxt(f,delimiter=delimiter,skiprows=skiprows)
    return data


def main():
    print("Thanks for using IPES\n")
    lp.loop(fname,sname,delimiter,skiprows)

if __name__ == "__main__":
    main()
