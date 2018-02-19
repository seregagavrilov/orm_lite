import sqlite3


def connect_to_data_base(name):
    return sqlite3.connect(name)


def drop_table(tablename, connect):
    connect.execute('drop table if exists %(table)s' % {'table': tablename})
    currentconn.commit()

def updatr_data(table, **updatedata):

    columns = table.write_paramiters_to_update(updatedata)

    values = table.write_values(updatedata['where'])

    s = 'UPDATE %(table)s SET %(columns)s WHERE id =?' % {'table': table.tablename,
                                                           'columns': columns}

    table.currentcursor.execute(s, values)

    table.currentbase.commit()

    return table


class dbservice():
    def __init__(self, coonect):

        self.tablename = type(self).__name__
        self.currentbase = coonect
        self.currentcursor = self.currentbase.cursor()
        self.dict_fields = self.__class__.__dict__

    def insert_data(self, **args):

        columns = self.write_paramiters_to_insert(args)

        values = self.write_values(args)

        qparamiters = ('?,' * len(args))[:-1]

        s = 'INSERT INTO %(table)s %(columns)s values(' % {'table': self.tablename,
                                                           'columns': columns} + qparamiters + ')'
        self.currentcursor.execute(s, values)

        self.currentbase.commit()

        return self

    def write_values(self, args):

        v = []

        for k in args:
            v.append(args[k])
        return v

    def select_all(self):

        self.currentcursor.execute('SELECT * FROM %(table)s' % {'table': self.tablename})

        return self.currentcursor.fetchall()

    def create_table(self):

        columns = self.write_tuple_colums()

        self.currentcursor.execute('CREATE TABLE %(table)s %(columns)s' % {'table': self.tablename, 'columns': columns})

        self.currentbase.commit()

        return self

    def write_paramiters_to_update(self, arqs):
        # написать параметры where
        reqdata = arqs.get('where')

        if reqdata is None:
            raise ValueError("'WHERE paramiter was not found")

        parameters = []
        for key in arqs.keys():
            if key != 'where':
                parameters.append(str(key))
            else:
                parameters.append(str(reqdata[key]))

        strinofparamiters = '=?, '.join(parameters)

        return strinofparamiters +'=?'

    def write_paramiters_to_insert(self, arqs):

        parameters = []
        for key in arqs.keys():
            parameters.append(str(key))

        strinofparamiters = ', '.join(parameters)

        return '('+strinofparamiters+')'

    def write_tuple_colums(self):

        fieldnames = [k for k in self.dict_fields.keys() if not k.startswith('__')]
        typefields = [self.dict_fields[k] for k in fieldnames]

        stringparamiters = ''

        for i in range(len(fieldnames)):
            stringparamiters += fieldnames[i] + " " + typefields[i][0] + ','

        stringparamiters = stringparamiters[:-1]

        return '(' + stringparamiters + ')'


class MyFamaly(dbservice):
    __tablename__ = 'mytable'


    sourname = ('text', 'required')
    age = ('int', 'required')
    name = ('text', 'required')


currentconn = connect_to_data_base("Buiding")

cursor = currentconn.cursor()

if __name__ == "__main__":
    u = MyFamaly()
    u.create_table()
    drop_table("MyFamaly")
