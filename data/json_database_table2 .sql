
# 台北一日遊資料表建立 : 
 
## 1.建立資料表 : Data來自(pongpong)json檔 :
use wehelp_travel;
CREATE TABLE Taipei2 (  
id INT NOT NULL AUTO_INCREMENT, 
PRIMARY KEY(id), 
name varchar(255) NOT NULL, 
image varchar(4000) NOT NULL,

);



# 2.如果需要刪除整個(member)資料表 : - 
-- DROP TABLE Taipei;