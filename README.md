# Step 1: Copy file search.py into chatterbot
C:\Users\ASUS\AppData\Local\Programs\Python\Python39\Lib\site-packages\chatterbot

# Train (JUST RUN ONE TIME.)
## This can make database become too large if run many times.
run `python chatbot.py` to train chatterbot
you can see data in database.sqlite3


# Run
run `python app.py`

# ERROR
you may don't have vietnamese stopword file.
you can download file `vietnamese-stopwords.txt` here: https://github.com/stopwords/vietnamese-stopwords
change name `vietnamese-stopwords.txt` into `vietnamese` (without `.txt`)
note that put it into the directory of warning.
