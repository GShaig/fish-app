=====
Fish App
=====

Fish App is a Python/Django backend and React Js frontend web application. The app predicts the fish weights based on fish dimensions received as input and visualizes the results with the line graphs with all possible combinations.

Deployment:
-----------
The application is deployed to heroku. Please visit below link to check and use the app:

    https://fishweights.herokuapp.com/


Python/Django Backend:
--------
Fish Backend API is a Django app serving as a backend API for Fish app. The API takes a CSV file as an input, turns it into a Pandas dataframe and uses a special model to predict fish weights based on their dimensions. After necessary calculations, the app adds 'Weight' column to the dataframe and visualizes the results on a seaborn graph.


Javascript/ReactJs Frontend:
---------
Fish Frontend API is a React Js application which uses class-based components. The API takes a CSV file as an input with the help of a small form. Submit action sends the file to the Backend API with axios POST request. After necessary calculations from backend side, the API again takes the results graphs from AWS S3 storage and visualizes for users.


Storage:
--------
Amazon AWS S3 storage was used for deployed version. The app uploads the input CSV file to the storage and again saves the results graphs to the storage in PNG format.
Static files storage: AWS S3
Media files storage: AWS S3


Communication Protocol:
-----------------------
Frontend API communicates with Backend API with the help of HTTP requests. Frontend API uses axios - a promise-based HTTP client and Backend API uses standard Django REST framework for communication.


Database:
---------
Deployed version of the app uses Heroku provided PostgreSQL database.
Local version uses local SQLite database.

Setup:
------
Please refer Fronted or Backend folder for relevant API setup information. Thanks!