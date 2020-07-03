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
import os

FILE_COUNT = 0

def populate_clusters():
    """
    Cluster on the data defined in the data upload location. Save these clusters into a defined upload path
    
    Args:
   
    Returns:
    
    """
    slave_object = Clustering()
    path_to_data = Config.DATA_UPLOAD_LOCATION
    #KMeans
    slave_object.K_Means(switch = 0, path_to_data = path_to_data, path_to_upload = Config.K_MEANS_PCA_UPLOAD_PATH, n_clusters = 3 )
    slave_object.K_Means(switch = 1, path_to_data = path_to_data, path_to_upload =  Config.K_MEANS_TSNE_UPLOAD_PATH, n_clusters = 3 )
    slave_object.K_Means(switch = 2, path_to_data = path_to_data, path_to_upload =  Config.K_MEANS_UMAP_UPLOAD_PATH, n_clusters = 3 )
    #MeanShift
    slave_object.Mean_Shift(switch = 0, path_to_data = path_to_data, path_to_upload = Config.MEAN_SHIFT_PCA_UPLOAD_PATH)
    slave_object.Mean_Shift(switch = 1, path_to_data = path_to_data, path_to_upload = Config.MEAN_SHIFT_TSNE_UPLOAD_PATH)
    slave_object.Mean_Shift(switch = 2, path_to_data = path_to_data, path_to_upload = Config.MEAN_SHIFT_UMAP_UPLOAD_PATH)
    #Expectation Maximaziation    
    slave_object.Expectation_Maximation(switch = 0, path_to_data = path_to_data, path_to_upload = Config.EXPECTATION_MAXIMIZATION_PCA_UPLOAD_PATH)
    slave_object.Expectation_Maximation(switch = 1, path_to_data = path_to_data, path_to_upload = Config.EXPECTATION_MAXIMIZATION_TSNE_UPLOAD_PATH)
    slave_object.Expectation_Maximation(switch = 2, path_to_data = path_to_data, path_to_upload = Config.EXPECTATION_MAXIMIZATION_UMAP_UPLOAD_PATH)
 
         
@app.route('/')
@app.route('/index')
def index():
    """
    Index location has no use
    
    Args:
   
    Returns:
    
    """
    return "Microblog Active Server"

@app.route('/data-upload', methods=['GET', 'POST'])
def data_upload():
    """
    Get the file delivered to this location
    
    Args:
   
    Returns:
    
    """
    global FILE_COUNT
    

    if request.method == 'POST':   
               
        img = open(Config.DATA_UPLOAD_LOCATION, "wb")
        img.write(bytearray(request.get_data()))
        img.close()
        
        print('request.method', request.method)
        print('request.args', request.args)
        print('request.form', request.form)
        print('request.files', request.files)
        
        FILE_COUNT = FILE_COUNT + 1
        return "File Received"
 
@app.route('/clustering-page', methods = ['Get', 'POST'])
def clustering_suite():
    """
    Call the clustering location when this aspect of the webapp is called
    
    Args:
   
    Returns:
    
    """
    
    populate_clusters()
    return "Function Finished"

@app.route('/data-format-type', methods = ["GET"])
def check_type_of_data():
    #Check if data can be clusterd or forecasted

    return "True"
    
@app.route('/data-upload-count', methods = ["GET"])
def check_num_of_data():
    global FILE_COUNT
    return str(FILE_COUNT)

@app.route('/empty-upload', methods = ["GET",'POST'])
def purge_upload():
    #TODO remove all files from upload dir
    global FILE_COUNT
    FILE_COUNT= 0
    return "Purge Completed"


