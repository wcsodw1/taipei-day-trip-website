
# 台北一日遊資料表建立 : 
 
## 1.建立資料表 : Data來自(pongpong)json檔 :
use wehelp_travel; # 使用自己剛創建的website資料庫
CREATE TABLE Taipei_Attraction (  # 新增會員資料表
id INT NOT NULL AUTO_INCREMENT, # (!)用途說明 : 會員的獨立編號, 1.id :會員ID 2.AUTO_INCREMENT:自動累加
name varchar(255) NOT NULL,  # (!)用途說明 : 景點名稱 2.NOT NULL : 此欄不可為空值 3.varchar(255):資料型態
category varchar(255) NOT NULL,
description varchar(2000) NOT NULL,
address varchar(255) NOT NULL,
transport varchar(2000) NOT NULL, 
MRT varchar(255) NULL, 
latitude varchar(255) NOT NULL,
longitude varchar(255) NOT NULL, 
SERIAL_NO varchar(255) NOT NULL, 
image varchar(4000) NOT NULL,
PRIMARY KEY(id) #  (!)用途說明 PRIMARY KEY(id) : 藉由id的設定以便撈資料
);

# 2.如果需要刪除整個(member)資料表 : - 
-- DROP TABLE Taipei_Attraction;