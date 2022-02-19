import os
import pandas as pd
from trainer import chatbot
import re
import string
from underthesea import word_tokenize, sent_tokenize
from nltk.corpus import stopwords


def get_questions(text):
    questions = []
    pattern = re.compile(r'- -.*\n')
    matches = pattern.finditer(text)
    for match in matches:
        s = match.group(0)[4:]
        questions.append(s)
    return questions


def get_answers(text):
    answers = []
    pattern = re.compile(r'  - .*\n')
    matches = pattern.finditer(text)
    for match in matches:
        s = match.group(0)[4:]
        answers.append(s)
    return answers


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def preprocess(text):
    text = remove_punctuation(text.strip().lower().rstrip('\n'))
    return text


def compare(sent_1, sent_2):
    sent_1 = preprocess(sent_1)
    sent_2 = preprocess(sent_2)
    return sent_1 == sent_2


list_test = os.listdir('./data/test')
for file in list_test:
    # if file == 'test_viem_duong_ho_hap.yml':
    # read data test
    with open('./data/test/'+file, encoding="utf-8") as f:
        test = f.read()

    test_questions = get_questions(test)
    test_answers = get_answers(test)

    # predict one sentence
    # --------------------
    # predict = chatbot.get_response(test_questions[38])
    # print("predict", predict)

    # predict all sentences in test file
    # --------------------
    print(file)
    score = 0
    a = []
    p = []
    s = []
    print(len(test_questions), len(test_answers))
    for index in range(0, len(test_questions)):
        predict = chatbot.get_response(test_questions[index])
        if compare(predict.text, test_answers[index]):
            score += 1
        else:
            a.append(test_answers[index])
            p.append(predict)
            s.append(predict.confidence)
    d = {'answer': a, 'predict': p}
    df = pd.DataFrame(data=d)
    print(df)
    print("score:", score, "total:", len(test_questions))


# predict one sentence
# --------------------

# while True:
#     message = input("input: ")
#     if not message:
#         break
#     predict = chatbot.get_response(message)
#     print(predict)
