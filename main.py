from config import settings
from models.task_models import Task
from repository.file_manager import JSONFileManager, BaseFileManager


def main():
    repository: BaseFileManager = JSONFileManager(model=Task, data_path=settings.data_file_path)

if __name__ == '__main__':
    main()
