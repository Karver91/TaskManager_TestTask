import os


class Settings:
    DATETIME_FORMAT = '%Y-%m-%d'
    LANGUAGE = 'en'  # 'ru', 'en'
    __DATA_DIR_NAME = 'data'
    __DATA_FILE_NAME = 'data.json'

    @property
    def data_file_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir_path = os.path.join(current_dir, self.__DATA_DIR_NAME)
        if not os.path.exists(data_dir_path):
            os.makedirs(data_dir_path)
        return os.path.join(data_dir_path, self.__DATA_FILE_NAME)


settings = Settings()
