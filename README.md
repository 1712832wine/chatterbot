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
Dataset: test gồm 380 cặp câu (câu hỏi, câu trả lời đúng), trong đó:  
- 50 cặp không thuộc lĩnh vực y tế (Câu trả lời đúng là "Xin lỗi tôi không hiểu")
- 330 cặp thuộc các lĩnh vực y tế đã có trong data


# Kết quả
Lần lượt chạy bert, lavenstein với các thao tác sơ loại sau:
 
- STEMWORD + WHITESPACE

- VIETNAMESE TOKENIZER + STEMWORD
0.8
total_score: 185 || len: 330 || score: 0.5606060606060606 
using_google: 136 ||time: 170.20093774795532
sai 9

0.75
total_score: 221 || len: 330 || score: 0.6696969696969697 
using_google: 86 ||time: 119.4660587310791
sai 23 câu

0.7
total_score: 238 || len: 330 || score: 0.7212121212121212 
using_google: 61 ||time: 98.01828622817993
sai 31 câu

0.65
total_score: 253 || len: 330 || score: 0.7666666666666667 
using_google: 32 ||time: 76.97225880622864
sai 45 câu

none
total_score: 269 || len: 330 || score: 0.8151515151515152 
using_google: 0 ||time: 43.35360789299011
sai 61 câu

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

