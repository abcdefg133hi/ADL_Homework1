import json
import pandas as pd
import argparse


def file_transform(input_file, output_file):
    fin = open('eval_predictions-17.json')
    data = json.load(fin)
    fin.close()
    li = []
    for entry in data:
        temp = []
        temp.append(entry)
        temp.append(data[entry])
        li.append(temp)

    df = pd.DataFrame(li, columns=['id', 'answer'])
    df.to_csv(output_file, index=False)


parser = argparse.ArgumentParser(description="Transfer result to csv")
parser.add_argument(
    "--input",
    type=str,
    default=None,
    help="Input result files.",
)
parser.add_argument(
    "--output",
    type=str,
    default=None,
    help="Output file.",
)
args = parser.parse_args()
file_transform(args.input, args.output)

