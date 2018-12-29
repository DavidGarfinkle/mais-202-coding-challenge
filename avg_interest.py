import sys
import csv
import pandas as pd

def main():
    inpath = sys.argv[1]
    outpath = sys.argv[2]

    # Parse input
    df = pd.read_csv(inpath)

    # Calculate means
    agg = df.groupby(['purpose']).mean()['int_rate']

    # Generate figures
    fig = agg.plot(kind='bar', y="interest_rate", x="purpose").get_figure()

    # Save results to disk
    agg.to_csv("{}.csv".format(outpath))
    fig.savefig("{}.png".format(outpath))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <input_csv>".format(__file__))
    main()
