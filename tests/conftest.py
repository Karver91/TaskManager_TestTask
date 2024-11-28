from datetime import datetime

import pytest

from config import settings
from enums import TaskCategoryEnum, TaskStatusEnum
from models.task_models import Task
from repository.file_manager import JSONFileManager


@pytest.fixture
def task_repository(tmp_path):
    """Фикстура для создания тестового JSON-файла."""
    test_file = tmp_path / "test_data.json"
    # test_file = settings.data_file_path
    repository = JSONFileManager(model=Task, data_path=test_file)

    test_data = Task(
        id=1,
        title='test_title',
        description='test_description',
        category=TaskCategoryEnum.PERSONAL.value,
        due_date=datetime.now(),
        status=TaskStatusEnum.NOT_COMPLETED.value
    )

    repository.add_data_obj(test_data)

    yield repository
