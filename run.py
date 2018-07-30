# run.py

import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':

    app.run(use_reloader=True)
