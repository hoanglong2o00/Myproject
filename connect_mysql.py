import mysql.connector, datetime, json, hashlib
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="mydata"
)
def authen(u: str, p: str):
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM list_user")
  myresult = mycursor.fetchall()
  p = hashlib.md5(p.encode())
  p = p.hexdigest()
  for x in myresult:
    if x[1] == u and x[2]==p:
      return True
  return False
def savequestion(u: str, q: str):
  mycursor = mydb.cursor()
  now = datetime.datetime.now()
  nowformat = now.strftime("%Y-%m-%d %H:%M:%S")
  res = ""
  if check_VIP(u) == True:
    res = " Chức năng hiện đang phát triển!"
  elif check_VIP(u) == False:
    res = "Bạn đã hết số lượng câu hỏi, vui lòng nâng cấp lên VIP"
  query = f"insert into question(user_name, question, answer, timezone) values ('{u}', '{q}', '{res}', '{nowformat}');"
  mycursor.execute(query)
  mydb.commit()
def check_VIP_exp(u:str):
  mycursor = mydb.cursor()
  query = f"select * from list_user where username = '{u}'"
  mycursor.execute(query)
  myresult = mycursor.fetchall()
  for x in myresult:
    if x[4] > datetime.date.today():
      return True
    else:
      return False
def check_VIP(u: str):
  mycursor = mydb.cursor()
  query = 'select * from Control_question'
  mycursor.execute(query)
  myresult = mycursor.fetchall()
  for x in myresult:
    if u == x[0]:
      if x[1] <5:
        return True
      else:
        if x[2] == 0: 
          return False
        else:
          if check_VIP_exp(u) == True:
            return True
          else:
            return False
    else:
      continue;
  else:
    return True
def check_my_expVIP(u: str):
  mycursor = mydb.cursor()
  query = f"select * from list_user where username = '{u}'"
  mycursor.execute(query)
  myresult = mycursor.fetchall()
  for x in myresult:
    return f"Tài khoản: {u}  Thời hạn VIP: {x[4]}"
def list_question_user(u:str):
    mycursor = mydb.cursor()
    query = f"select * from question where user_name = '{u}' order by timezone"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    A = {
      "user": u,
      "hits": []
    }
    for x in myresult:
        data = {
      "ques": str,
      "ans": str
    }
        data["ques"] = x[2]
        data["ans"] =  x[3]
        A["hits"].append(data)
    A = json.dumps(A, indent=4,ensure_ascii=False)
    return A
def update(u: str):
  mycursor = mydb.cursor()
  new_VIP = datetime.date.today() + datetime.timedelta(days= 30)
  query = f"update list_user set VIP = 1, exp_VIP = '{new_VIP}' where username = '{u}'"
  mycursor.execute(query)
  mydb.commit()
  print(print("Hôm nay là : ", datetime.date.today(), " Bạn sẽ là VIP đến ngày: ", datetime.date.today()+datetime.timedelta(days=30)))
# list_A = list_question_user('hoanglong2o00')
# A =  json.loads(list_A)
# print(type(A))
# for x in A["hits"]:
#   print(x)
# print(list_question_user('hoanglong2o00'))
savequestion('hoanglong2o00', 'xin chào')
print(check_VIP('hoanglong2o00'))