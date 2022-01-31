from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from wallet.messages import START_PROCESS

logging.info(START_PROCESS)   
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:docker@localhost/CPEX'
db = SQLAlchemy(app)

if __name__ == "__main__":
    from wallet.controller import *
    app.run(debug=True)