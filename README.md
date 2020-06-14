# Indirect Keras Node.js Server Template Work In Progress


As Machine Learning becomes more effecient and more available to the masses, there more applications for the technology in many fields. One of the limiting factors for machine learning deployment are the large models for a task. Often times, a machine learning product has a large model which cannot be easily be deployed to the client. In addition to deployment issues, sometimes the model itself is proprietary. One solution to these problems is remote deployment through a webserver. This project tries to emulate this pipeline. By using a Node.js server that calls a remote Flask powered server housing a machine learning model, the client to product can be emulated.  

The goal of this project is to create an example webproduct. The website will be run with a Node.js server backend. This server will communicate with a Flask server for calculations. For the example, this project will emulate a basic classification and clustering website. 


## Structure:

### Client Interface
* Index
    * Basic landing page
* Break Down
    * Describes the attributes the data
* Clustering
    * Clusters the data given by the user
* Data Processing
    * Sets conditions on how the data should be processed. 
* Data Upload
    * Upload the data used by the web product
* Forecasting
    * Forecasts on the data given by the user

### Backend 
* Node.js
    * Servers the pages for the client
    * Sends requests to the Flask Server for offloaded computation
* Flask
    * Server that computes on the data sent by the Node.js server
    * Sends posts to the Node.js server with the results


## Installation TO BE UPDATED AS PROJECT PROGRESSES

Node.js Server
* Node.js
* express
* multer
Python Server
* Flask
* numpy
* umap
* sklearn

Author
Russel Mendes
