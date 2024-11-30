from config import settings

__MESSAGE_LEXICON = {
    'available_commands': 'Available commands:',
    'exit_command_msg': 'The program is complete\n'
                        'See your later!',
    'help_command_info': 'To see a list of commands, type "help"',
    'input_msg': 'Input',
    'welcome_message': 'Welcome to our Task Manager!\n'
                       'The control element is a set of simple text commands',
    'unknown command': 'Unknown command. Type "help" for a list of commands'
}

__COMMANDS_LEXICON = {
    'help': 'Displays a list of commands on the screen',
    'exit': 'Exit the application'
}

__EXCEPTION_LEXICON = {
    'exception_msg': 'Error. Program terminated',
    'models_date_format_not_valid': f'Date does not match the format {settings.DATETIME_FORMAT}',
    'models_date_must_be_less_current': 'The task due date cannot be less than the current date',
    'models_fields_length_not_valid': 'Fields are not filled',
    'models_id_not_valid': 'ID must be of type int and greater than zero',
    'repository_id_generated_failed': 'Error generating id, id attribute not found',
    'repository_object_not_found': 'Object not found in the database'
}


def get_lexicon():
    return __COMMANDS_LEXICON, __MESSAGE_LEXICON, __EXCEPTION_LEXICON

