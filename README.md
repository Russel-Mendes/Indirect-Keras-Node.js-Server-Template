# Offload Node.js Flask Server Work In Progress


As data processing becomes more effecient and more ubiquotous in products, there are more applications for the technology in many fields. One of the limiting factors for this technology are the large model. Often times, data models are large which limits deployment. In addition to deployment issues, sometimes the model itself is proprietary. One solution to these problems is remote deployment through a webserver. This project tries to emulate this pipeline. By using a Node.js server that calls a remote Flask powered server housing a machine learning model, the client to product can be emulated.  

The goal of this project is to create an example webproduct. The website will be run with a Node.js server backend. This server will communicate with a Flask server for calculations. For the example, this project will emulate a basic classification and clustering website. 

# How To Use
To deploy this program, the user has to download the entire repository. There are two main components: nodejs and python. The python section is a folder for an environment. The "flaskEnv" is a python virtual environment. A user has to activate the environment and locally install flask, keras, and other necessary dependencies Inside the virtual environment, run the "microblog.py" from the terminal. This allows the flask portion of the code to run. 
For the NodeJS portion of the code, the same process has to be applied. The user has to install the required NodeJS dependencies and run the program. This can be done by executing the "main.js" file. 
This repository has the downloaded dependencies already uploaded. Since the program is meant to be a replica of a larger system, a snapshot upload will suffice as an example deployment of this program. If there are any issues, please refer to the dependencies section of this program

# Structure:

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


# Installation TO BE UPDATED AS PROJECT PROGRESSES

Node.js Server
* Node.js
* express
* multer
Python Server
* Flask
* numpy
* umap
* sklearn

# Author
Russel Mendes
