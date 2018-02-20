import sqlite3


def connect_to_data_base(name):
    return sqlite3.connect(name)


def drop_table(tablename, connect):
    connect.execute('drop table if exists %(table)s' % {'table': tablename})
    connect.commit()


def get_where_parameters(datatoupdat):
    whereparamiters = datatoupdat.pop('where')

    return whereparamiters


def write_string_paramiters(searchparamiters):
    parameters = ''
    for key in searchparamiters.keys():
        parameters = parameters + str(key) + ' =?,'

    return parameters[:-1]


def get_values(alldataparamiters):
    return [alldataparamiters[key] for key in alldataparamiters]


def write_paramiters_to_insert(paramiterstoinsert):
    parameters = []
    for key in paramiterstoinsert.keys():
        parameters.append(str(key))
    strinofparamiters = ', '.join(parameters)
    return '(' + strinofparamiters + ')'


def union_values_for_cimmit(dataforupdate, dataforsearchinbase):
    return [dataforupdate[key] for key in dataforupdate] + [dataforsearchinbase[key] for key in dataforsearchinbase]


def update_data(table, **updatedata):
    dictwhereparamiters = get_where_parameters(updatedata)
    paramitertosearch = write_string_paramiters(dictwhereparamiters)
    columnnames = write_string_paramiters(updatedata)
    valuestochange = union_values_for_cimmit(updatedata, dictwhereparamiters)
    querystrig = 'UPDATE %(nametable)s SET %(columns)s WHERE %(where)s' % {'nametable': table.tablename,
                                                                           'columns': columnnames,
                                                                           'where': paramitertosearch}
    table.currentcursor.execute(querystrig, valuestochange)
    table.currentbase.commit()
    return table


def write_colums_for_create_table(fields_in_table):
    fieldnames = [k for k in fields_in_table.keys() if not k.startswith('__')]
    typefields = [fields_in_table[k] for k in fieldnames]

    stringparamiters = ''

    for index in range(len(fieldnames)):
        stringparamiters += fieldnames[index] + " " + typefields[index] + ','

    stringparamiters = stringparamiters[:-1]

    return '(' + stringparamiters + ')'


def insert_data(tabletoinsert, **datatoinsert):

        columns = write_paramiters_to_insert(datatoinsert)
        values = get_values(datatoinsert)
        queryparamiters = ('?,' * len(datatoinsert))[:-1]
        querystring = 'INSERT INTO %(table)s %(columns)s values(' % {'table': tabletoinsert.tablename,
                                                           'columns': columns} + queryparamiters + ')'
        tabletoinsert.currentcursor.execute(querystring, values)
        tabletoinsert.currentbase.commit()
        return tabletoinsert


def write_columns_to_select(columns):
    stringofcolumns = ','.join(columns)
    return  stringofcolumns

class dbservice():
    def __init__(self, coonect):
        self.tablename = type(self).__name__
        self.currentbase = coonect
        self.currentcursor = self.currentbase.cursor()
        self.dict_fields = self.__class__.__dict__

    def select_all(self):
        self.currentcursor.execute('SELECT * FROM %(table)s' % {'table': self.tablename})

        return self.currentcursor.fetchall()

    def select(self, columns_to_choise):

        stringcolumns =  write_columns_to_select(columns_to_choise)

        self.currentcursor.execute('SELECT %(columns)s FROM %(table)s' % {'table': self.tablename, 'columns': stringcolumns})

        return self.currentcursor.fetchall()

    def create_table(self):
        columns = write_colums_for_create_table(self.dict_fields)

        self.currentcursor.execute('CREATE TABLE %(table)s %(columns)s' % {'table': self.tablename, 'columns': columns})

        self.currentbase.commit()

        return self

if __name__ == "__main__":
    pass
