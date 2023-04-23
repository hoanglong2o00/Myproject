import requests, json
from connect_mysql import authen, savequestion, check_VIP, update,check_my_expVIP
def sendquestion():
    url = "https://api.openai.com/v1/chat/completions"
    url2 = "https://api.openai.com/v1/models"
    api_key = "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"
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model":"babbage",
        "prompt": "Hello!",
        "temperature": 0.5,
        "max_tokens": 16,
        "top_p": 1.0,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    # res2 = requests.get(url2, headers=header)
    # print(res2.text)
    res = requests.post(url, headers=header, json=data)
    result = res.json()
    print("response: ", json.dumps(result, indent= 4))
def login():
    user = input("Nhập username: ")
    passwd = input("Nhập password: ")
    if authen(user,passwd) == True:
        menu(user)
    else:
        print("Đăng nhập sai! Bấm phím ESC nếu muốn hủy bỏ!")
def postquestion(u: str):
    if check_VIP(u) == True:
        ques = input("Nhập câu hỏi của bạn: ")
        savequestion(u,ques)
        print("Chức năng này đang phát triển!")
    else:
        print("Bạn đã dùng hết số câu free")
def update_VIP(u: str):
    print("Bạn có muốn gia hạn thêm 1 tháng không ?")
    print("Bấm Y để đồng ý!")
    a = input()
    if a == 'Y':
        update(u)
def menu(u: str):
    print("1. Đặt câu hỏi")
    print("2. Nâng cấp VIP")
    print("3. Kiểm tra thời hạn VIP")
    a = int(input("Chọn chức năng: "))
    if a == 1:
        postquestion(u)
    elif a==2:
        update_VIP(u)
    elif a==3:
        check_my_expVIP(u)