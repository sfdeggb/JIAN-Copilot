"""
@function: 实现机器人简单的交互
@author: zhuJianhao
@contact: zjmac1635@163.com
@time: 2020/8/4 11:25
"""
from dirty_recognize import dirty_reg
from tokenization_unilm import UnilmTokenizer
from modeling_unilm import UnilmForSeq2SeqDecodeSample, UnilmConfig
import torch
import torch.nn.functional as F
import copy
import os
import argparse
import re
import chat_ui

def remove_dirty_sentence(dirty_obj, sentence):
    if len(dirty_obj.match(sentence)) == 0:
        return False
    else:
        return True


def remove_multi_symbol(text):
    r = re.compile(r'([.,，/\\#!！？?。$%^&*;；:：{}=_`´︵~（）()-])[.,，/\\#!！？?。$%^&*;；:：{}=_`´︵~（）()-]+')
    text = r.sub(r'\1', text)
    return text


def top_k_top_p_filtering(logits, top_k=0, top_p=0.0, filter_value=-float('Inf')):
    assert logits.dim() == 1
    top_k = min(top_k, logits.size(-1))
    if top_k > 0:
        indices_to_remove = logits < torch.topk(logits, top_k)[0][..., -1, None]
        logits[indices_to_remove] = filter_value
    if top_p > 0.0:
        sorted_logits, sorted_indices = torch.sort(logits, descending=True)
        cumulative_probs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)
        sorted_indices_to_remove = cumulative_probs > top_p
        sorted_indices_to_remove[..., 1:] = sorted_indices_to_remove[..., :-1].clone()
        sorted_indices_to_remove[..., 0] = 0
        indices_to_remove = sorted_indices[sorted_indices_to_remove]
        logits[indices_to_remove] = filter_value
    return logits


def main(input_text3):
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', default='0', type=str, help='生成设备')
    parser.add_argument('--topk', default=3, type=int, help='取前k个词')
    parser.add_argument('--topp', default=0.95, type=float, help='取超过p的词')
    parser.add_argument('--dirty_path', default='D:/python/NLP-PY/UnilmChatchitRobot/data/dirty_words.txt', type=str, help='敏感词库')
    # parser.add_argument('--model_name_or_path', default='kuakua_robot_model/', type=str, help='模型路径')
    parser.add_argument('--model_name_or_path', default='D:/python/NLP-PY/UnilmChatchitRobot/jiann_wenda_model/', type=str, help='模型路径')
    parser.add_argument('--repetition_penalty', default=1.2, type=float, help="重复词的惩罚项")
    parser.add_argument('--max_len', type=int, default=32, help='生成的对话的最大长度')
    parser.add_argument('--no_cuda', type=bool, default=False, help='是否使用GPU进行预测')

    args = parser.parse_args()
    args.cuda = torch.cuda.is_available() and not args.no_cuda
    device = 'cuda' if args.cuda else 'cpu'
    
    #这里有个输出
    # print('using device:{}'.format(device))
    text1=chat_ui.get_context('using device:{}'.format(device))
    
    os.environ['CUDA_DEVICE_ORDER'] = 'PCI_BUS_ID'
    os.environ["CUDA_VISIBLE_DEVICES"] = args.device
    #进行模型的加载
    config = UnilmConfig.from_pretrained(args.model_name_or_path, max_position_embeddings=512)
    tokenizer = UnilmTokenizer.from_pretrained(args.model_name_or_path, do_lower_case=False)
    model = UnilmForSeq2SeqDecodeSample.from_pretrained(args.model_name_or_path, config=config)
    model.to(device)
    model.eval()
    #输出2
    # print('Chitchat Robot Starting')
    text2=chat_ui.get_context("Chitchat Robot Starting")
    
    dirty_obj = dirty_reg(args.dirty_path)
    while True:
        try:
            text = input("user:")#输入1
            if remove_dirty_sentence(dirty_obj, text):
                # print("chatbot:" + "换个话题聊聊吧。")
                answer_text4=chat_ui.get_context("chatbot:" + "换个话题聊聊吧。")
                continue
            input_ids = tokenizer.encode(text)
            token_type_ids = [4] * len(input_ids)
            generated = []
            for _ in range(args.max_len):
                curr_input_ids = copy.deepcopy(input_ids)
                curr_input_ids.append(tokenizer.mask_token_id)
                curr_input_tensor = torch.tensor(curr_input_ids).long().to(device).view([1, -1])
                curr_token_type_ids = copy.deepcopy(token_type_ids)
                curr_token_type_ids.extend([5])
                curr_token_type_ids = torch.tensor(curr_token_type_ids).long().to(device).view([1, -1])
                outputs = model(input_ids=curr_input_tensor, token_type_ids=curr_token_type_ids, attention_mask=None)
                next_token_logits = outputs[-1, -1, :]
                for id in set(generated):
                    next_token_logits[id] /= args.repetition_penalty
                next_token_logits[tokenizer.convert_tokens_to_ids('[UNK]')] = -float('Inf')
                filtered_logits = top_k_top_p_filtering(next_token_logits, top_k=args.topk, top_p=args.topp)
                next_token = torch.multinomial(F.softmax(filtered_logits, dim=-1), num_samples=1)
                if next_token == tokenizer.sep_token_id:  # 遇到[SEP]则表明生成结束
                    break
                generated.append(next_token.item())
                input_ids.append(next_token.item())
                token_type_ids.extend([5])
            text = tokenizer.convert_ids_to_tokens(generated)
            text = remove_multi_symbol("".join(text))
            if remove_dirty_sentence(dirty_obj, text):
                # print("chatbot:" + "我要想一想。")#输出3
                answer_text4=chat_ui.get_context("chatbot:" + "换个话题聊聊吧。")
            else:
                # print("chatbot:" + text)#输出4
                answer_text4=chat_ui.get_context("chatbot:" + "换个话题聊聊吧。")
        except:
            # print("chatbot:" + "说点别的吧，好吗？")#输出5
            answer_text4=chat_ui.get_context("chatbot:" + "换个话题聊聊吧。")
    return text1, text2, answer_text4


if __name__ == "__main__":
    input_text3=chat_ui.getinput()
    text1, text2, answer_text4=main(input_text3)
    chat_ui.gui(text1, text2, answer_text4)




