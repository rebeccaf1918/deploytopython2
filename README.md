# Web Services & Applications Module

# ATU Galway Data Analytics HDip 2023/2024  
## Web Services & Applications Project 
Created by Rebecca Feeley   
Student ID G00425652  

# Introduction
This repository contains my project for the the Web Services and Application module assigned as part of the Web Services and Application module 2024.
The Web Services and Application module forms part of the ATU Galway Higher Diploma in Science in Computing in Data Analytics.


# Technical Requirements
## To download this Work
1. Go to my repository on Github at https://github.com/rebeccaf1918/deploytopython2
2. From there, you can choose how to use the repository whether that is downloading it as a zipfile or cloning the repository.  


## Requirements & Instructions  
In order to complete my work, I imported the libraries required as listed in the requirements.txt file.



## **Table of Contents**

- [Introduction](#introduction)
- [Project Contents](#project-contents)
    - [songDAO](#songDAOpy)
    - [server](#serverpy)
    - [config file](#dbconfigpy)
    - [songViewer](#songViewerhtml)
    - [requirements](#requirementstxt)
- [Online Hosting](#online-hosting)
- [Running the Program](#running-the-program)
- [References](#references)

## **Introduction**
A web application was created for a database containing a table of Taylor Swift Songs. 
This was hosted online using the website PythonAnywhere (https://rebeccaf1918.pythonanywhere.com/songViewer.html)
This application lets users view the table in the database and perform CRUD operations on the table i.e it allows users to create, update or delete data.

## **Project Contents**
The repository contains various files necessary to create and host the web application. The files contained in the repository are as follows:

    - songDAO.py
    - server.py
    - songViewer.html
    - config file
    - requirements file


### **server.py**
The server.py file is a Flask application which is used as a backend server. Flask is a lightweight Python web framework which facilitates a simple web application being deployed to a server. The server uses RESTful API endpoints to handle any CRUD operations carried out on the Taylor Swift songs data. The user then interacts with this through the web page songView.html.

### **songDAO.py**
The songDAO.py file contains the Data Access Object (DAO) which is utilised to link with the MySQL database and the main application. Through this DAO file, the database connections and the execution of SQL database queries are carried out and the relevant results are returned.

### **config file**
The config file contains the details of the Database Configuration settings required to access the database (e.g host name and password).

### **songViewer.html**
The songViewer file is operates as the frontend interface, setting out how the user views the web page. It is a HTML (HyperText Markip Language) file which handles the structure of the page, CSS for the style of the page and Javascript (and Ajax) for the behaviour of the web page.

### **requirements.txt**
This text file sets out the required modules to operate this code.


## **Online Hosting**
The web application is hosted online using PythonAnywhere. 
A Github repostitory, containing all the required code, is used to deploy the application to the server.



## **References**
