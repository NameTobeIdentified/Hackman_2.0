from flask import Flask, redirect, url_for, request, render_template
import json

app = Flask(__name__)
from flask_cors import CORS
CORS(app)

'''
#routes
UI -> sendData -> Server
Server -> 




'''

@app.route('/login',methods = ['POST', 'GET'])
def login():
	print ("hello")
	return render_template('login.html')
	  
@app.route('/display', methods = ['POST', 'GET'])
def display():
	user = request.form['nm']
	jsonob = {}
	jsonob["name"] =  user
	# print (user)
	# print JSON.parse(jsonob)
	return json.dumps(jsonob)  
   
if __name__ == '__main__':
   app.run(	host='0.0.0.0',debug = True)