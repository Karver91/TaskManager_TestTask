import shutil

from lexicon.lexicon_manager import MESSAGE_LEXICON


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

    def print_command_info(self, commands):
        """Выводит доступные команды"""
        self.print_message(MESSAGE_LEXICON['available_commands'])
        for key, value in commands.items():
            print(f'{key} - {value['description']}')

    def print_help_command_info(self):
        self.print_message(MESSAGE_LEXICON['help_command_info'])

    def print_exit_command_msg(self):
        self.print_message(MESSAGE_LEXICON['exit_command_msg'])

    def print_welcome_message(self):
        """Выводит приветственное сообщение"""
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
