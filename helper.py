
from nltk.corpus import stopwords
from underthesea import word_tokenize
import re
import string


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


def remove_stopwords(text):
    stop_words = set(stopwords.words('vietnamese'))
    word_tokens = word_tokenize(text, format='text').split(' ')
    filtered_text = [word for word in word_tokens if word not in stop_words]
    if filtered_text:
        return filtered_text
    else:
        return word_tokens


def preprocess(text):
    text = remove_punctuation(
        text.strip().lower().rstrip('\n').replace(" ", ""))
    return text


def compare(sent_1, sent_2):
    sent_1 = preprocess(sent_1)
    sent_2 = preprocess(sent_2)
    return sent_1 == sent_2
