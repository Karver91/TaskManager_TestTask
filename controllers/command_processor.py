from controllers.task_controller import TaskController
from lexicon.lexicon_manager import COMMANDS_LEXICON, MESSAGE_LEXICON
from views.view import console


class CommandProcessor:
    def __init__(self, task_controller: TaskController):
        self.task_controller = task_controller
        self.commands = {
            'help': {'method': self.help_command, 'description': COMMANDS_LEXICON['help']},
            'exit': {'method': self.exit_command, 'description': COMMANDS_LEXICON['exit']},
            '1': {'method': self.task_controller.show_tasks, 'description': COMMANDS_LEXICON['show_tasks']},
            '2': {'method': self.task_controller.search_tasks, 'description': COMMANDS_LEXICON['search_tasks']},
            '3': {'method': self.task_controller.add_task, 'description': COMMANDS_LEXICON['add_task']},
            '4': {'method': self.task_controller.remove_task, 'description': COMMANDS_LEXICON['delete_task']},
            '5': {'method': self.task_controller.edit_task, 'description': COMMANDS_LEXICON['edit_task']},
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
                console.print_main_menu_label()
                user_input = console.user_input().lower()
                self.process_command(user_input)
        except KeyboardInterrupt:
            self.exit_command()
