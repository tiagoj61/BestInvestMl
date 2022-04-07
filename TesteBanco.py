import psycopg2
con = psycopg2.connect(host='localhost', database='teste',
user='postgres', password='postgres')
cur = con.cursor()
print(cur)
sql = 'create table IF NOT EXISTSq a (id serial primary key, aa varchar(2))'
cur.execute(sql)
con.commit()
sql = "insert into a values (default,'SP')"
cur.execute(sql)

cur.execute('select * from a')
recset = cur.fetchall()
for rec in recset:
    print(rec)
con.close()