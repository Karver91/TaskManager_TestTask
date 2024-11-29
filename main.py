from config import settings
from controllers.command_processor import CommandProcessor
from controllers.task_controller import TaskController
from models.task_models import Task
from repository.file_manager import JSONFileManager, BaseFileManager
from services.task_service import TaskService


def main():
    repository: BaseFileManager = JSONFileManager(model=Task, data_path=settings.data_file_path)
    task_service: TaskService = TaskService(repository=repository)
    task_controller = TaskController(service=task_service)
    processor = CommandProcessor(task_controller)
    processor.run()

if __name__ == '__main__':
    main()
