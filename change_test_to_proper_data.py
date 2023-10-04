import json
fin = open('test.json')
data = json.load(fin)
fin.close()
data[1]['relevant'] = 0
print(data[1])
print(len(data))
for entry in data:
    entry['relevant'] = entry['paragraphs'][0]
    entry['answer'] = {}
    entry['answer']['text'] = '0'
    entry['answer']['start'] = 0

print(data[1])

fout = open('test2.json', 'w')
json.dump(data, fout, indent=2, ensure_ascii=False)

