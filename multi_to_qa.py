import json
import argparse

def construct(test_or_not, in_file, out_file):
    fin = open(in_file, 'r')
    f_context = open('context.json', 'r')
    data = json.load(fin)
    context = json.load(f_context)
    fin.close()
    data_out = []
    if test_or_not:
        for entry in data:
            temp = {}
            temp['id'] = entry['id']
            temp['context'] = context[entry['relevant']]
            temp['question'] = entry['question']
            temp['answers'] = {}
            temp['answers']['text'] = [""]
            temp['answers']['answer_start'] = [0]
            """
            temp['answers']['text'] = ""
            temp['answers']['answer_start'] = 0
            """
            data_out.append(temp)
    else:
        for entry in data:
            temp = {}
            temp['id'] = entry['id']
            temp['context'] = context[entry['relevant']]
            temp['question'] = entry['question']
            temp['answers'] = {}
            temp['answers']['text'] = [entry['answer']['text']]
            temp['answers']['answer_start'] = [int(entry['answer']['start'])]
            """
            temp['answers']['text'] = entry['answer']['text']
            temp['answers']['answer_start'] = entry['answer']['start']
            """
            data_out.append(temp)


    fout = open(out_file, 'w')
    json.dump(data_out, fout, indent=2, ensure_ascii=False)


parser = argparse.ArgumentParser(description="Transfer to qa json")
parser.add_argument(
    "--origin_name",
    type=str,
    default=None,
    help="Original file from Multiple Choice.",
)
parser.add_argument(
    "--output",
    type=str,
    default=None,
    help="Output file.",
)
parser.add_argument(
    "--test",
    default=False,
    action='store_true',
    help="If input testfile",
)
args = parser.parse_args()
construct(args.test, args.origin_name, args.output)
