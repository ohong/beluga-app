#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
from flask import jsonify
# from flask.ext.sqlalchemy import SQLAlchemy
import os

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
        name: "pretty-whale",
        status: "good"
    })


@app.route('/img')
def img():
    return jsonify({
        todo: "todo"
    })

@app.route('/ref')
def ref():
    return jsonify({
        todo: "todo"
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
    app.run(host='0.0.0.0', port=80)
