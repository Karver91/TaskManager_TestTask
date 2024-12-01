from enum import EnumType

from enums import TaskCategoryEnum, TaskPriorityEnum
from lexicon.lexicon_manager import MESSAGE_LEXICON
from services.task_service import TaskService
from views.view import console


class TaskController:
    """Обрабатывает команды, связанные с тасками"""

    def __init__(self, service: TaskService):
        self.service = service

    def add_task(self) -> None:
        """Добавление новой таски"""
        try:
            console.print_message(MESSAGE_LEXICON['add_task_info'])
            category = self.get_category()
            priority = self.get_priority()
            title, description, due_date = [
                console.user_input(msg) for msg in (
                    MESSAGE_LEXICON['input_task_title'],
                    MESSAGE_LEXICON['input_task_description'],
                    MESSAGE_LEXICON['input_task_date'],
                )
            ]
            task = self.service.add_task(title, description, due_date, category, priority)
            console.print_message_with_task_info(task, MESSAGE_LEXICON['add_task_success'])
        except ValueError as e:
            console.print_exception_message(e)
            # logger.log_exception(traceback.format_exc())

    def get_category(self) -> str:
        """Предлагает пользователю выбрать категорию таски"""
        commands = self.service.get_enumerate_commands_from_enum(TaskCategoryEnum)
        return self.get_user_choice_from_commands(
            commands, f'{MESSAGE_LEXICON['select_category']}:'
        )

    def get_priority(self):
        """Предлагает пользователю выбрать приоритет таски"""
        commands = self.service.get_enumerate_commands_from_enum(TaskPriorityEnum)
        return self.get_user_choice_from_commands(
            commands, f'{MESSAGE_LEXICON['select_priority']}:'
        )

    def get_user_choice_from_commands(self, commands: dict[dict], title_msg: str) -> str:
        """Возвращает значение, которое выбрал пользователь из списка команд"""
        console.print_command_info(commands, title_msg=title_msg)
        user_input = self.user_input_command(commands)
        status = commands[user_input]['description']
        return status

    @staticmethod
    def user_input_command(commands):
        """Просит пользователя ввести команду из списка команд"""
        while True:
            user_input = console.user_input()
            if not user_input in commands.keys():
                console.print_message(MESSAGE_LEXICON['invalid_command'])
                continue
            break
        return user_input
