# ADL Homework

## Installation
Install the package for running ADL Homework1 😙😙.<br>
(Including models, plots ......)
```
./download.sh
```
which is equal to
```
git clone https://github.com/abcdefg133hi/ADL_Homework.git
```

## Run && Get Results
The shell script for running the optimized results
```
mkdir results
./run.sh context.json test.json results
```

## Plot the learning curve
```
cd plot
python3 plotLearningCurve.py
```
Notice that data for the plot are stored in "results.json". One needs to record the values
 from the running script and store to "results.json". 😅😅

## To-do List
- Calculate the performance of bert-base-chinese for span-selection.
- Calculate the performance of different model on multi-selection.
- Do the non-pretrained performance.

## Have a nice journey ~~ ^-^
