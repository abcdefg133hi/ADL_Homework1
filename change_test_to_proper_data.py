import json
import argparse

def change_to_proper_data(input_file, output_file):
    fin = open(input_file)
    data = json.load(fin)
    fin.close()
    for entry in data:
        entry['relevant'] = entry['paragraphs'][0]
        entry['answer'] = {}
        entry['answer']['text'] = '0'
        entry['answer']['start'] = 0


    fout = open(output_file, 'w')
    json.dump(data, fout, indent=2, ensure_ascii=False)

parser = argparse.ArgumentParser(description="Transfer data to proper data form")
parser.add_argument(
    "--input",
    type=str,
    default=None,
    help="Input data files.",
)
parser.add_argument(
    "--output",
    type=str,
    default=None,
    help="Output file.",
)
args = parser.parse_args()
change_to_proper_data(args.input, args.output)

