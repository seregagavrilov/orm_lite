import sqlite3


def connect_to_data_base(name):
    return sqlite3.connect(name)


def drop_table(tablename, connect):
    connect.execute('drop table if exists %(table)s' % {'table': tablename})
    currentconn.commit()


class dbservice():
    def __init__(self, coonect):

        self.tablename = type(self).__name__
        self.currentbase = coonect
        self.currentcursor = self.currentbase.cursor()

    def insert_data(self, **args):

        columns = self.write_paramiters_to_insert(args)

        values = self.write_values_to_insert(args)

        qparamiters = ('?,' * len(args))[:-1]

        s = 'INSERT INTO %(table)s %(columns)s values(' % {'table': self.tablename,
                                                           'columns': columns} + qparamiters + ')'
        self.currentcursor.execute(s, values)

        self.currentbase.commit()

        return self

    def updatr_data(self, **args):

        columns = self.write_paramiters_to_update(args)

        values = self.write_values_to_insert(args)

        s = 'UPDATE %(table)s SET %(columns)s WHERE id =?' % {'table': self.tablename,
                                                           'columns': columns}

        self.currentcursor.execute(s, values)

        self.currentbase.commit()

        return self

    def write_values_to_insert(self, args):

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

        parameters = []
        for key in arqs.keys():
            if key != 'id':
                parameters.append(str(key))

        strinofparamiters = '=?, '.join(parameters)

        return strinofparamiters +'=?'

    def write_paramiters_to_insert(self, arqs):

        parameters = []
        for key in arqs.keys():
            parameters.append(str(key))

        strinofparamiters = ', '.join(parameters)

        return '('+strinofparamiters+')'

    def write_tuple_colums(self):
        fieldnames = [k for k in self.__class__.__dict__.keys() if not k.startswith('__')]
        typefields = [self.__class__.__dict__[k] for k in self.__class__.__dict__.keys() if not k.startswith('__')]

        strinofparamiters = ''

        for i in range(len(fieldnames)):
            strinofparamiters += fieldnames[i] + " " + typefields[i][0] + ','

        strinofparamiters = strinofparamiters[:-1]

        return '(' + strinofparamiters + ')'


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
