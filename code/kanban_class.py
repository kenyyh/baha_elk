import requests
import json
import pymysql

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='example', db='baha', charset='utf8')
cursor = conn.cursor()

classes = {400:"線上遊戲", 94:"手機", 80:"網頁", 40:"電腦", 52:"TV掌機", 22:"動漫畫", 60:"閒聊", 61:"主題", 95:"場外", 28:"站務"}

for kanbanclass in classes.keys():
  # session.add(kanban(class_id = class_, class_name = classes[class_]))
    sql = 'INSERT INTO kanban_class (class_id, class_name) VALUE ({}, "{}")'.format(kanbanclass, classes[kanbanclass])
    cursor.execute(sql)
    conn.commit()


# 關閉遊標
cursor.close()
# 關閉連線
conn.close()
print("kanban_class.py 執行完成")
