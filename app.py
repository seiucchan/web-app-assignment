from flask import Flask
import os
import logging

def create_app():

    app = Flask(__name__)

    return app

app = create_app()