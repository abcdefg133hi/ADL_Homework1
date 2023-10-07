import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

fin = open('results.json', 'r')
data = json.load(fin)
fin.close()

train_loss_values = data['train_loss']['values']
train_loss_iterations = data['train_loss']['iterations']

train_EM_values = data['train_EM']['values']
train_EM_iterations = data['train_EM']['iterations']

val_EM_values = data['val_EM']['values']
val_EM_iterations = data['val_EM']['iterations']


plt.plot(train_loss_iterations, train_loss_values, label='train_loss', marker='o')
plt.xlabel('iterations')
plt.ylabel('loss')
plt.title('Learning Curve: Loss')
plt.legend()
plt.savefig('Learning_Curve_Loss.png')
plt.clf()
print("Successfully plot the learning curve with loss to Learning_Curve_Loss.png")
#plt.show()

plt.plot(train_EM_iterations, train_EM_values, label='train_EM', marker='o')
plt.plot(val_EM_iterations, val_EM_values, label='val_EM', marker='o')
plt.xlabel('iterations')
plt.ylabel('Exact Match')
plt.title('Learning Curve: Exact Match')
plt.legend()
plt.savefig('Learning_Curve_EM.png')
print("Successfully plot the learning curve with EM to Learning_Curve_EM.png")
plt.clf()
#plt.show()
