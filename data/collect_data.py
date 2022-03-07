
# python collect_data.py

import json
import mysql.connector
from encodings import utf_8


def db_connection():
    mydb = None
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            database="wehelp_travel",
            password="root",
            charset="utf8"
        )
    except mysql.connector.Error as e:
        print(e)
    return mydb


mydb = db_connection()
mycursor = mydb.cursor()


# Load Data :
data = open('taipei-attractions.json', 'r', encoding='utf-8').read()
# print("data : ", data)
obj = json.loads(data)
# print(obj)

# (!)取json檔巢狀資料方法 :
information = obj["result"]["results"]
# print(information)

'''
Test 丟資料到 MySQL :

for i in information:
    data_1 = []
    id = i["_id"]
    name = i["stitle"]
    image = i["file"].split('https')
    image.pop(0)
    output = []

    # 圖片字串處理 :
    for j in image:
        total = 'https' + j
        # print(total)

        last = total.split('.')[-1].lower()
        # print(last)  # jpg
        if last == 'jpg' or last == 'JPG' or last == 'png' or last == 'PNG':
            https = "https"
            output.append(https + j)
            image_dic = {"images": output}
            # print(image_dic)
            # print("")
            images_json = json.dumps(image_dic)

    sql = """
        INSERT INTO taipei2 (id, name, image)
        VALUES (%s, %s, %s)
    """
    val = (id, name, images_json, )
    mycursor.execute(sql, val)
'''
for i in information:
    id = i["_id"]

    # 處理圖片字串 :
    image = i["file"].split('https')
    image.pop(0)

    # 其他項目 :
    transport = i["info"]
    name = i["stitle"]
    longitude = i["longitude"]
    mrt = i["MRT"]
    # print(mrt)
    serial_number = i["SERIAL_NO"]
    category = i["CAT2"]
    latitude = i["latitude"]
    description = i["xbody"]
    address = i["address"].replace(' ', '')  # 處理資料 : 刪除空白處

    output = []

    # 圖片字串處理 :
    for j in image:
        total = 'https' + j
        # print(total)

        last = total.split('.')[-1].lower()
        # print(last)  # jpg
        if last == 'jpg' or last == 'JPG' or last == 'png' or last == 'PNG':
            https = "https"
            output.append(https + j)
            image_dic = {"images": output}
            # print(image_dic)
            # print("")
            images_json = json.dumps(image_dic)

    sql = """
        INSERT INTO taipei_attraction (id, name, category, description, address, transport, mrt, latitude, longitude, SERIAL_NO, image)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    val = (id, name, category, description, address,
           transport, mrt, latitude, longitude, serial_number, images_json, )
    mycursor.execute(sql, val)
''''''
mydb.commit()
mydb.close()
