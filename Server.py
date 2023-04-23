from flask import Flask, render_template, request, redirect, url_for, session, flash
from Chat_GPT_Server import *
from connect_mysql import *
from datetime import timedelta
import json
app = Flask(__name__, static_folder='image')
app.config["SECRET_KEY"] = '123456'
app.permanent_session_lifetime = timedelta(minutes= 5)
@app.route('/', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authen(username, password) == True:
            session["user"] = username
            return redirect(url_for('menu'))
        else: 
            return render_template('login.html', error='Tên đăng nhập hoặc mật khẩu không chính xác!')
    elif "user" in session:
        return redirect(url_for('menu'))
    return render_template('login.html')
@app.route('/menu')
def menu():
    if 'user' in session:
        username = session['user']
        return render_template('menu.html',username = username)
    else:
        return redirect(url_for('login'))
@app.route('/chat', methods = ['GET', 'POST'])
def chat():
    if 'user' in session:
        username = session['user']
        if request.method == 'POST':
            ques = request.form['question']
            savequestion(session['user'], ques)
            list_A = list_question_user(session['user'])
            user = json.loads(list_A)
            return render_template('chat.html',user = user, username = username)
        else: 
            list_A = list_question_user(session['user'])
            user = json.loads(list_A)
            return render_template('chat.html',user = user, username = username)
    else:
        return redirect(url_for('login'))
@app.route('/checkme')
def checkme():
    if 'user' in session:
        res1 = None
        return render_template('menu.html', res1 = check_my_expVIP(session['user']))
    else:
        return redirect(url_for('login'))
@app.route('/beginlogout')
def beginlogout():
    return render_template('beginlogout.html')
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(host='0.0.0.0')