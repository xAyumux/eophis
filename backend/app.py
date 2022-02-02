import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, request, render_template


cred = credentials.Certificate('./key/eophis-ff982-firebase-adminsdk-b2q4q-b94cfa2f39.json')
firebase_admin.initialize_app(cred)
app = FLask(__name__, static_folder='../front/src', template_folder='../front/public')

# indexにリダイレクト
@app.route('/', defaults={'path':''})
@app.route(''/<path:path>)
def index():
    return redirect(url_for('index'))

# 登録
@app.route('/registration', methods=['POST'])
def register():
    # ? register_audio_path = app_static_pass + "/audio/"

    # ディレクトリが存在するか
    if os.path.exists(register_audio_path):
        pass
    else:
        os.makerdirs(register_audio_path)

    if request.method == 'POST':

# 照合
@app.route('/recognition', methods=['POST'])
def recognize():
    if request.method == 'POST':
        input_audio = request.files['input_audio']
        input_text = #google_speech_to_text(input_audio)

        

        

        
    else:
        return mmake_response(jsonify({'result': 'invalid method'}), 400)

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=8000)


