from controllers.task_controller import TaskController
from lexicon.lexicon_manager import COMMANDS_LEXICON, EXCEPTION_LEXICON, MESSAGE_LEXICON
from views.view import console


class CommandProcessor:
    def __init__(self, task_controller: TaskController):
        self.task_controller = task_controller
        self.commands = {
            'help': {'method': self.help_command, 'description': COMMANDS_LEXICON['help']},
            'exit': {'method': self.exit_command, 'description': COMMANDS_LEXICON['exit']},
        }

    def process_command(self, command: str) -> None:
        if command in self.commands:
            self.commands[command]['method']()
        else:
            console.print_message(MESSAGE_LEXICON['unknown_command'])

    def help_command(self) -> None:
        console.print_command_info(self.commands)

    def exit_command(self) -> None:
        console.print_exit_command_msg()
        exit()

    def run(self):
        try:
            console.print_welcome_message()
            console.print_command_info(self.commands)
            while True:
                console.print_help_command_info()
                user_input = console.user_input().lower()
                self.process_command(user_input)
        except KeyboardInterrupt:
            console.print_message(MESSAGE_LEXICON['exit_command_msg'])
            exit()