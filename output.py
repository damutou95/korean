import pymysql
host = '127.0.0.1'
user = 'root'
passwd = '18351962092'
dbname = 'korean'
tablename = 'fanyi'
proxies = []
db = pymysql.connect(host, user, passwd, dbname)
cursor = db.cursor()
sql = f"select * from {tablename}"
cursor.execute(sql)
results = cursor.fetchall()
cursor.close()
with open('/home/xiyujing/文档/韩中词典三语对照2019年2月13日.txt', 'a') as f:
    for row in results:
        en = row[0]
        cn = row[1]
        kr = row[2]
        f.write(en + '\n' + cn + '\n' + kr + '\n')
