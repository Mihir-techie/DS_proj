import os
import sys
from src.ML_Project.exceptions import CustomException
from src.ML_Project.logger import logging
import pandas as pd
import pymysql
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
db = os.getenv("db")
user = os.getenv("user")
password = os.getenv("password")

def create_sample_data():
    """Create sample data when database is not available"""
    logging.info("Creating sample data as fallback")
    print("📊 Database not available - Creating sample data...")
    sample_data = {
        'math_score': [85, 90, 78, 92, 88, 76, 95, 89, 84, 91],
        'reading_score': [78, 85, 82, 88, 90, 75, 92, 86, 80, 89],
        'writing_score': [82, 88, 80, 90, 85, 78, 94, 87, 83, 92],
        'gender': ['female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male']
    }
    df = pd.DataFrame(sample_data)
    print(f"✅ Created {len(df)} sample records")
    return df

def read_sql_data():
    logging.info("Starting to read data from SQL database")
    
    # Validate environment variables
    if not all([host, db, user, password]):
        logging.warning("Missing database environment variables. Using sample data.")
        print("⚠️  Missing database credentials - Using sample data")
        return create_sample_data()
    
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db,
            connect_timeout=10  # Add timeout to prevent hanging
        )
        logging.info("Database connection established successfully")
        
        # Check if the table exists
        cursor = mydb.cursor()
        cursor.execute("SHOW TABLES LIKE 'students'")
        result = cursor.fetchone()
        cursor.close()
        
        if not result:
            logging.warning("Table 'students' not found. Using sample data.")
            print("⚠️  Table 'students' not found - Using sample data")
            mydb.close()
            return create_sample_data()
        
        df = pd.read_sql("SELECT * FROM students", con=mydb)
        mydb.close()
        
        if df.empty:
            logging.warning("No data found in students table. Using sample data.")
            print("⚠️  No data found in students table - Using sample data")
            return create_sample_data()
            
        logging.info(f"Successfully read {len(df)} records from database")
        print(f"✅ Successfully loaded {len(df)} records from database")
        return df
        
    except pymysql.err.OperationalError as e:
        logging.error(f"MySQL connection error: {e}")
        logging.info("Falling back to sample data")
        print("🔌 MySQL connection failed - Using sample data")
        return create_sample_data()
    except Exception as e:
        logging.error(f"Unexpected error reading from database: {e}")
        logging.info("Falling back to sample data")
        print("❌ Database error occurred - Using sample data")
        return create_sample_data()
