import mysql.connector, time, json
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="mydata"
)
def menu():
    print("1. Liệt kê người dùng")
    print("2. Kiểm tra câu hỏi")
    print("3. Thống kê")
    a = int(input("Chọn chức năng:"))
    if a == 1:
        listuser()
    elif a==2:
        check_question()
    elif a==3: 
        statistical()
def check_question():
    mycursor = mydb.cursor()
    query = 'select * from question'
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(f"user:{x[1]} question: {x[2]}")
def listuser():
    mycursor = mydb.cursor()
    query = 'select * from list_user'
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(f"ID: {x[0]}  username: {x[1]}        VIP: {x[3]}     exp VIP: {x[4]}")
def statistical():
    mycursor = mydb.cursor()
    query = 'select * from control_question'
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(f"user: {x[0]}    So cau hoi: {x[1]}  VIP: {x[2]}")