import sqlite3
conn=sqlite3.connect('kika.db')
c=conn.cursor()
c.execute('''Create table stka(name text,address text,age real,mobileno int)''')
c.execute("Insert Into stka Values('sanjay','lpu',29,'959241')")
c.execute("insert into stka values('jack','lpu',28,'945673')")
conn.commit()
conn.close()
