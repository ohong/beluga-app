#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
from flask import jsonify
# from flask.ext.sqlalchemy import SQLAlchemy
import os
import uuid
import base64
import sys
import time
import re


# sys.path.append('./cgi-bin/wnet')
sys.path.append('./cgi-bin/paint_x2_unet')
import cgi_exe
sys.path.append('./cgi-bin/helpers')
from platformAdapter import OSHelper


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

@app.route('/colorize', methods = ['POST'])
def colorize():
    content = request.json
    grey_encoded = content["grey_image"] # the base64 of the img
    color_encoded = content["color_image"] # the base64 of the img
    grey = base64.b64decode(grey_encoded)
    color = base64.b64decode(color_encoded)
    img_id = str(uuid.uuid4())
    # save the image
    sketch = open("./images/line/" + img_id + ".png", 'wb')
    sketch.write(grey)
    sketch.close()
    # save the ref
    ref = open("./images/ref/" + img_id + ".png", 'wb')
    ref.write(color)
    ref.close()

    painter.colorize(img_id)

    #output
    f = open("./images/out/"+ img_id + "_0.png", "rb+")
    colorized = f.read()
    f.close()
    return jsonify({
        "id": img_id,
        "colorized_image": str(base64.b64encode(colorized))[2:-1]
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
    painter = cgi_exe.Painter(gpu=0)
    app.run(host='0.0.0.0', port=80)
