from config import settings

__MESSAGE_LEXICON = {
    'available_commands': 'Available commands:',
    'exit_command_msg': 'The program is complete\n'
                        'See your later!',
    'help_command_info': 'To see a list of commands, type "help"',
    'input_msg': 'Input',
    'welcome_message': 'Welcome to our Task Manager!\n'
                       'The control element is a set of simple text commands',
    'unknown command': 'Unknown command. Type "help" for a list of commands',
    'add_task_info': 'To add a new task, you need to specify the task name, its description, '
                     'the deadline for its completion; and also select the task category '
                     'and the priority of its completion',
    'input_task_title': 'Enter the task name',
    'input_task_description': 'Enter the task description',
    'input_task_date': f'Enter the task completion date in the format {settings.DATETIME_FORMAT}',
    'add_task_success': 'Task added successfully',
    'task_not_found': 'No tasks found',
    'title': 'Title',
    'description': 'Description',
    'category': 'Category',
    'due_date': 'Completion date',
    'priority': 'Priority',
    'status': 'Status',
    'cancel': 'Cancel',
    'select_category': 'Select category',
    'select_priority': 'Select priority',
    'select_status': 'Select status',
    'invalid_command': 'Invalid command entered. Try again',
    'show_all_tasks': 'View all current tasks',
    'show_tasks_by_category': 'View tasks by category',
    'search_by_keyword': 'Search for a task by keyword',
    'search_by_category': 'Search tasks by category',
    'search_by_priority': 'Search tasks by priority',
    'search_by_status': 'Search tasks by completion status',
    'search_by_keyword_info': 'The keyword can be the task name, description, category, priority, or status',
    'delete_by_id': 'Delete task by its ID',
    'deleted_success': 'The deletion has been completed successfully!',
    'delete_completed_tasks': 'Delete all completed tasks'
}

__ENUMS_LEXICON = {
    'WORK': 'Work',
    'PERSONAL': 'Personal',
    'EDUCATION': 'Education',
    'COMPLETED': 'Completed',
    'NOT_COMPLETED': 'Not Completed',
    'HIGH': 'High',
    'MEDIUM': 'Medium',
    'LOW': 'Low'
}

__COMMANDS_LEXICON = {
    'add_task': 'Add task',
    'show_tasks': 'Show tasks',
    'search_tasks': 'Search for tasks',
    'delete_task': 'Delete task',
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
    return __COMMANDS_LEXICON, __MESSAGE_LEXICON, __ENUMS_LEXICON, __EXCEPTION_LEXICON
