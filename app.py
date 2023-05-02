from flask import Flask
from flask_cors import CORS
from uuid import uuid4
import sys
import os
import argparse

global csv_load
csv_load = False

def create_app():
    from usercontroller import user_blueprint

    app = Flask(__name__)
    # Swagger(app)
    # Random Secret Key
    app.secret_key = uuid4().hex
    app.config['DEBUG'] = True
    CORS(app, allow_headers=['Content-Type', 'Access-Control-Allow-Origin',
                             'Access-Control-Allow-Headers', 'Access-Control-Allow-Methods'])

    app.register_blueprint(user_blueprint, url_prefix='/v1')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5555, debug=True)

