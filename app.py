import logging
from src.ML_Project.exceptions import CustomException
from src.ML_Project.utils import read_sql_data
from src.ML_Project.components.data_ingestion import DataIngestion
from src.ML_Project.components.data_ingestion import DataIngestionConfig


import sys


if __name__ == "__main__":
    print(" ML Project Application Starting...")
    logging.info("Starting the ML project application.")

    try:
        from src.ML_Project.components.data_ingestion import DataIngestion
        data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed.")
        print(" Application completed successfully!")


       
    except Exception as e:
        logging.info("An error occurred.", exc_info=True)
        print(" Application failed!")
        raise CustomException(e, sys)