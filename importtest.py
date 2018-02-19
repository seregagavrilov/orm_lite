from testclass import dbservice
from testclass import connect_to_data_base
from testclass import drop_table
from testclass import updatr_data
class MyFamaly(dbservice):

    id = ("int", 'required')
    sourname = ('text', 'required')
    age = ('int', 'required')
    name = ('text', 'required')

connect = connect_to_data_base("mydata")

drop_table("MyFamaly",connect)

myfam = MyFamaly(connect)

# myfam.create_table()
# #
# myfam.insert_data(name="Vera", sourname="Gavrilov", age = 29, id=4)
#
updatr_data(myfam, name="Vera", sourname="Gavrilov", age = 80, where = {'id' :2})
#
# row = myfam.select_all()
#
# print(row)


