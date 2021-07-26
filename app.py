from flask import Flask, request
from faces import test_faces

app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/faces', methods = ['POST'])
def faces():
  return test_faces(
      request.files.get('image'), request.files.get('confirm')
    )

