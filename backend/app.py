import os
import io
import json
import firebase_admin
import numpy as np
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask, request, render_template
from recognition import speech_recognition, speaker_recognition
# テスト用
from pydub import AudioSegment

# firebase初期化
cred = credentials.Certificate('./key/eophis-ff982-firebase-adminsdk-b2q4q-b94cfa2f39.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://eophis-ff982-default-rtdb.firebaseio.com/',
    })

# flaskの初期化
app = Flask(__name__, static_folder='../front/dist/static', template_folder='../front/dist')

# databaseに初期データを追加
users_ref = db.reference('/users')

# indexにリダイレクト
@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

# 登録
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # wav? 
        app.logger.debug('register!!')
        f = request.files['input_audio']
        audio_path = '/tmp_audio/tmp.wav'
        with open(audio_path, 'wb') as audio:
            f.save(audio)

        with io.open('./tmp_audio/tmp.wav', 'rb') as f:
            in_audio = f.read()

        in_text = speech_recognition(in_audio)
        data = {}
        data['text'] = in_text
        data['audio'] = str(in_audio)

        if users_ref.get() == None:
            f_num = 1
        else:
            f_num = (len(users_ref.get()) + 1) // 2 + 1
            print(f_num)

        users_ref.child(str(f_num)).set(data)

        return redirect(url_for('index'))

    else:
        return make_response(jsonify({'result': 'invalid method'}), 400)


        
# 照合
@app.route('/recognition', methods=['POST'])
def recognize():
    if request.method == 'POST':
        f = request.files['input_audio']
        audio_path = '/tmp_audio/tmp.wav'
        with open(aduio_path, 'wb') as audio:
            f.save(audio)

        with io.open('./tmp_audio/tmp.wav', 'rb') as f:
            in_audio = f.read()

        in_text = speech_recognition(in_audio)
        f_num = (len(users_ref.get()) + 1) // 2 + 1
        speech_flag = False

        # 照合開始
        for i in range(1, f_num):
            # 話者照合
            texts_ref = db.reference('/users/' + str(i) + '/text')
            reg_text = texts_ref.get()
            speech_flag = speech_flag or (reg_text == in_text)


        result_json = {}
        result_json['result'] = speech_flag
        print(speech_flag)
        return make_response(jsonify(result_json), 400)


    else:
        return make_response(jsonify({'result': 'invalid method'}), 400)

'''
# テスト
def register():
    #in_audio = AudioSegment.from_file('./test_audio/test.mp3', format='mp3').get_array_of_samples()
    with io.open('./test_audio/「初めまして」.wav', 'rb') as f:
        in_audio = f.read()
    
    in_text = speech_recognition(in_audio)
    data = {}
    data['text'] = in_text
    data['audio'] = str(in_audio)

    if users_ref.get() == None:
        f_num = 1
    else:
        f_num = (len(users_ref.get()) + 1) // 2 + 1
    print(f_num)
    users_ref.child(str(f_num)).set(data)

# テスト
def recognize():
    with io.open('./test_audio/「初めまして」.wav', 'rb') as f:
        in_audio = f.read()

    in_text = speech_recognition(in_audio)
    f_num = (len(users_ref.get()) + 1) // 2 + 1
    speech_flag = False

    # 照合開始
    for i in range(1, f_num):
        # 話者照合
        texts_ref = db.reference('/users/' + str(i) + '/text')
        reg_text = texts_ref.get()
        speech_flag = speech_flag or (reg_text == in_text)
        
        # 話者照合
        audio_ref = db.reference('/users/' + str(i) + '/audio')
        reg_audio = audio_ref.get()
        with io.open('./test_audio/test.wav', 'w') as f:
            f.write(reg_audio)
        #speaker_flag = speaker_recognition(cat_audio)
    print(speech_flag)
'''

if __name__ == '__main__':
    #register()
    #recognize()
    app.run(host='127.0.0.1', port=8000)


