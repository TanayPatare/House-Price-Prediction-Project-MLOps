from collections import namedtuple

#Entity_1
DataIngestionConfig = namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])
DataIngestionConfig = namedtuple("DataIngestionConfig", ["schema_file_path"])
# 1.dataset_download_url has url of dataset.
# 2.tgz_download_dir contains rar file of dataset.
# 3.raw_data_dir conatins extracted dataset.
# 4.ingested_train_dir is train dataset.
# 5.ingested_test_dir is test dataset.

#Entity_2
DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path"])

#Entity_3
DataTransformationConfig = namedtuple("DataTransformationConfig",
["add_bedroom_per_room", "transformed_train_dir", "transformed_test_dir", "preprocessed_object_file_path"])

#Entity_4
ModelTrainerConfig = namedtuple("ModelTrainingConfig",
["trained_model_file_path", "base_accuracy"])
# 1.trained_model_file_path is pickle file location.
# 2.base_accuracy is accuracy of older ML model.

#Entity_5
ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",
["model_evaluation_file_path", "time_stamp"])
# 1.model_evaluation_file_path is file loaction which has all info of older models.
# 2.time_stamp has time of file saved.

#entity_6
ModelPusherConfig = namedtuple("ModelPusherConfig",
["export_dir_path"])
# 1.if the new model has better accuracy than base accuracy then export_dir_path holds path for that model for replacement of older model.

#Entity_7
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])