# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:43:40 2020

@author: Russel
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'