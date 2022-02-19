
# copy file search.py and comparisons.py into chatterbot
C:\Users\ASUS\AppData\Local\Programs\Python\Python39\Lib\site-packages\chatterbot
# trainer.py
you can train chatterbot here, see data trained in `database.sqlite3`
you can download extension SQLite to see data in `database.sqlite3` in visual studio code
select all data in file --SQLite.sql ===> Ctrl+SHIFT+Q to delete data in database

run `python trainer.py` to train

# app.py
run `python app.py` to run web server, connect API.

# test.py
run `python test.py` to test

# ERROR
you may don't have vietnamese stopword file.
you can download file `vietnamese-stopwords.txt` here: https://github.com/stopwords/vietnamese-stopwords
change name `vietnamese-stopwords.txt` into `vietnamese` (without `.txt`)
note that put it into the directory of warning.
C:\Users\ASUS\AppData\Roaming\nltk_data\corpora\stopwords


# Result

BERT 39/40
![image](https://user-images.githubusercontent.com/35862674/152638656-533e8db8-18f5-4313-b3ed-ab72c8dc2d72.png)

levenshtein_distance 38/40

![image](https://user-images.githubusercontent.com/35862674/152638863-68ac8bcc-dc53-4590-a956-507b3251281c.png)
