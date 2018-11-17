from flask import Flask,render_template,request,url_for
import urllib.request
import urllib.parse
import requests


url='localhost'
values = {'q':'input','submit':'search'}
r =requests.post(url =API_ENDPOINT, data = values)
p=r.text
print(p)

app= Flask(__name___)
@app.route('/input=<object>',methods="POST")

def input():
    return render_template("<html> ", )

@app.route('/output=<object>',methods="POST")

def output():
    return render_template(" <html> ", )



if ___name__ == "__main__ ":
    app.run()