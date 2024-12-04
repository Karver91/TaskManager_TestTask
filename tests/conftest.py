import pytest

from controllers.task_controller import TaskController
from enums import TaskCategoryEnum, TaskStatusEnum, TaskPriorityEnum
from models.task_models import Task
from repository.file_manager import JSONFileManager
from services.task_service import TaskService


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
            due_date='3024-10-01',
            priority=TaskPriorityEnum.LOW.value,
            status=TaskStatusEnum.NOT_COMPLETED.value
        ),
        Task(
            id=2,
            title='test_title',
            description='description',
            category=TaskCategoryEnum.EDUCATION.value,
            due_date='3024-10-01',
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
