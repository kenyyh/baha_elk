import requests
import json
import pymysql
import datetime

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='example', db='baha', charset='utf8')
cursor = conn.cursor()

for count in range(1, 67):
    url = 'https://forum.gamer.com.tw/ajax/rank.php?c=21&page=' + str(count)
    res = requests.get(url, headers=headers)
    js = json.loads(res.text)

    value = []
    for k in js:
        value.append('("{}", "{}", {}, {}, {})'.format(str(yesterday), k['bsn'], k['ranking'], k['hot'],  k['article']))

    sql = 'INSERT INTO ranking (rank_day, kanban_id, ranking, hot, article) VALUES ' + ",".join(value) + ";"
    cursor.execute(sql)
    conn.commit()
    count += 1

# 關閉遊標
cursor.close()
# 關閉連線
conn.close()
print("ranking.py 執行完成")
