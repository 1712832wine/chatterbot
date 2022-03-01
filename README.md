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
total_score: 173 || len: 200 || score: 0.865
time: 21.69052529335022

bert
total_score: 180 || len: 200 || score: 0.9
time: 329.67266035079956

<!-- VIETNAMESE CUSTOM 1 (POSTAG DEFAULT + VIETNAMESE TOKEN) -->

levenshtein_distance
total_score: 176 || len: 200 || score: 0.88
time: 20.617034435272217

bert
total_score: 181 || len: 200 || score: 0.905
time: 402.98384308815

# Comment
Quá trình xử lí của Chatterbot

- tiền xử lí
- sơ tuyển (chọn từ data những statement phù hợp để đưa vào model ở bước 2) (bước 1)
- similarity compare (model so sánh tương đồng, tìm ra statement tương đồng nhất) (bước 2)
- câu trả lời của statement tương đồng nhất là câu trả lời cần tìm

## NOTE: 
### Ở bước 1 (sơ tuyển):
chatterbot sử dụng các kĩ thuật cho tiếng anh: 
- tokenizer (whitespace)
- remove_stopwords 
- pos_tag
- hypernyms
chatterbot sử dụng các kĩ thuật cho tiếng Việt:
- tokenizer (whitespace)
- remove_stopwords
- stem_words (trả về kí tự đầu của từ đứng liền trước)
VD: 'thừa cân béo phì là gì' => 't:cân c:béo b:phì'   
### Nhận xét
- do đặc điểm ngôn ngữ, quy trình sơ tuyển dành cho tiếng anh là hợp lí. (nltk có hỗ trợ)
- quy trình sơ tuyển cho tiếng Việt chưa sử dụng nhiều các thao tác xử lí ngôn ngữ tự nhiên dành cho tiếng Việt. Trong quá trình này, nhóm đã thử sử dụng các thao tác xử lí tiếng Việt của underthesea vào, nhưng chưa cho kết quả khả quan. Điều này hợp lí, là do:
    + do đặc trưng tiếng Việt: có tồn tại từ ghép, việc tokenizer phụ thuộc nhiều vào ngữ cảnh. Các thư viện tokenizer hiện tại chưa tokenizer đúng 100% => nếu tokenizer sai, sẽ dẫn tới nhiều hệ lụy khác (pos_tag sai, remove stopword sai).
    + nltk chưa hỗ trợ hypernyms cho tiếng Việt
- Quy trình sơ tuyển hiện tại của chatterbot phụ phụ thuộc nhiều vào trật tự các từ xuất hiện trong câu