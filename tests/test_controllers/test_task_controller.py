import random
from datetime import datetime
from unittest.mock import patch

import pytest

from config import settings
from enums import TaskCategoryEnum, TaskPriorityEnum, TaskStatusEnum
from lexicon.lexicon_manager import MESSAGE_LEXICON, ENUMS_LEXICON
from models.task_models import Task
from tests.conftest import DATE_STR, DATE_OBJ
from views.view import console



class TestTaskController:
    def test_add_task(self, task_controller):
        repository_data = task_controller.service.repository.data
        expected_data_len = len(repository_data) + 1

        date = DATE_STR
        category_input = random.randint(1, len(TaskCategoryEnum))
        priority_input = random.randint(1, len(TaskPriorityEnum))
        console_input = {
            'category': str(category_input),
            'priority': str(priority_input),
            'title': 'some title',
            'description': 'some description',
            'due_date': date
        }
        with patch('builtins.print') as mock_print:
            console.print_message(MESSAGE_LEXICON['add_task_success'])
            expected_result = mock_print.call_args.args[0]

        with patch('builtins.print') as mock_print:
            with patch('builtins.input', side_effect=console_input.values()):
                # Вызываем метод
                task_controller.add_task()
                # Проверяем вывод на экран
                mock_print.assert_any_call(expected_result)

        assert len(repository_data) == expected_data_len, 'Объект не добавлен в память'
        new_obj: Task = repository_data[-1]
        # Проверяем соответствие полям
        assert new_obj.title == console_input['title']
        assert new_obj.description == console_input['description']
        assert new_obj.due_date == DATE_OBJ
        assert new_obj.category == list(TaskCategoryEnum)[category_input - 1].value
        assert new_obj.priority == list(TaskPriorityEnum)[priority_input - 1].value
        assert new_obj.status == TaskStatusEnum.NOT_COMPLETED.value

    @pytest.mark.parametrize('delete_task_command, task_id',
                             [
                                 ('1', 1),
                                 ('2', 2)
                             ])
    def test_remove_task(self, task_controller, delete_task_command, task_id):
        repository_data = task_controller.service.repository.data
        expected_data_len = len(repository_data) - 1
        console_input = {
            'delete_task_command': delete_task_command,
            'task_id': task_id
        }
        task: Task = [task for task in repository_data if task.id == task_id][0]
        task.status = TaskStatusEnum.COMPLETED.value

        with patch('builtins.print') as mock_print:
            console.print_message(MESSAGE_LEXICON['deleted_success'])
            expected_result = mock_print.call_args.args[0]

        with patch('builtins.print') as mock_print:
            with patch('builtins.input', side_effect=console_input.values()):
                # Вызываем метод
                task_controller.remove_task()
                # Проверяем вывод на экран
                mock_print.assert_any_call(expected_result)

        assert len(repository_data) == expected_data_len, 'Объект не удален из базы'

    @pytest.mark.parametrize('edit_field_command, user_input, expected_data, task_attr',
                             [
                                 ('1', 'new title', 'new title', 'title'),
                                 ('2', 'new description', 'new description', 'description'),
                                 ('3', '1', ENUMS_LEXICON['WORK'], 'category'),
                                 ('4', DATE_STR, DATE_OBJ, 'due_date'),
                                 ('5', '1', ENUMS_LEXICON['HIGH'], 'priority'),
                                 ('6', '1', ENUMS_LEXICON['COMPLETED'], 'status')
                             ])
    def test_edit_task(self, task_controller,
                       edit_field_command, user_input, expected_data, task_attr):
        repository_data = task_controller.service.repository.data
        task_id = 1
        console_input = {
            'task_id': str(task_id),
            'edit_field_command': edit_field_command,
            'user_input': user_input
        }
        task: Task = [task for task in repository_data if task.id == task_id][0]

        with patch('builtins.print') as mock_print:
            console.print_message(MESSAGE_LEXICON['edit_task_success'])
            expected_result = mock_print.call_args.args[0]

        with patch('builtins.print') as mock_print:
            with patch('builtins.input', side_effect=console_input.values()):
                # Вызываем метод
                task_controller.edit_task()
                # Проверяем вывод на экран
                mock_print.assert_any_call(expected_result)

        assert getattr(task, task_attr) == expected_data

    def test_show_all_tasks(self, task_controller):
        repository_data = task_controller.service.repository.data
        data_len = len(repository_data)
        console_input = {
            'show_task_command': '1'
        }
        with patch('builtins.print') as mock_print:
            console.print_tasks(repository_data)
            data = mock_print.call_args_list[-data_len:]
            expected_result = [obj.args for obj in data]

        with patch('builtins.print') as mock_print:
            with patch('builtins.input', side_effect=console_input.values()):
                # Вызываем метод
                task_controller.show_tasks()
                # Проверяем вывод на экран
                data = mock_print.call_args_list[-data_len:]
                displayed_result = [obj.args for obj in data]
                assert expected_result == displayed_result

    def test_show_tasks_by_category(self, task_controller):
        category_choice = '2'
        console_input = {
            'show_task_command': '2',
            'category_choice': category_choice
        }

        # Получаем название категории
        with patch('builtins.input', side_effect=[category_choice]):
            category = task_controller.get_category()

        expected_data = [task for task in task_controller.service.repository.data if task.category == category]
        data_len = len(expected_data)

        # Получаем ожидаемый вывод на экран
        with patch('builtins.print') as mock_print:
            console.print_tasks(expected_data)
            data = mock_print.call_args_list[-data_len:]
            expected_result = [obj.args for obj in data]

        with patch('builtins.print') as mock_print:
            with patch('builtins.input', side_effect=console_input.values()):
                # Вызываем метод
                task_controller.show_tasks()
                # Проверяем вывод на экран
                data = mock_print.call_args_list[-data_len:]
                displayed_result = [obj.args for obj in data]
                assert expected_result == displayed_result

    def test_search_tasks_by_keyword(self, task_controller):
        repository_data = task_controller.service.repository.data
        keyword = repository_data[0].description
        console_input = {
            'search_task_command': '1',
            'user_input': keyword
        }
        expected_data = [obj for obj in repository_data if keyword in obj.description]
        data_len = len(expected_data)

        # Получаем ожидаемый вывод на экран
        with patch('builtins.print') as mock_print:
            console.print_tasks(expected_data)
            data = mock_print.call_args_list[-data_len:]
            expected_result = [obj.args for obj in data]

        with patch('builtins.print') as mock_print:
            with patch('builtins.input', side_effect=console_input.values()):
                # Вызываем метод
                task_controller.search_tasks()
                # Проверяем вывод на экран
                data = mock_print.call_args_list[-data_len:]
                displayed_result = [obj.args for obj in data]
                assert expected_result == displayed_result
