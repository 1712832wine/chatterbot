# install packages
pip install -r requirements.txt
# Setup
Trong thư mục custom:  
- Copy FILE `comparisons.py` và `search.py` vào thư viện chatterbot ở đường dẫn:  
`C:\Users\ASUS\AppData\Local\Programs\Python\Python39\Lib\site-packages\chatterbot`
- Copy FILE `best_match.py` vào thư viện chatterbot ở đường dẫn:  
`C:\Users\ASUS\AppData\Local\Programs\Python\Python39\Lib\site-packages\chatterbot\logic`
- Copy NỘI DUNG một trong 3 file `tagging vietnamese token+postag.py` hoặc `tagging vietnamese` hoặc `tagging whitespace+stemword.py` ghi đè vào nội dung file `tagging.py` trong thư viện chatterbot ở đường dẫn:  
`C:\Users\ASUS\AppData\Local\Programs\Python\Python39\Lib\site-packages\chatterbot`
- copy FILE `./stopwords/vietnamese` vào thư mục sau:  
`C:\Users\ASUS\AppData\Roaming\nltk_data\corpora\stopwords`
# Delete data trong database
Nếu bạn muốn train lại, trước hết phải xóa toàn bộ data trong `database.sqlite3`
download extension SQLite trong visual studio code, chọn toàn bộ nội dung trong file `--SQLite.sql` ===> Nhấn tổ hợp phím `Ctrl+SHIFT+Q` để xóa data trong database

# trainer.py
Bạn có thể train lại bằng câu lệnh `python trainer.py`. Xem data đã train trong `database.sqlite3`
# app.py
Để khởi động server, kết nối với giao diện, Hãy chạy lệnh `python app.py`

# test.py
Để test, hãy chạy lệnh `python test.py`

# Comment
Quá trình xử lí của Chatterbot

- tiền xử lí
- sơ tuyển (chọn từ data những statement phù hợp để đưa vào model ở bước 2) (bước 1)
- similarity compare (model so sánh tương đồng, tìm ra statement tương đồng nhất) (bước 2)
- câu trả lời của statement tương đồng nhất là câu trả lời cần tìm


# Data:
Dataset: test gồm 330 cặp câu (câu hỏi, câu trả lời đúng) thuộc các lĩnh vực y tế đã có trong data


# Kết quả
Lần lượt chạy bert, lavenstein với các thao tác sơ loại sau:
 
- STEMWORD + WHITESPACE

- VIETNAMESE TOKENIZER + STEMWORD
threshold lavenstein 0.75  
total_score: 270 || len: 380 || score: 0.71  
không biết: 86 => 0.23 (bỏ đi phần google)
sai 24 câu => 0.06  
time: 154.9934642314911  

threshold bert 0.8
total_score: 327 || len: 380 || score: 0.8605263157894737 
unknown: 23||time: 896.9174010753632
sai 30 câu

threshold 0.85
total_score: 300 || len: 380 || score: 0.7894736842105263 
unknown: 65||time: 896.623348236084
sai 15 câu
- VIETNAMESE TOKENIZER + POSTAG  



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
- quy trình sơ tuyển cho tiếng Việt chưa sử dụng nhiều các thao tác xử lí ngôn ngữ tự nhiên dành cho tiếng Việt. Trong quá trình này, nhóm đã thử sử dụng các thao tác xử lí tiếng Việt của underthesea vào, nhưng chưa cho kết quả khả quan. Điều này hợp lí, là do  + do đặc trưng tiếng Việt: có tồn tại từ ghép, nghĩa của từ phụ thuộc nhiều vào ngữ cảnh. Các thao tác như (tokenizer, pos_tag) đã được hỗ trợ, nhưng chưa chính xác 100%  + nltk chưa hỗ trợ hypernyms cho tiếng Việt
- Quy trình sơ tuyển hiện tại của chatterbot phụ phụ thuộc nhiều vào trật tự các từ xuất hiện trong câu


# Khắc phục một số lỗi
- Lỗi time:
vào util/compat.py dòng 264 sửa time.clock thành time.time
- Lỗi Loader:
đổi load() thành safe_load()




total_score: 299 || len: 330 || score: 0.906060606060606 
time: 2482.210257768631
unknown: 5
