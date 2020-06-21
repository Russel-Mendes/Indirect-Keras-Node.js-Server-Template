# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:57:47 2020

@author: Russel
"""

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DATA_UPLOAD_LOCATION =  r'''D:\Program Projects\Machine Learning in Production\Server Side Version\flaskEnv\app\uploads\dump.txt'''
    K_MEANS_PCA_UPLOAD_PATH = r'''D:/Program Projects/Machine Learning in Production/Server Side Version/Resources/Clustering Resources/K-Means/PCA/'''
    K_MEANS_TSNE_UPLOAD_PATH = r'''D:/Program Projects/Machine Learning in Production/Server Side Version/Resources/Clustering Resources/K-Means/TSNE/'''
    K_MEANS_UMAP_UPLOAD_PATH = r'''D:/Program Projects/Machine Learning in Production/Server Side Version/Resources/Clustering Resources/K-Means/UMAP/'''
    