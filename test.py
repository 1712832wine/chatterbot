import pandas as pd
from trainer import chatbot
import re


def get_questions(text):
    questions = []
    pattern = re.compile(r'- -.*\?')
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


# read data test
with open('./data/test_data.yml', encoding="utf-8") as f:
    test = f.read()

test_questions = get_questions(test)
test_answers = get_answers(test)


# predict one sentence
# --------------------
predict = chatbot.get_response(test_questions[38])
print("predict", predict)


# predict all sentences in test file
# --------------------
# score = 0
# a = []
# p = []

# for index in range(0, len(test_questions)):
#     predict = chatbot.get_response(test_questions[index])
#     if (predict.text[:50] == test_answers[index][:50]):
#         score += 1
#     else:
#         a.append(test_answers[index])
#         p.append(predict)

# d = {'answer': a, 'predict': p}
# df = pd.DataFrame(data=d)
# print(df)
# print("score:", score, "total:", len(test_questions))
