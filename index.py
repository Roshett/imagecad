import os
import json
from flask import Flask, jsonify, send_from_directory, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from intensity import deleteNoices
from coordinates import coordHarris
from random import randint


app = Flask(__name__, static_folder='static/dist')

@app.route('/')
def index():
    # тут просто пробрасываем файлик, без всякого препроцессинга
    return app.send_static_file("index.html")

@app.route('/dist/<path:path>')
def static_dist(path):
    # тут пробрасываем статику
    return send_from_directory("static/dist", path)

UPLOAD_FOLDER = './static/src/assets/img'
ALLOWED_EXTENSIONS = set(['pdf','png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload_file', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
        return filename
    else:
        return '300'

@app.route('/api/intensity', methods=['GET','POST'])
def intensity():
    if request.method == 'POST':
        data = request.get_data()
        dataDict = json.loads(data)
        name = dataDict["name"]
        intensity = dataDict["intensity"]
        hashId = deleteNoices(name,intensity)
    else:
        return '300'
    return hashId

@app.route('/api/corner_harris', methods=['GET','POST'])
def cornerHarris():
    if request.method == 'POST':
        data = request.get_data()
        dataDict = json.loads(data)
        print(dataDict)
        name = dataDict["name"]
        blockSize = dataDict["blockSize"]
        kSize = dataDict["kSize"]
        k = dataDict["k"]
        print(name)
        hashId = coordHarris(name,blockSize,kSize,k)
    else:
        return '300'
    return hashId

if __name__ == '__main__':
    app.run()