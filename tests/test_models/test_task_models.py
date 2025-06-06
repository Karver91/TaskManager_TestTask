from datetime import datetime, date

import pytest

from enums import TaskCategoryEnum, TaskStatusEnum, TaskPriorityEnum
from lexicon.lexicon_manager import EXCEPTION_LEXICON
from models.task_models import Task
from tests.conftest import DATE_STR


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
        _date = DATE_STR
        task = Task(
            id=1,
            title='test_title',
            description='test_description',
            category=TaskCategoryEnum.PERSONAL.value,
            due_date=_date,
            priority=TaskPriorityEnum.LOW.value,
            status=TaskStatusEnum.NOT_COMPLETED.value
        )
        assert isinstance(task.due_date, date)

    @pytest.mark.parametrize('date_n_time, expected_error_message',
                                 [
                                     ('some-date', EXCEPTION_LEXICON['models_date_format_not_valid']),
                                     # ('1999-01-01', EXCEPTION_LEXICON['models_date_must_be_less_current'])
                                 ]
                             )
    def test_validate_due_date_format_exception(self, date_n_time, expected_error_message):
        with pytest.raises(ValueError, match=expected_error_message):
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
        with pytest.raises(ValueError, match=EXCEPTION_LEXICON['models_fields_length_not_valid']):
            Task(
                id=1,
                title='',
                description='',
                category=TaskCategoryEnum.PERSONAL.value,
                due_date='',
                priority=TaskPriorityEnum.LOW.value,
                status=TaskStatusEnum.NOT_COMPLETED.value
            )