from testclass import dbservice
from testclass import connect_to_data_base
from testclass import drop_table
class MyFamaly(dbservice):

    id = ("int", 'required')
    sourname = ('text', 'required')
    age = ('int', 'required')
    name = ('text', 'required')

connect = connect_to_data_base("mydata")

drop_table("MyFamaly",connect)

myfam = MyFamaly(connect)

myfam.create_table()
#
myfam.insert_data(name="Vera", sourname="Gavrilov", age = 29, id=4)

myfam.updatr_data(name="Vera", sourname="Gavrilov", age = 80, id = 4)

row = myfam.select_all()

print(row)


