import pyodbc

config = dict(database='sqlite.db')

connection_str = (r"Driver=SQLite3 ODBC Driver;"
                  r"Database={database};")

cnxn = pyodbc.connect(connection_str.format(**config))
cursor = cnxn.cursor()
