import json
import pandas as pd
fin = open('eval_predictions-5.json')
data = json.load(fin)
fin.close()
li = []
for entry in data:
    temp = []
    temp.append(entry)
    temp.append(data[entry])
    li.append(temp)

df = pd.DataFrame(li, columns=['id', 'answer'])
df.to_csv('first_trial_with_1_and_4_1024.csv', index=False)
