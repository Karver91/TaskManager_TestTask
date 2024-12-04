from datetime import datetime

import pytest

from config import settings
from controllers.task_controller import TaskController
from enums import TaskCategoryEnum, TaskStatusEnum, TaskPriorityEnum
from models.task_models import Task
from repository.file_manager import JSONFileManager
from services.task_service import TaskService

DATE_FORMAT = settings.DATETIME_FORMAT
DATE_STR = DATE_FORMAT.replace('%Y', '2025').replace('%m', '12').replace('%d', '12')
DATE_OBJ = datetime.strptime(DATE_STR, DATE_FORMAT)


@pytest.fixture
def task_repository(tmp_path):
    """Фикстура для создания тестового JSON-файла."""
    test_file = tmp_path / "test_data.json"
    # test_file = settings.data_file_path
    repository = JSONFileManager(model=Task, data_path=test_file)

    test_data = [
        Task(
            id=1,
            title='test_title',
            description='test_description',
            category=TaskCategoryEnum.PERSONAL.value,
            due_date=DATE_STR,
            priority=TaskPriorityEnum.LOW.value,
            status=TaskStatusEnum.NOT_COMPLETED.value
        ),
        Task(
            id=2,
            title='test_title',
            description='description',
            category=TaskCategoryEnum.EDUCATION.value,
            due_date=DATE_STR,
            priority=TaskPriorityEnum.MEDIUM.value,
            status=TaskStatusEnum.NOT_COMPLETED.value
        )
    ]
    [repository.add_data_obj(obj) for obj in test_data]

    yield repository


@pytest.fixture
def task_service(task_repository):
    service = TaskService(
        repository=task_repository
    )

    yield service


@pytest.fixture
def task_controller(task_service):
    controller = TaskController(
        service=task_service
    )

    yield controller
