from collections import namedtuple

#we are going to pass all required info from yaml file to this config entity
DataIngestionConfig=namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])


DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path","report_file_path","report_page_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig", ["add_bedroom_per_room", # this datatransformationconfig is geiven for feature engineering
                                                                   "transformed_train_dir",
                                                                   "transformed_test_dir",
                                                                   "preprocessed_object_file_path"]) #preprocessed will hav e the pickle file path


ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path","base_accuracy","model_config_file_path"]) #exporting the trained model pickle with this modeltarinerconfig

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path","time_stamp"])  #model eval file is like wea re going to keep info about model eval, model eval file will have info about all the models that are in prod


ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"]) #push the model to prod if its good 

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"]) 