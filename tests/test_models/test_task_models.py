from datetime import datetime

import pytest

from enums import TaskCategoryEnum, TaskStatusEnum, TaskPriorityEnum
from models.task_models import Task


class TestTaskModel:
    def test_to_dict_method(self, task_repository):
        task = task_repository.data[0]
        expected_dict = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'category': task.category,
            'priority': task.priority,
            'due_date': task.due_date,
            'status': task.status
        }

        assert task.to_dict() == expected_dict

    def test_validate_due_date_format(self):
        date_n_time = '3024-11-11'
        task = Task(
            id=1,
            title='test_title',
            description='test_description',
            category=TaskCategoryEnum.PERSONAL.value,
            due_date=date_n_time,
            priority=TaskPriorityEnum.LOW.value,
            status=TaskStatusEnum.NOT_COMPLETED.value
        )

        task._validate_due_date_format()
        assert isinstance(task.due_date, datetime)

    @pytest.mark.parametrize('date_n_time',
                                 [
                                     'some-date',  # Неверный формат даты
                                     '1999-01-01'  # Время меньше текущего
                                 ]
                             )
    def test_validate_due_date_format_exception(self, date_n_time):
        with pytest.raises(ValueError):
            Task(
                id=1,
                title='test_title',
                description='test_description',
                category=TaskCategoryEnum.PERSONAL.value,
                due_date=date_n_time,
                priority=TaskPriorityEnum.LOW.value,
                status=TaskStatusEnum.NOT_COMPLETED.value
            )
            # это законченный тест, исключение вылетает в момент создания модели


    def test_validate_len_value_exceptions(self):
        with pytest.raises(ValueError, match='Поля не заполнены'):
            Task(
                id=1,
                title='',
                description='',
                category=TaskCategoryEnum.PERSONAL.value,
                due_date='',
                priority=TaskPriorityEnum.LOW.value,
                status=TaskStatusEnum.NOT_COMPLETED.value
            )