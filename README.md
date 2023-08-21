# Student Attrition Intervention Platform Template

Student attrition is still a common problem in education today. This project investigates the causes and factors involved in university student dropout rates withe the aim of providing support to the relevant students. 

The project uses machine learning techniques to identify features and patterns that can be used to interpret the data from an individual and provide the information relevant to their specific use case.

This template is designed as an open-source project to be customised for different situations and datasets. 

This template is designed as a development project and should NOT be used in production without modification. 

## Prerequisits

### Dataset
The dataset used by this project was provided by an open-source project on Kaggle. In order to ensure that the authors of the project recieve the relevant credit, the dataset has not be included with this template and needs to be downloaded seperately. 

The dataset can be downloaded from https://www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention

More information on the specifics of the dataset can be found in Realinho, V. et al. (2022) ‘Predicting Student Dropout and Academic Success’, Data, 7(11), p. 146. Available at: https://doi.org/10.3390/data7110146.

Once the dataset has been downloaded, add it to the local version of this respository at the following location (ensure that the file is named dataset.csv):

saip-template/student-attrition-model/data/dataset.csv 

### Software

If using Docker:
Docker

If not using Docker:
Python 3.11
NodeJS
MongoDB

## Initialisation steps 
This assumes that you have already installed the prerequisit software, cloned the repository and added the dataset to it. 

### Docker process

1. Navigate to the root of the project in a terminal. 
2. Enter the command: docker compose up -d
3. In a browser go to http://localhost

### Alternative local process
The project is setup to use docker. In order to use the local method the following files need to be edited: 

./student-intervention-model/db/services_pymongo.py -line 4: the docker variable needs to be changed to False
./student-intervention-server/utils/habitat.ts -line 3: the docker variable needs to be changed to true
./student-intervention-client/vite.config.ts -line 17-18: line 17 needs to commented out and line 18 needs to be uncommented. 

#### Initialise the model
1. Navigate to inside the student-atttrition-model directory found in the root of the project using a terminal.
2. Create a venv file by running the following (or os-varient of): python3 -m venv
3. Activate the venv by running the following (or os-varient of): source venv/bin/activate
4. Install the python requirements by running the following (or os-varient of): pip install -r requirements.txt
5. Before executing the command in step 6, please understand what the bind flag does. 
6. Start the model server by running one of the the following command: hypercorn --bind=0.0.0.0 main:create_app()

#### Initialise the server
1. Navigate to inside the student-atttrition-server directory found in the root of the project using a terminal.
2. Install the NodeJS requirements by running the following command: npm install
3. Start the server by running the following command: npm run start 

#### Initialise the user interface

1. Navigate to inside the student-atttrition-client directory found in the root of the project using a terminal.
2. Install the UI requirements by running the following command: npm install
3. Start the server by running the following command: npm run dev

#### To access the site
3. In a browser go to http://localhost:5173/