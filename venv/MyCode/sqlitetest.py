import sqlite3

db = sqlite3.connect('banco.db')
cur = db.cursor()
cur.execute("create table teste(id, nome)")
cur.execute("insert into teste (id, nome) values (1, 'Fabrício')")
cur.execute("insert into teste (id, nome) values (2, 'Pâmela')")
cur.execute("insert into teste (id, nome) values (3, 'Alice')")
cur.execute("select * from teste")
result = dict(cur.fetchall())
# print(result[2])
# dresult = dict(result)
# print(dresult)


def encerraBD(cur: sqlite3.Cursor, db: sqlite3.Connection):
    cur.close()
    db.commit()
    db.close()
    return "BD Encerrado"

for pessoa in result:
    if pessoa == 1:
        print("Eu sou o {}".format(result[pessoa]))
    else:
        print("Eu amo a {}".format(result[pessoa]))


def findData(cursor: sqlite3.Cursor, aString):
    cursor.execute("select * from teste where nome like ?", (aString,))
    return cursor.fetchall()


print(findData(cur, '%â%'))

print(encerraBD(cur, db))

