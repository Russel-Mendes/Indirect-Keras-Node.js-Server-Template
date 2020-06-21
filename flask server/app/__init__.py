# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:46:59 2020

@author: Russel
"""

from flask import Flask
from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)

from app import routes