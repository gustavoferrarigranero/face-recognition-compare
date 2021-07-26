import face_recognition
from flask import jsonify

def test_faces(image1, image2):
    image1 = face_recognition.load_image_file(image1)
    image2 = face_recognition.load_image_file(image2)
    image1_encoding = face_recognition.face_encodings(image1)[0]
    image2_encoding = face_recognition.face_encodings(image2)[0]
    results = face_recognition.compare_faces([image1_encoding], image2_encoding)
    return jsonify(equals=bool(results[0]))