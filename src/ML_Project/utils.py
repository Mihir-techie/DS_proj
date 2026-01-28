import os
import sys
from src.ML_Project.exceptions import CustomException
from src.ML_Project.logger import logging
import pandas as pd
import numpy as np 
import pymysql
from dataclasses import dataclass

from dotenv import load_dotenv
load_dotenv()

host = os.getenv("host")
db = os.getenv("db")
user = os.getenv("user")
password = os.getenv("password")

def read_sql_data():
    logging.info("Starting to read data from SQL database")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db

        )
        logging.info("Database connection established successfully", mydb)
        df = pd.read_sql("SELECT * FROM students", con=mydb)
        print(df.head())

    except Exception as e:
        raise CustomException(e, sys)
