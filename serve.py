#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
from flask import jsonify
# from flask.ext.sqlalchemy import SQLAlchemy
import os
import uuid
import base64

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return jsonify({
        "name": "pretty-whale",
        "status": "good"
    })

@app.route('/img', methods = ['POST'])
def img():
    content = request.json
    encoded_img = content["encoded_img"] # the base64 of the img
    decoded_img = base64.b64decode(encoded_img)
    img_id = str(uuid.uuid4())
    # save the image
    fout1 = open("./images/line/" + img_id + ".png", 'wb')
    fout1.write(decoded_img)
    fout1.close()
    # save the ref
    fout1 = open("./images/ref/" + img_id + ".png", 'wb')
    fout1.write(decoded_img)
    fout1.close()

    return jsonify({
        "id": img_id,
    })

@app.route('/ref', methods = ['POST'])
def ref():
    # STUB
    return jsonify({
        "todo": "todo"
    })

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({
        "status": "404 Not Found"
    })

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
