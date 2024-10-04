import mysql.connector
# cursor=None
# db=None
try:
    db=mysql.connector.connect(host='localhost',user='root',password='Eswar123',database='eswar')
    print(db)
    cursor=db.cursor()
    sql_st='select * from 10am'
    cursor.execute(sql_st)
    employe=cursor.fetchall()
    for i in employe:
        print(i)
except mysql.connector.Error as err:
    print(err)
# finally:
    # cursor.close()
    # db.close()