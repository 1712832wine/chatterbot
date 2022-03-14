import requests
import json
import os
from trainer import chatbot
from helper import get_questions, get_answers, compare
import time
from google_search import googleSearch


def get_response(message):
    data = json.dumps({"sender": "Rasa", "message": message})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    res = requests.post(
        'http://localhost:5005/webhooks/rest/webhook', data=data, headers=headers)
    res = res.json()
    val = res[0]['text']
    return val


list = ['test_quaibi_taimuihong_thuydau_viemxoang.yml',
        'test_other.yml', 'test_than_dalieu_daumatdo_muntrungca.yml']
for file in list:
    with open('./data/test/'+file, encoding="utf-8") as f:
        test = f.read()

    # read questions and answers from test file
    test_questions = get_questions(test)
    test_answers = get_answers(test)
    if (len(test_questions) == len(test_answers)):
        print("ok")
        for index in range(0, len(test_questions)):
            print(index + 1, '/', len(test_questions), 'of', file)
            predict_text = get_response(test_questions[index])
    # with open('./results/test-result-rasa.txt', "w", encoding='utf-8') as fw:
    #     time_start = time.time()
    #     # start testing
    #     total_score = 0
    #     total_len = 0
    #     list_test = os.listdir('./data/test')
    #     for file in list_test:
    #         with open('./data/test/'+file, encoding="utf-8") as f:
    #             test = f.read()

    #         # read questions and answers from test file
    #         test_questions = get_questions(test)
    #         test_answers = get_answers(test)
    #         # write len of test_questions and len of test answers
    #         print("start testing", file)
    #         fw.write('==================================\n')
    #         fw.write('file_name: {}\n'.format(file))
    #         fw.write('size: {}/{}\n'.format(len(test_questions), len(test_answers)))

    #         # check len of test_questions and len of test answers is equal
    #         if (len(test_questions) != len(test_answers)):
    #             fw.write(
    #                 'FILE {} HAS NUMBER OF QUESTIONS DIFFERENT TO NUMBER OF ANSWERS\n'.format(file))
    #             continue
    #         total_len += len(test_questions)
    #         score = 0

    #         for index in range(0, len(test_questions)):
    #             print(index + 1, '/', len(test_questions), 'of', file)
    #             predict_text = get_response(test_questions[index])

    #             if compare(predict_text, test_answers[index]):
    #                 score += 1
    #             else:
    #                 # WRONG CASES
    #                 fw.write('{}---------------------\n'.format(type))
    #                 fw.write('TEST QUESTION: {}\n'.format(
    #                     test_questions[index]))
    #                 fw.write('GOLD QUESTION: {}\n'.format(
    #                     test_answers[index]))
    #                 fw.write('PREDICT QUESTION: {}\n'.format(
    #                     predict_text))
    #                 fw.write('-------------------------\n')

    #         total_score += score
    #         # end of test file
    #         fw.write('score: {} || total: {}\n'.format(
    #             score, len(test_questions)))
    #         fw.write('==================================\n')
    #         print('finished', file)
    #     # finish all
    #     time_end = time.time()
    #     total_time = time_end - time_start
    #     fw.write('total_score: {} || len: {} || score: {} \ntime: {}\n'.format(
    #         total_score, total_len, total_score/total_len, total_time))
