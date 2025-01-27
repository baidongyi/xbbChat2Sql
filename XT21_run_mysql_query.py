
import mysql.connector

def test01():

    mydb = mysql.connector.connect(
      host="10.1.21.164",
      user="root",
      password="1qazXSW@",
      database="mysql"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM xxtony_user_tbl")

    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)


if __name__ =='__main__':
    test01()