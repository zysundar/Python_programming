import sqlite3
c=sqlite3.connect('ete.db')
d=c.cursor()
d.execute(CREATE table  sundaram(rno real,name text,mb real))
d.execute(insert into sundaram values(11505607,'sundaram',841900))
c.commit()
c.close()
          
