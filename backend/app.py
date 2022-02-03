import os
import io
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask, request, render_template
# テスト用
from pydub import AudioSegment

# firebase初期化
cred = credentials.Certificate('./key/eophis-ff982-firebase-adminsdk-b2q4q-b94cfa2f39.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://eophis-ff982-default-rtdb.firebaseio.com/',
    })

# flaskの初期化
app = Flask(__name__, static_folder='../front/src', template_folder='../front/public')

# databaseに初期データを追加
users_ref = db.reference('/users')

'''
# indexにリダイレクト
@app.route('/', defaults={'path':''})
@app.route(''/<path:path>)
def index():
    return redirect(url_for('index'))

# 登録
@app.route('/registration', methods=['POST'])
def register():
    if request.method == 'POST':
        # wav? mp3?
        in_audio = request.files['input_audio']
        intext = #google_speech_to_text(in_audio)

        
# 照合
@app.route('/recognition', methods=['POST'])
def recognize():
    if request.method == 'POST':
        in_audio = request.files['input_audio']
        in_text = #google_speech_to_text(in_audio)
        docs = db.collection('users').get()

    else:
        return make_response(jsonify({'result': 'invalid method'}), 400)
'''

# テスト
def register():
    #in_audio = AudioSegment.from_file('./test_audio/test.mp3', format='mp3').get_array_of_samples()
    with io.open('./test_audio/test.wav', 'rb') as f:
        in_audio = f.read()
    
    #in_contents =  google speech to text
    data = {}
    data['text'] = 'test'
    data['audio'] = str(in_audio)

    if users_ref.get() == none:
        f_num = 0
    else:
        f_num = (len(users_ref.get()) + 1) // 2 + 1
    print(f_num)
    users_ref.child(str(f_num)).set(data)

# テスト
def recognize():
    f_num = (len(users_ref.get()) + 1) // 2 + 1
    print(f_num)
    for i in range(1, f_num+1):
        texts_ref = db.reference('/users/' + str(i) + '/text')
        text = texts_ref.get()
        print(text)

if __name__ == '__main__':
    #register()
    #recognize()
    #flask_app.run(host='0.0.0.0', port=8000)


