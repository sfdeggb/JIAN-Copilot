#Lunix
nohup python3 -u run_train.py --data_dir data/ --src_file egret_wenda_lines.json --model_type unilm --model_name_or_path unilm_model/ --output_dir kuakua_robot_model/ --max_seq_length 128 --max_position_embeddings 512 --do_train --do_lower_case --train_batch_size 32 --learning_rate 2e-5 --logging_steps 100 --num_train_epochs 10 > log.log 2>&1 &

#windows
python -u run_train.py --data_dir data/ 
--src_file egret_wenda_lines.json 
--model_type unilm 
--model_name_or_path unilm_model/ 
--output_dir kuakua_robot_model/ 
--max_seq_length 128 
--max_position_embeddings 512 
--do_train 
--do_lower_case 
--train_batch_size 32 
--learning_rate 2e-5 
--logging_steps 100 
--num_train_epochs 10 > log.log 2>&1 &
#-------------------------------------#
python -u run_train.py --data_dir data/ --src_file egret_wenda_lines.json --model_type unilm --model_name_or_path unilm_model/ --output_dir jiann_wenda_model/ --max_seq_length 128 --max_position_embeddings 512 --do_train --do_lower_case --train_batch_size 32 --learning_rate 2e-5 --logging_steps 100 --num_train_epochs 10 > log.log 2>&1 &
#--------------------------------------#
python -u decode_seq2seq.py 
--model_type unilm 
--model_name_or_path ./data/model/
--model_recover_path ./data/output_dir/model.3.bin 
--max_seq_length 512 
--input_file ./data/weibo/test_data.json 
--output_file ./data/weibo/predict.json 
--do_lower_case --batch_size 8 
--beam_size 5 --max_tgt_length 128
