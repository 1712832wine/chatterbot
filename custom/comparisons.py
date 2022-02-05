"""
This module contains various text-comparison algorithms
designed to compare one statement to another.
"""
from sentence_transformers import SentenceTransformer, util
from chatterbot.comparisons import Comparator


class MyBert(Comparator):
    def __init__(self):
        self.bert = SentenceTransformer(
            'sentence-transformers/multi-qa-MiniLM-L6-cos-v1')
        #self.tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base", use_fast=True)

    def compare(self, statement_a, statement_b):
        # encode sentence 1
        encoded_1 = self.bert.encode(statement_a.text)

        # encode sentence 2
        encoded_2 = self.bert.encode(statement_b.text)

        # get similarity score
        score = util.dot_score(encoded_1, encoded_2)
        return round(float(score[0][0]), 4)
