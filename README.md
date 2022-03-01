# install packages
pip install -r requirements.txt
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
<!-- DEFAULT -->
levenshtein_distance
total_score: 176 || len: 200 || score: 0.88
time: 36.98527812957764

bert
total_score: 179 || len: 200 || score: 0.895
time: 388.76241278648376

<!-- WITHOUT HYPERNYMS -->

levenshtein_distance
total_score: 176 || len: 200 || score: 0.88
time: 29.82931661605835

bert
total_score: 182 || len: 200 || score: 0.91
time: 713.4014749526978

<!--  -->