# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:57:47 2020

@author: Russel
"""

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DATA_UPLOAD_LOCATION                      = r'''D:/Program Projects/Offload-Nodejs-Flask-Server/flaskEnv/app/uploads/dump.txt'''
    K_MEANS_PCA_UPLOAD_PATH                   = r'''D:/Program Projects/Offload-Nodejs-Flask-Server/Resources/Clustering Resources/K-Means/PCA/'''
    K_MEANS_TSNE_UPLOAD_PATH                  = r'''D:/Program Projects/Offload-Nodejs-Flask-Server/Resources/Clustering Resources/K-Means/TSNE/'''
    K_MEANS_UMAP_UPLOAD_PATH                  = r'''D:/Program Projects/Offload-Nodejs-Flask-Server/Resources/Clustering Resources/K-Means/UMAP/'''
    MEAN_SHIFT_PCA_UPLOAD_PATH                = r'''D:/Program Projects/Offload-Nodejs-Flask-Server/Resources/Clustering Resources/Mean-Shift/PCA/'''
    MEAN_SHIFT_TSNE_UPLOAD_PATH               = r'''D:/Program Projects/Offload-Nodejs-Flask-Server/Resources/Clustering Resources/Mean-Shift/TSNE/'''
    MEAN_SHIFT_UMAP_UPLOAD_PATH               = r'''D:/Program Projects/Offload-Nodejs-Flask-Server/Resources/Clustering Resources/Mean-Shift/UMAP/'''
    EXPECTATION_MAXIMIZATION_PCA_UPLOAD_PATH  = r'''D:/Program Projects/Offload-Nodejs-Flask-Server/Resources/Clustering Resources/Expectation Maximation/PCA/'''
    EXPECTATION_MAXIMIZATION_TSNE_UPLOAD_PATH = r'''D:/Program Projects/Offload-Nodejs-Flask-Server/Resources/Clustering Resources/Expectation Maximation/TSNE/'''
    EXPECTATION_MAXIMIZATION_UMAP_UPLOAD_PATH = r'''D:/Program Projects/Offload-Nodejs-Flask-Server/Resources/Clustering Resources/Expectation Maximation/UMAP/'''