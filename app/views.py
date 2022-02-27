from app import app
from flask import render_template
from .request import topHeadlines

@app.route('/')
def index():
     return render_template('index.html',contents=contents,all=all)

