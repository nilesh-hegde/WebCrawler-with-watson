import sqlite3

conn=sqlite3.connect("emotion.db")
c=conn.cursor()

try:
    c.execute("""CREATE TABLE emo(e text,value integer)""")
    c.execute("""INSERT INTO emo VALUES('anger',0)""")
    c.execute("""INSERT INTO emo VALUES('fear',0)""")
    c.execute("""INSERT INTO emo VALUES('joy',0)""")
    c.execute("""INSERT INTO emo VALUES('sadness',0)""")
    c.execute("""INSERT INTO emo VALUES('analytical',0)""")
    c.execute("""INSERT INTO emo VALUES('confident',0)""")
    c.execute("""INSERT INTO emo VALUES('tentative',0)""")
except sqlite3.OperationalError:
    pass
conn.commit()

try:
    c.execute("""CREATE TABLE emotoi(e text,value integer)""")
    c.execute("""INSERT INTO emotoi VALUES('anger',0)""")
    c.execute("""INSERT INTO emotoi VALUES('fear',0)""")
    c.execute("""INSERT INTO emotoi VALUES('joy',0)""")
    c.execute("""INSERT INTO emotoi VALUES('sadness',0)""")
    c.execute("""INSERT INTO emotoi VALUES('analytical',0)""")
    c.execute("""INSERT INTO emotoi VALUES('confident',0)""")
    c.execute("""INSERT INTO emotoi VALUES('tentative',0)""")
except sqlite3.OperationalError:
    pass
conn.commit()

try:
    c.execute("""CREATE TABLE emondtv(e text,value integer)""")
    c.execute("""INSERT INTO emondtv VALUES('anger',0)""")
    c.execute("""INSERT INTO emondtv VALUES('fear',0)""")
    c.execute("""INSERT INTO emondtv VALUES('joy',0)""")
    c.execute("""INSERT INTO emondtv VALUES('sadness',0)""")
    c.execute("""INSERT INTO emondtv VALUES('analytical',0)""")
    c.execute("""INSERT INTO emondtv VALUES('confident',0)""")
    c.execute("""INSERT INTO emondtv VALUES('tentative',0)""")
except sqlite3.OperationalError:
    pass
conn.commit()
    
def ins(di):
    for x in di:
        #print(x,di[x])
        c.execute("UPDATE emo set value=value+{} where e='{}'".format(di[x],x))
    #c.execute("SELECT * FROM emo")
    #print(c.fetchall())
    conn.commit()


def instoi(di):
    for x in di:
        #print(x,di[x])
        c.execute("UPDATE emotoi set value=value+{} where e='{}'".format(di[x],x))
    #c.execute("SELECT * FROM emo")
    #print(c.fetchall())
    conn.commit()


def insndtv(di):
    for x in di:
        #print(x,di[x])
        c.execute("UPDATE emondtv set value=value+{} where e='{}'".format(di[x],x))
    #c.execute("SELECT * FROM emo")
    #print(c.fetchall())
    conn.commit()
