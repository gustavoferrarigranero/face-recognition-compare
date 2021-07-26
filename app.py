import os
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)

