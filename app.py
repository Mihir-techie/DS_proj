from src.ML_Project.logger import logging 
from src.ML_Project.exceptions import CustomException
import sys


if __name__ == "__main__":
    logging.info("Starting the ML project application.")

    try:
        a = 1/0
    except Exception as e:
        logging.info("An error occurred.", exc_info=True)
        raise CustomException(e, sys)
    