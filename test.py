import os
from trainer import chatbot
import re
import string
import time


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
    text = remove_punctuation(
        text.strip().lower().rstrip('\n').replace(" ", ""))
    return text


def compare(sent_1, sent_2):
    sent_1 = preprocess(sent_1)
    sent_2 = preprocess(sent_2)
    return sent_1 == sent_2


if __name__ == "__main__":
    # open test-result to write
    with open('test-result.txt', "w", encoding='utf-8') as fw:
        time_start = time.time()
        # start testing
        total_score = 0
        total_len = 0
        list_test = os.listdir('./data/test')
        for file in list_test:
            with open('./data/test/'+file, encoding="utf-8") as f:
                test = f.read()

            # read questions and answers from test file
            test_questions = get_questions(test)
            test_answers = get_answers(test)

            # write len of test_questions and len of test answers
            print("start testing", file)
            fw.write('==================================\n')
            fw.write('file_name: {}\n'.format(file))
            fw.write('size: {}/{}\n'.format(len(test_questions), len(test_answers)))

            # check len of test_questions and len of test answers is equal
            if (len(test_questions) != len(test_answers)):
                fw.write(
                    'FILE {} HAS NUMBER OF QUESTIONS DIFFERENT TO NUMBER OF ANSWERS\n'.format(file))
                continue
            total_len += len(test_questions)
            score = 0

            for index in range(0, len(test_questions)):
                print(index + 1, '/', len(test_questions), 'of', file)
                predict = chatbot.get_response(test_questions[index])
                if compare(predict.text, test_answers[index]):
                    score += 1
                else:
                    # WRONG CASES
                    fw.write('--------------------------------\n')

                    fw.write('TEST QUESTION: {}\n'.format(
                        test_questions[index]))
                    fw.write('GOLD ANSWER: {}\n'.format(
                        test_answers[index]))
                    fw.write('PREDICT ANSWER: {}\n'.format(
                        predict.text))
                    fw.write('CONFIDENCE: {}\n'.format(
                        predict.confidence))

                    fw.write('--------------------------------\n')

            total_score += score
            # end of test file
            fw.write('score: {} || total: {}\n'.format(
                score, len(test_questions)))
            fw.write('==================================\n')
            print('finished', file)
        # finish all
        fw.write('total_score: {} || len: {} || score: {}\n'.format(
            total_score, total_len, total_score/total_len))

        time_end = time.time()
        total_time = time_end - time_start
        fw.write('time: {}\n'.format(total_time))
