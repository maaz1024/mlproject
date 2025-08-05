import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #Filename for logging file
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #Path for the log files
os.makedirs(logs_path,exist_ok=True) #This says keep appending even if there exists a file

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# To override the logging functionality
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__=='__main__':
    logging.info("Logging has started")
