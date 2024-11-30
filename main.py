from config import settings
from controllers.command_processor import CommandProcessor
from controllers.task_controller import TaskController
from lexicon.lexicon_manager import EXCEPTION_LEXICON
from models.task_models import Task
from repository.file_manager import JSONFileManager, BaseFileManager
from services.task_service import TaskService
from views.view import console


def main():
    repository: BaseFileManager = JSONFileManager(model=Task, data_path=settings.data_file_path)
    task_service: TaskService = TaskService(repository=repository)
    task_controller = TaskController(service=task_service)
    processor = CommandProcessor(task_controller)
    processor.run()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        # logger.log_exception(traceback.format_exc())
        console.print_exception_message(EXCEPTION_LEXICON['exception_msg'])
