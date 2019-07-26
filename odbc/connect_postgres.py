import pyodbc

for x in pyodbc.drivers():
    print(x)
print("")

config = dict(server='localhost',
              port=54320,
              database='test',
              username='postgres',
              password='docker')

connection_str = (r"Driver=PostgreSQL Unicode(x64);"
                  r"Server={server};"
                  r"Port={port};"
                  r"Database={database};"
                  r"UID={username};"
                  r"PWD={password};")

cnxn = pyodbc.connect(connection_str.format(**config))
cursor = cnxn.cursor()
