import os
import sys
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
import pandas as pd
from src.ml_project.utils import read_sql_data

from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            #reading the data from mysql database have to write code
            #in utilis and add all data in .env variable and import it here
            df=read_sql_data()  #this line indicates dataframe came here
            #and this is called raw data 
            
            logging.info('Reading completed from mysql database')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
           
            # this rawa data will split into train and test data we will use 
            #scikit learn for this and add it in requirement.txt file and install it
            #add impot train_test_split from sklearn.model_selection above

            #now we will split the data into train and test data
            
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
           
            

            logging.info("Data ingestion is completed successfully")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )



        except Exception as e:
            raise CustomException(e,sys)