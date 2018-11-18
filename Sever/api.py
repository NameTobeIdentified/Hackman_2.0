from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import os
import json

app = Flask(__name__)
from flask_cors import CORS
CORS(app)
summary = ''
'''
#routes
UI -> sendData -> Server
					Server -> getData -> ML
											ML -> sendJSON -> Server
																Server -> getJSON -> UI
'''
UPLOAD_FOLDER = '/toextract/'
ALLOWED_EXTENSIONS = set(['mp4', 'avi', 'flv', 'mp3', 'mov','wav'])


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
	return render_template("upload.html")

@app.route('/sendData', methods = ['POST'])
def sendData():
    if request.method == 'POST':
        global f
        f = request.files['file']
        # print(f)
        filename = secure_filename(f.filename)
        f.save(str("./"+filename))
        print('<script>alert("Done!");</script>')
        pass
    else:
        print('<script>alert("Error");</script>')
        pass

@app.route('/getData', methods = ['GET'])
def getData():
    if request.method == 'GET':
        global f
        print(f)
        return
    else:
        print('<script>alert("Error");</script>')
        return
	
from werkzeug import SharedDataMiddleware
app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})

app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024	
	
@app.route('/sendJSON', methods = ['POST'])
def sendJSON():
	global summary
	summary = request.form['summary']
	print('<script>alert("Done!");</script>')
	
@app.route('/getJSON', methods = ['GET'])
def getJSON():
	global summary
	return json.dumps({"summary":summary})

if __name__ == '__main__':
   app.run(	host='0.0.0.0',debug = True)