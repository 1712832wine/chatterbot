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

levenshtein_distance (stopword min):(training using pos_tag)
total_score: 175 || len: 200 || score: 0.875
time: 23.84418511390686

bert (stopword min):(training using pos_tag)
total_score: 181 || len: 200 || score: 0.905
time: 359.512713432312
