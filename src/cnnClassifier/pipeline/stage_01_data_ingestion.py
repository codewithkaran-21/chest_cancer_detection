from src.cnnClassifier.config.configuration import ConfigurationManager

from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.logger import logger

STAGE_NAMEE = "Data Ingestion Stage"

class DataIngestionTrainingPipeline :
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config  = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__=='__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAMEE} started >>>>>>>>")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAMEE} completed >>>>>>>>")
    except Exception as e:
        raise e