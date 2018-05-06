import base64


from flask import Flask, request, jsonify, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES

import retrain_run_inference

app = Flask(__name__)


def convert_and_save(b64_string, key):
    filename = "C:/tmp/imageToSave_"+key+".png"
    with open(filename, "wb") as fh:
        fh.write(base64.decodestring(b64_string.encode()))
        return filename

@app.route('/upload',methods = ['POST','GET'])
def upload_base64_file():

  data = request.form['img']
  key = request.form['key']
  # print(data)

  if data is None:
        print("No valid request body, json missing!")
        return jsonify({'error': 'No valid request body, json missing!'})

  else:

      img_data = data
      filename = convert_and_save(img_data, key)

  imagePath = filename  # 이거 대신에 저장한 이미지의 path를 넣어줌
  return retrain_run_inference.run_inference_on_image(imagePath)


if __name__ == '__main__':
    app.debug = True
    app.run()

