import sqlite3
import os.path
# location = 'data'
# table_name = "mytable"
#
# conn = sqlite3.connect(location)
# cursor = conn.cursor()
#
# sql = 'create table if not exists ' + table_name + ' (id integer)'
# cursor.execute(sql)
#
# sql = 'insert into ' + table_name + ' (id) values (%d)' % (1)
# cursor.execute(sql)
#
# conn.commit()

connect = sqlite3.connect("my_test_data.db")

c = connect.cursor()

c.execute('''CREATE TABLE stocks
            (date text, trans text, symbol text, qty real, price real)''')


c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

connect.commit()

symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

print(c.fetchone())

# class DbModel():
#
#     __tablename__ = "table1"
#
#     def __init__(self, nametable):





