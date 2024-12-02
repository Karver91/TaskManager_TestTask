import shutil

from config import settings
from lexicon.lexicon_manager import MESSAGE_LEXICON
from models.task_models import Task


class ConsoleView:
    """Отвечает за формат вывода данных"""

    @staticmethod
    def print_message(message: str):
        """Выводит сообщение в консоль"""
        print(f'\n{message}')

    def print_exception_message(self, message: str):
        """Выводит сообщение об ошибке"""
        terminal_width = self.__get_terminal_width()

        msg_format = f'!!!{message}!!!'
        msg_len = len(msg_format)
        separator = '-'

        len_separator = msg_len if msg_len < terminal_width else terminal_width
        print(f'\n{separator * len_separator}\n{msg_format}\n{separator * len_separator}')

    def print_task_info(self, task: Task):
        """Выводит информацию о задаче"""
        print(
            f"{task.id:<5} "
            f"{task.title:<30} "
            f"{task.category:<15} "
            f"{task.priority:<15} "
            f"{task.status:<15} "
            f"{task.due_date.strftime(settings.DATETIME_FORMAT):<15}"
        )

    @staticmethod
    def print_task_info_detail(task: Task):
        """Выводит подробную информацию о задаче"""
        print(
            f"\nID: {task.id}\n"
            f"{MESSAGE_LEXICON['title']}: {task.title}\n"
            f"{MESSAGE_LEXICON['description']}: {task.description}\n"
            f"{MESSAGE_LEXICON['category']}: {task.category}\n"
            f"{MESSAGE_LEXICON['due_date']}: {task.due_date.date()}\n"
            f"{MESSAGE_LEXICON['priority']}: {task.priority}\n"
            f"{MESSAGE_LEXICON['status']}: {task.status}"
        )

    def print_task_not_found(self):
        """Выводит сообщение, если задача не найдена"""
        self.print_message(MESSAGE_LEXICON['task_not_found'])


    def print_message_with_task_info(self, task, msg):
        """Выводит переданное сообщение и информацию о таске"""
        if not task:
            self.print_task_not_found()
            return
        self.print_message(msg)
        self.print_task_info_detail(task)

    def print_tasks(self, tasks: list[Task]):
        """Выводит список задач"""
        if not tasks:
            self.print_task_not_found()
            return
        print(f"\n"
              f"{'ID':<5} "
              f"{MESSAGE_LEXICON['title']:<30} "
              f"{MESSAGE_LEXICON['category']:<15} "
              f"{MESSAGE_LEXICON['priority']:<15} "
              f"{MESSAGE_LEXICON['status']:<15} "
              f"{MESSAGE_LEXICON['due_date']:<15}")
        for task in tasks:
            self.print_task_info(task)

    def print_command_info(self, commands, title_msg: str = None):
        """Выводит доступные команды"""
        if not title_msg:
            title_msg = MESSAGE_LEXICON['available_commands']
        self.print_message(title_msg)
        for key, value in commands.items():
            print(f'{key} - {value['description']}')

    def print_help_command_info(self):
        self.print_message(MESSAGE_LEXICON['help_command_info'])

    def print_exit_command_msg(self):
        self.print_message(MESSAGE_LEXICON['exit_command_msg'])

    def print_welcome_message(self):
        self.print_message(MESSAGE_LEXICON['welcome_message'])

    @staticmethod
    def user_input(msg: str = MESSAGE_LEXICON['input_msg']):
        msg_format = f'{msg}: '
        return input(msg_format)

    @staticmethod
    def __get_terminal_width():
        """Получаем ширину терминала"""
        try:
            terminal_width = shutil.get_terminal_size().columns
        except OSError:
            terminal_width = 0
        return terminal_width


console = ConsoleView()
