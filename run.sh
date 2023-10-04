git clone https://github.com/abcdefg133hi/ADL_Homework.git
cd ADL_Homework
echo ">>> Start to predict the multi-selections problem"
mkdir selection_result
mkdir qa_result
python change_test_to_proper_data.py --input ${2}
python hw1_selection.py --predict --train_file 'train.json' --validation_file 'test_today_is_a_good_day.json' --model_name_or_path './multi_selection_model' --max_seq_length 512 --per_device_train_batch_size 1 --gradient_accumulation_steps 2  --num_train_epochs 0 --learning_rate 3e-5  --output_dir './selection_result' --context_name ${1}

echo ">>> Finish predicting the multi-selections problem. The test output will be stored in the \'output.json\'"
python multi_to_qa.py --origin_name train.json --output train_pre.json
python multi_to_qa.py --origin_name valid.json --output valid_pre.json
python multi_to_qa.py --origin_name ./selection_result/output.json --output test_pre.json

echo ">>> Start to predict the QA problems"
python hw1_qa.py --model_name_or_path './qa_selection_model' --train_file "train_pre.json" --max_seq_length 512  --validation_file "test_pre.json"  --learning_rate 3e-5 --num_train_epochs 0 --per_device_train_batch_size 1 --gradient_accumulation_steps 2 --output_dir './qa_result' --test_file "valid_pre.json"
python result_to_csv.py --input './qa_result/eval_predictions.json' --output ${3}



