from flask import Flask
app = Flask(__name__)
from flask import request, redirect
from flask import render_template
import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
data=data[0]
data_rates=data["rates"]


header = ['currency', 'code', 'bid', 'ask']

writer = csv.writer(open('/home/bartosz/Pulpit/Kodilla/Python/mod9_kalkulator/plik.csv', "w"), delimiter=';', dialect=csv.excel)
writer.writerow(header)

for i in data_rates:
    tab=[]
    tab.append(i["currency"])
    tab.append(i["code"])
    tab.append(i["bid"])
    tab.append(i["ask"])
    print(tab)
    writer.writerow(tab)
    
    print("----------------------")


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
