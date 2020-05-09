import requests
import json
import pymysql

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

"""
總覽 21

線上遊戲 400
手機 94
網頁 80
電腦 40
TV 掌機 52
動漫畫 22
閒聊 60
主題 61
場外 95
站務 28
"""

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='example', db='baha', charset='utf8')
cursor = conn.cursor()

sql = "SELECT kanban_id FROM kanban;"
cursor = conn.cursor()
cursor.execute(sql)
row = cursor.fetchall()

ids = set()
for i in row:
  ids.add(i[0])

classes = [400, 94, 80, 40, 52, 22, 60, 61, 95, 28]
for kanbanclass in classes:
    count = 1
    while count < 100:
        url = 'https://forum.gamer.com.tw/ajax/rank.php?c=' + str(kanbanclass)+ '&page=' + str(count)
        res = requests.get(url, headers=headers)
        js = json.loads(res.text)
        # print(js)

        value = []
        if js:
            for k in js:
                if k['bsn'] not in ids:
                    value.append('({}, "{}", {})'.format(k['bsn'], k['title'], kanbanclass))
                    ids.add(k['bsn'])
                    print("新看板 {}".format(k['title']))
        else:
            break

        if len(value) == 0:
            count += 1
            continue

        sql = 'INSERT INTO kanban (kanban_id, kanban_name, class_id) VALUES ' + ",".join(value) + ";"
        # print(sql)
        cursor.execute(sql)
        conn.commit()
        count += 1
    print("{} 完成".format(kanbanclass))

# 關閉遊標
cursor.close()
# 關閉連線
conn.close()
print("kanban.py 執行完成")
