import os
import sys
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

#for data read from .env have to 
#use load_dotenv and import it and for this add python-dotenv 
# in requirement.txt file and install it
# firstly to connect sql with this 
#add mysql-connector-python and pymysql in requirement.txt file and install it

#we ahve to load 4 info from .env
host=os.getenv('host')
user=os.getenv('user')
password=os.getenv('password')
db=os.getenv('db')
 #now from this lines alll info came now on 
 #this basis we will write code to read data from sql database 
 # and add it in csv file and then we will use that csv file 
 # for training and testing purpose

def read_sql_data():
    logging.info('Reading data from mysql database started')
    try:
        #for this code have to first impot pymysql
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        ) #this code is databse is connected to mydb

        logging.info("Connection Established Successfully",mydb)
        df=pd.read_sql_query('Select * from students',mydb) 
        #this code is for reading data from sql database and add it in dataframe

        print(df.head())

        return df
    
    except Exception as ex:
        raise CustomException(ex,sys)