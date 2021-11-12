from flask import Flask
app = Flask(__name__)
from flask import request, redirect
from flask import render_template


@app.route('/base', methods=['GET', 'POST'])
def base():
   if request.method == 'GET':
       print("We received GET")
       return render_template("mypage/base.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/me', methods=['GET', 'POST'])
def me():
   if request.method == 'GET':
       print("We received GET")
       return render_template("mypage/me.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("mypage/contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return render_template("mypage/contact.html")
