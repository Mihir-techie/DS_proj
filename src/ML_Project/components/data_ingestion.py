## Data Ingestion module 
## This module is responsible for loading and preprocessing the dataset.
import os
import sys
from src.ML_Project.exceptions import CustomException
from src.ML_Project.logger import logging
import pandas as pd
import numpy as np 
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.ML_Project.utils import read_sql_data




@dataclass 
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str  = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        logging.info("Entered the data ingestion method or component")
        print("🚀 Starting data ingestion process...")
        try:
            df = read_sql_data()
            logging.info("Read the dataset as dataframe")
            print(f"📋 Dataset loaded with shape: {df.shape}")

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_data_path, index=False, header=True)
            print(f"💾 Raw data saved to: {self.data_ingestion_config.raw_data_path}")

            logging.info("Train test split initiated")
            print("🔄 Splitting data into train and test sets...")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.data_ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path, index=False, header=True)
            
            print(f"📊 Train data saved: {len(train_set)} records -> {self.data_ingestion_config.train_data_path}")
            print(f"📊 Test data saved: {len(test_set)} records -> {self.data_ingestion_config.test_data_path}")

            logging.info("Ingestion of the data is completed")
            print("✅ Data ingestion completed successfully!")

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path,
                self.data_ingestion_config.raw_data_path

            )

        except Exception as e:
            raise CustomException(e, sys)