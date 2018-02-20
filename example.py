from sqliteorm import dbservice
from sqliteorm import connect_to_data_base
from sqliteorm import drop_table
from sqliteorm import update_data
from sqliteorm import insert_data
class MyFamaly(dbservice):

    id = ("int")
    sourname = ('text')
    age = ('int')
    name = ('text')

connect = connect_to_data_base("mydata")

drop_table("MyFamaly",connect)

myfam = MyFamaly(connect)

myfam.create_table()
insert_data(myfam, name="Vera", sourname="Gavrilov", age = 29, id=4)

print(myfam.select(['name','id']))
print(myfam.select_all())

update_data(myfam, name="Vera", sourname="Gavrilov", age = 80, id = 3, where = {'id':4})

row = myfam.select_all()

print(row)


