from enums import TaskCategoryEnum, TaskPriorityEnum, TaskStatusEnum
from lexicon.lexicon_manager import MESSAGE_LEXICON
from models.task_models import Task
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

    def remove_task(self) -> None:
        """Удаление таски"""
        try:
            command_values = [
                (MESSAGE_LEXICON['delete_by_id'], self.remove_task_by_id),
                (MESSAGE_LEXICON['delete_completed_tasks'], self.service.remove_completed_task)
            ]
            descriptions, methods = zip(*command_values)
            commands = self.service.get_enumerate_commands(descriptions, methods)
            selected_command = self.get_user_choice_from_commands(commands)
            tasks = selected_command['method']()
            console.print_message(MESSAGE_LEXICON['deleted_success'])
        except ValueError as e:
            console.print_exception_message(e)
            # logger.log_exception(traceback.format_exc())

    def show_tasks(self):
        """Отвечает за просмотр задач пользователем"""
        try:
            command_values = [
                (MESSAGE_LEXICON['show_all_tasks'], self.service.get_all_tasks),
                 (MESSAGE_LEXICON['show_tasks_by_category'], self.get_tasks_by_category)
            ]
            descriptions, methods = zip(*command_values)
            commands = self.service.get_enumerate_commands(descriptions, methods)
            selected_command = self.get_user_choice_from_commands(commands)
            tasks = selected_command['method']()
            console.print_tasks(tasks)
        except ValueError as e:
            console.print_exception_message(e)
            # logger.log_exception(traceback.format_exc())

    def search_tasks(self):
        """Отвечает за поиск задач пользователем"""
        try:
            command_values = [
                (MESSAGE_LEXICON['search_by_keyword'], self.get_tasks_by_keyword),
                (MESSAGE_LEXICON['search_by_category'], self.get_tasks_by_category),
                (MESSAGE_LEXICON['search_by_priority'], self.get_tasks_by_priority),
                (MESSAGE_LEXICON['search_by_status'], self.get_task_by_status)
            ]
            descriptions, methods = zip(*command_values)
            commands = self.service.get_enumerate_commands(descriptions, methods)
            selected_command = self.get_user_choice_from_commands(commands)
            tasks = selected_command['method']()
            console.print_tasks(tasks)
        except ValueError as e:
            console.print_exception_message(e)
            # logger.log_exception(traceback.format_exc())

    def get_tasks_by_keyword(self):
        """Возвращает задачи по ключевому слову"""
        console.print_message(MESSAGE_LEXICON['search_by_keyword_info'])
        user_input = console.user_input()
        return self.service.get_tasks_by_task_keyword(user_input)

    def get_tasks_by_category(self):
        """Возвращает задачи по категориям"""
        selected_category = self.get_category()
        return self.service.get_tasks_by_task_attr(attr='category', keyword=selected_category)

    def get_tasks_by_priority(self):
        """Возвращает задачи по приоритету"""
        selected_category = self.get_priority()
        return self.service.get_tasks_by_task_attr(attr='priority', keyword=selected_category)

    def get_task_by_status(self):
        """Возвращает задачи по статусу"""
        selected_category = self.get_status()
        return self.service.get_tasks_by_task_attr(attr='status', keyword=selected_category)

    def get_category(self) -> str:
        """Предлагает пользователю выбрать категорию таски"""
        commands = self.service.get_enumerate_commands_from_enum(TaskCategoryEnum)
        selected_command =  self.get_user_choice_from_commands(
            commands, f'{MESSAGE_LEXICON['select_category']}:'
        )
        return selected_command['description']

    def get_priority(self):
        """Предлагает пользователю выбрать приоритет таски"""
        commands = self.service.get_enumerate_commands_from_enum(TaskPriorityEnum)
        selected_command = self.get_user_choice_from_commands(
            commands, f'{MESSAGE_LEXICON['select_priority']}:'
        )
        return selected_command['description']

    def get_status(self):
        """Предлагает пользователю выбрать статус таски"""
        commands = self.service.get_enumerate_commands_from_enum(TaskStatusEnum)
        selected_command = self.get_user_choice_from_commands(
            commands, f'{MESSAGE_LEXICON['select_status']}:'
        )
        return selected_command['description']

    def get_user_choice_from_commands(self, commands: dict[dict], title_msg: str = None) -> dict[dict]:
        """Возвращает значение, которое выбрал пользователь из списка команд"""
        console.print_command_info(commands, title_msg=title_msg)
        user_input = self.user_input_command(commands)
        selected_command = commands[user_input]
        return selected_command

    def remove_task_by_id(self) -> Task:
        """Вызывает удаление задачи по ее id"""
        try:
            user_input = console.user_input()
            return self.service.remove_task_by_id(user_input)
        except ValueError:
            raise

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
