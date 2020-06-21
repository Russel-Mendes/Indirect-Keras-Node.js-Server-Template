# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:48:27 2020

@author: Russel
"""
from flask import render_template
from app import app
from flask import request #import main Flask class and request object
from app.config import Config
from app.calculations import Clustering



def populate_clusters():
    slave_object = Clustering()
    path_to_data = Config.DATA_UPLOAD_LOCATION
    #KMeans
    slave_object.K_Means(switch = 0, path_to_data = path_to_data, path_to_upload = Config.K_MEANS_PCA_UPLOAD_PATH, n_clusters = 3 )
    slave_object.K_Means(switch = 1, path_to_data = path_to_data, path_to_upload =  Config.K_MEANS_TSNE_UPLOAD_PATH, n_clusters = 3 )
    slave_object.K_Means(switch = 2, path_to_data = path_to_data, path_to_upload =  Config.K_MEANS_UMAP_UPLOAD_PATH, n_clusters = 3 )

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('welcome.html', title = 'Home', user = user)


@app.route('/data-upload', methods=['GET', 'POST'])
def data_upload():

    if request.method == 'POST':   
               
        img = open(Config.DATA_UPLOAD_LOCATION, "wb")
        img.write(bytearray(request.get_data()))
        img.close()
        
        print('request.method', request.method)
        print('request.args', request.args)
        print('request.form', request.form)
        print('request.files', request.files)
        
        
        return "File Received"
 
@app.route('/clustering-page', methods = ['Get', 'POST'])
def clustering_suite():
    populate_clusters()

    
    return "Function Finished"
    