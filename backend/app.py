import os
from flask import Flask, request, render_template

app = FLask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')

# indexにリダイレクト
@app.route('/', defaults={'path':''})
@app.route(''/<path:path>)
def index():
    return redirect(url_for('index'))

if __name__ == '__main__':
    
