# Online Data Processor and Analyzer

## Description
In the world of big data, complex algorithms are required to process data and give meaningful output. Often times, the model created are far too big to be deployed to the client side. One solution for this is simply having the client interact with a page that calls a server that calls the model and sends the result. This method has the added advantage that the model is secured away from the client, protecting the company's assets. This demo program seeks to replicate this system through a NodeJS server and Python Flask microapp.The user will interact with the Node JS as if it were a simple application and will send the user commands to the Flask Server and have python to conduct machine learning algorithms, such as clustering, classification, and forecasting

## How To Use
To deploy this program, the user has to download the entire repository. There are two main components: nodejs and python. The python section is a folder for an environment. The "flaskEnv" is a python virtual environment. A user has to activate the environment and locally install flask, keras, and other necessary dependencies Inside the virtual environment, run the "microblog.py" from the terminal. This allows the flask portion of the code to run. <br> 
For the NodeJS portion of the code, the same process has to be applied. The user has to install the required NodeJS dependencies and run the program. This can be done by executing the "main.js" file. <br>
This repository has the downloaded dependencies already uploaded. Since the program is meant to be a replica of a larger system, a snapshot upload will suffice as an example deployment of this program. If there are any issues, please refer to the dependencies section of this program


## Dependencies
### Python
* Flask
* Keras
* Scipy
* Numpy
### NodeJS
* Express
* Multper

## Release Version
Version 0.25

## Added Features
* User can upload .txt or .csv files for the program to analyze
* User can see a list of clustering performed by the program

## Future Features
* Creating a user database where data is saved between sessions

## Known Bugs