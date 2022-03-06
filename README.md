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

# Comment
Quá trình xử lí của Chatterbot

- tiền xử lí
- sơ tuyển (chọn từ data những statement phù hợp để đưa vào model ở bước 2) (bước 1)
- similarity compare (model so sánh tương đồng, tìm ra statement tương đồng nhất) (bước 2)
- câu trả lời của statement tương đồng nhất là câu trả lời cần tìm

## NOTE: 
### Ở bước 1 (sơ tuyển):
#### chatterbot sử dụng các kĩ thuật cho tiếng anh: 
- tokenizer (whitespace)
- remove_stopwords 
- pos_tag
- hypernyms
- VD: `'What a beautiful swamp' => 'DT:beautiful JJ:wetland'`
=> Tìm kiếm tất cả những statement có: `DT:beautiful` hoặc `JJ:wetland`
#### chatterbot sử dụng các kĩ thuật cho tiếng Việt:
- tokenizer (whitespace)
- remove_stopwords
- stem_words (trả về kí tự đầu của từ đứng liền trước)
- VD: `'thừa cân béo phì là gì' => 't:cân c:béo b:phì'`
=> Tìm kiếm tất cả những statement có: `t:cân` hoặc `c:béo` hoặc `b:phì`
### Nhận xét
- do đặc điểm ngôn ngữ, quy trình sơ tuyển dành cho tiếng anh là hợp lí. (nltk có hỗ trợ)
- quy trình sơ tuyển cho tiếng Việt chưa sử dụng nhiều các thao tác xử lí ngôn ngữ tự nhiên dành cho tiếng Việt. Trong quá trình này, nhóm đã thử sử dụng các thao tác xử lí tiếng Việt của underthesea vào, nhưng chưa cho kết quả khả quan. Điều này hợp lí, là do:
    + do đặc trưng tiếng Việt: có tồn tại từ ghép, nghĩa của từ phụ thuộc nhiều vào ngữ cảnh. Các thao tác như (tokenizer, pos_tag) đã được hỗ trợ, nhưng chưa chính xác 100%
    + nltk chưa hỗ trợ hypernyms cho tiếng Việt
- Quy trình sơ tuyển hiện tại của chatterbot phụ phụ thuộc nhiều vào trật tự các từ xuất hiện trong câu


# error
- Lỗi time:
vào util/compat.py dòng 264 sửa time.clock thành time.time
- Lỗi Loader:
pip install pyyaml==5.4.1


total_score: 204 || len: 230 || score: 0.8869565217391304
time: 614.1756165027618