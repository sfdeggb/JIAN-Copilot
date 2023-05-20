# Jian-N-Roboot

HPOEING YOU COMING!

## logo

![image](https://github.com/sfdeggb/JIAN-N-QA-ROBOOT/assets/95692531/f18eff4d-ef67-4015-a510-3a9add13679a)


## Introduction
This project is a imation of LIKE_CHAT_GPT.the base of the project is UNILM which is relased by Micosoft.As we all know, the large language model can be  fine tuning so that it can make greate performeance under the downstrom  of NLP work. Even if it is cant not put into the market from the current level, it is a great work to understand large language model how to work. we hope this project can be more people who has need find. at the same time, we also continue to improve the project and hope more and more people get involved this project. Looking forward you comming. Have a good day! 

## corpus
egrget_corpus is the main corpus that used. Also, there have many other excellent corpus. 

link:https://github.com/candlewill/Dialog_Corpus

## How to lanuch
**attention **
this project only have its source code. the data and model is so large that can not be upload. so you have two choice to deploy it. the first is download the origin corpus and then runing the relation code that be used to preprocessing, traing, and test. The sceond is to download the data and model preprocesing. the below is we talk about the second simple way to launch to project.
> 1. download the dealed data and trained model.the address is below.
> 2. put the "egert_wenda_lines.json" under the /data. and put the pytorch_model.bin, optim.json,config.json under the /jiann_wenda_model.
> 3. open the cmd under the path of project.
> 4. input this commend below.
```shell
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
```
> 5.After above operation is done. Finnally, you can use its with "intervatewithConsole.py"(current).
  
## preprocess data and model
data link:  链接：https://pan.baidu.com/s/1jbWhOa0ORPftW4C0GOvJAg <br>
            提取码：345f
model link: 链接：https://pan.baidu.com/s/1xjOwGPU60yPOCcasqs03hQ <br>
            提取码：345f

## requrients enviroment
pytorch
numpy 
transformers

## reference 
UNILM MODEL: https://www.jianshu.com/p/22e3cc4842e1
             https://zhuanlan.zhihu.com/p/378514578
           
            
# end enjoy!
