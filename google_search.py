import requests
from bs4 import BeautifulSoup
import re

GOOGLE_URL = "https://www.google.com.vn"


def googleSearch(question):
    try:
        url = GOOGLE_URL + '/search?q=' + question
        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')
        # answer = soup.find("div", class_="kCrYT")
        answer = soup.find("div", class_="BNeawe s3v9rd AP7Wnd")
        if answer == None:
            raise Exception

        link = answer.find("a")
        answer = str(answer)
        answer = re.sub(r'<(li|sub)( class="[\w\d\s]+")?>', '\n', answer)
        answer = re.sub(r'<a( href="\/url\?q=[^\s\"]+")?>', '\n', answer)
        answer = re.sub(r'<.*?>', '', answer)

        if link != None:
            link = GOOGLE_URL + link['href']
            answer += '\nlink: ' + link

        return answer
    except:
        return "Xin lỗi không hiểu yêu cầu"


print(googleSearch("tôi bị mệt mỏi"))
