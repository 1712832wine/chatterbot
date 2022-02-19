# Setup
- copy all file and folder in the directory ./custom into chatterbot at directory
`C:\Users\ASUS\AppData\Local\Programs\Python\Python39\Lib\site-packages\chatterbot`
- copy file ./stopwords/vietnamese into 
`C:\Users\ASUS\AppData\Roaming\nltk_data\corpora\stopwords`
# Delete data in database
you can download extension SQLite to see data in `database.sqlite3` in visual studio code
select all data in file --SQLite.sql ===> Ctrl+SHIFT+Q to delete data in database

# trainer.py
you can train chatterbot here, see data trained in `database.sqlite3`
run `python trainer.py` to train

# app.py
run `python app.py` to run web server, connect API.

# test.py
run `python test.py` to test

# Result

BERT 39/40
![image](https://user-images.githubusercontent.com/35862674/152638656-533e8db8-18f5-4313-b3ed-ab72c8dc2d72.png)

levenshtein_distance 38/40

![image](https://user-images.githubusercontent.com/35862674/152638863-68ac8bcc-dc53-4590-a956-507b3251281c.png)

laven cũ
total_score: 172 || len: 200 || score: 0.86
time: 70.72047543525696
bert cũ
total_score: 172 || len: 200 || score: 0.86
time: 1445.5244662761688

laven mới
total_score: 173 || len: 200 || score: 0.865
time: 30.971308946609497
bert mới

