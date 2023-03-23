"""
@function:实现句子的分词
@author: ZhuJianhao
@date:2021-6-15
"""

# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

import logging

from transformers import BertTokenizer


logger = logging.getLogger(__name__)

VOCAB_FILES_NAMES = {'vocab_file': 'vocab.txt'}

PRETRAINED_VOCAB_FILES_MAP = {
    'vocab_file':
    {
        'unilm-large-cased': "",
        'unilm-base-cased': ""
    }
}

PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES = {
    'unilm-large-cased': 512, 
    'unilm-base-cased': 512
}


# 将文本按照空格进行分词
def whitespace_tokenize(text):
    """Runs basic whitespace cleaning and splitting on a piece of text."""
    text = text.strip()
    if not text:
        return []
    tokens = text.split()
    return tokens

class UnilmTokenizer(BertTokenizer):
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES


class WhitespaceTokenizer(object):
    """
    功能：用来按照空格进行分词的一个类
    
    """
    def tokenize(self, text):
        return whitespace_tokenize(text)
