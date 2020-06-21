# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:32:21 2020

@author: Russel
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift 
from sklearn.mixture import GaussianMixture

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap

def PCA_setup(data_array):
    data_array = StandardScaler().fit_transform(data_array)
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(data_array)
    return principalComponents

def TSNE_setup(data_array):
    data_array = StandardScaler().fit_transform(data_array)
    tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
    tsne_results = tsne.fit_transform(data_array)
    return tsne_results

def UMAP_setup(data_array):
    data_array = StandardScaler().fit_transform(data_array)
    embedding = umap.UMAP(n_neighbors=50).fit_transform(data_array)
    return embedding

def create_colored_cluster_chart(path_to_save, title, data_array, model, n_clusters, extra = None):
    colored_cluster_array = []
    for point in data_array:
        ans = model.predict(point.reshape(1,-1))
        colored_cluster_array.append([point, ans.tolist()])
        
    color_suite = []
    for e in range(n_clusters):
        color_e = [i[0].tolist() for i in colored_cluster_array if i[1][0] == e ]
        color_ex = [i[0] for i in color_e]
        color_ey = [i[1] for i in color_e]
        color_suite.append([color_ex, color_ey])
        
    fig, ax = plt.subplots()
    title = "Identified Clusters - " + title 
    ax.set_title(title+ extra)
    color_list = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white']
    legend_list = []
    cluster_list = []
    i = 0
    for point_array in color_suite:
        leg = ax.scatter(point_array[0], point_array[1], s = 10, color=color_list[i])
        legend_list.append(leg)
        cluster_list.append('Cluster: ' + str(i))
        i+=1
    # Shrink current axis by 20%
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # Put a legend to the right of the current axis
    ax.legend(legend_list, cluster_list, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.savefig(path_to_save + title + ".png")

def create_possesion_chart(path_to_save, title, data_array, model, n_clusters, data_type, extra= None):
    x_data = [i[0] for i in data_array]
    y_data = [i[1] for i in data_array]
    
    point_array = []
    density_factor = 5
    for x in range(int(min(x_data)-1)*density_factor,int(max(x_data)+1)*density_factor):
        for y in range(int(min(y_data)-1)*density_factor,int(max(y_data)+1)*density_factor):
            point_array.append((np.array([x,y]))/density_factor)
            
    color_point_array = []

    for point in point_array:
        c_point = point.astype(data_type)
        t_point = c_point.reshape(1,-1)
       
        ans = model.predict(t_point)
        color_point_array.append([point, ans.tolist()])
        
    color_suite = []
    for e in range(n_clusters):
        color_e = [i[0].tolist() for i in color_point_array if i[1][0] == e ]
        color_ex = [i[0] for i in color_e]
        color_ey = [i[1] for i in color_e]
        color_suite.append([color_ex, color_ey])

    fig, ax = plt.subplots()
    title = "Possesion Chart - " + title
    ax.set_title(title+ extra)
    color_list = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white']
    legend_list = []
    cluster_list = []
    i = 0
    
    for point_array in color_suite:
        leg = ax.scatter(point_array[0], point_array[1], s = 10, color=color_list[i])
        legend_list.append(leg)
        cluster_list.append('Cluster: ' + str(i))
        i+=1
    ax.scatter(data_array[ : , 0], data_array[ :, 1], s = 25, color='k')
   
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    # Put a legend to the right of the current axis
    ax.legend(legend_list, cluster_list, loc='center left', bbox_to_anchor=(1, 0.5))
    
    plt.savefig(path_to_save + title + ".png")
    
def EM_Cluster(data, MIN_CLUSTERS = 1, MAX_CLUSTERS = 8):
    
    n_components = np.arange(MIN_CLUSTERS, MAX_CLUSTERS)
    models = [GaussianMixture(n, covariance_type='full', random_state=0).fit(data) for n in n_components]
    BIC_data_array = [m.bic(data) for m in models]
    AIC_data_array = [m.aic(data) for m in models]
    
    cluster_results = []
    if BIC_data_array.index(min(BIC_data_array)) < AIC_data_array.index(min(AIC_data_array)):
        cluster_results.append([" BIC",BIC_data_array.index(min(BIC_data_array))])
    else:
        cluster_results.append([" AIC",AIC_data_array.index(min(AIC_data_array))])
    
    return cluster_results

   
class Clustering():
    def K_Means(self, switch, path_to_data, path_to_upload, n_clusters = 3):
        title = "K-Means"
        df = pd.read_csv(path_to_data)
        key_arr = df.columns.values
        #Since we are clustering, we do not need to care about the key
        data_df = df.drop(key_arr[-1], axis = 1)
        data_array = data_df.values
        number_of_dim = (data_array.shape)[-1]
        if(number_of_dim > 2):
        #We have to compress
            if(switch == 0):
                title += " PCA"
                data_array = PCA_setup(data_array)
            if(switch == 1):
                title += " TSNE"
                data_array = TSNE_setup(data_array)
            if(switch == 2):
                title += " UMAP"
                data_array = UMAP_setup(data_array)
        
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data_array)
        Kmean = KMeans(n_clusters)
        Kmean.fit(data_scaled)
        data_type = data_array.dtype
        create_possesion_chart(path_to_upload, title, data_array, Kmean, n_clusters , data_type)
        create_colored_cluster_chart(path_to_upload, title, data_array, Kmean, n_clusters )
        print("Finished")
        
    def Mean_Shift(self, switch, path_to_data, path_to_upload, radius = .75):
        title = "Mean-Shift"
        df = pd.read_csv(path_to_data)
        key_arr = df.columns.values
        #Since we are clustering, we do not need to care about the key
        data_df = df.drop(key_arr[-1], axis = 1)
        data_array = data_df.values
        number_of_dim = (data_array.shape)[-1]
        if(number_of_dim > 2):
        #We have to compress
            if(switch == 0):
                title += " PCA"
                data_array = PCA_setup(data_array)
            if(switch == 1):
                title += " TSNE"
                data_array = TSNE_setup(data_array)
            if(switch == 2):
                title += " UMAP"
                data_array = UMAP_setup(data_array)

        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data_array)
       
        meanShift = MeanShift(bandwidth = radius)        
        meanShift.fit(data_scaled)
        num_of_cluster = len(meanShift.cluster_centers_)
        data_type = data_array.dtype
        create_possesion_chart(path_to_upload, title, data_array, meanShift, num_of_cluster , data_type)
        create_colored_cluster_chart(path_to_upload, title, data_array, meanShift, num_of_cluster )
        print("Finished")
        
    
    def Expectation_Maximation(self, switch, path_to_data, path_to_upload):
        title= "Expectation-Maximation"
        df = pd.read_csv(path_to_data)
        key_arr = df.columns.values
        #Since we are clustering, we do not need to care about the key
        data_df = df.drop(key_arr[-1], axis = 1)
        data_array = data_df.values
        number_of_dim = (data_array.shape)[-1]
        if(number_of_dim > 2):
        #We have to compress
            if(switch == 0):
                title += " PCA"
                data_array = PCA_setup(data_array)
            if(switch == 1):
                title += " TSNE"
                data_array = TSNE_setup(data_array)
            if(switch == 2):
                title += " UMAP"
                data_array = UMAP_setup(data_array)
        
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data_array)        
        
        option = EM_Cluster(data_scaled)[0]
        extra = str(option[0])
        clusters = option[1]
        gmm = GaussianMixture(n_components = clusters)
        gmm.fit(data_scaled)
        data_type = data_array.dtype
        create_possesion_chart(path_to_upload, title, data_array, gmm, clusters , data_type, extra)
        create_colored_cluster_chart(path_to_upload, title, data_array, gmm, clusters, extra )
   
        print("Finished")
      
      
    