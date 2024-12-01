import random
from datetime import datetime
from unittest.mock import patch

from config import settings
from enums import TaskCategoryEnum, TaskPriorityEnum, TaskStatusEnum
from lexicon.lexicon_manager import MESSAGE_LEXICON
from models.task_models import Task
from views.view import console


class TestTaskController:
    def test_add_task(self, task_controller):
        repository_data = task_controller.service.repository.data
        data_len = len(repository_data)

        date_format = settings.DATETIME_FORMAT
        date = date_format.replace('%Y', '2025').replace('%m', '12').replace('%d', '12')
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

        assert len(repository_data) == data_len + 1, 'Объект не добавлен в память'
        new_obj: Task = repository_data[-1]
        # Проверяем соответствие полям
        assert new_obj.title == console_input['title']
        assert new_obj.description == console_input['description']
        assert new_obj.due_date == datetime.strptime(console_input['due_date'], date_format)
        assert new_obj.category == list(TaskCategoryEnum)[category_input -1].value
        assert new_obj.priority == list(TaskPriorityEnum)[priority_input -1].value
        assert new_obj.status == TaskStatusEnum.NOT_COMPLETED.value
