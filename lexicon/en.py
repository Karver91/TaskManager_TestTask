from config import settings

__MESSAGE_LEXICON = {
    'add_task_info': 'To add a new task, you need to specify the task name, its description, '
                     'the deadline for its completion; and also select the task category '
                     'and the priority of its completion',
    'add_task_success': 'Task added successfully',
    'available_commands': 'Available commands:',
    'deleted_success': 'The deletion has been completed successfully!',
    'edit_task_success': 'Editing was successful!',
    'enter_id': 'Enter task id',
    'exit_command_msg': 'The program is complete\n'
                        'See your later!',
    'help_command_info': 'To see a list of commands, type "help"',
    'input_msg': 'Input',
    'input_task_date': f'Enter the task completion date in the format {settings.DATETIME_FORMAT}',
    'input_task_description': 'Enter the task description',
    'input_task_title': 'Enter the task name',
    'invalid_command': 'Invalid command entered. Try again',
    'main_menu_label': '(Main menu)',
    'search_by_keyword_info': 'The keyword can be the task name, description, category, priority, or status',
    'select_category': 'Select category',
    'select_priority': 'Select priority',
    'select_status': 'Select status',
    'unknown command': 'Unknown command. Type "help" for a list of commands',
    'welcome_message': 'Welcome to our Task Manager!\n'
                       'The control element is a set of simple text commands',
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
    'cancel': 'Cancel',
    'category': 'Category',
    'delete_by_id': 'Delete task by its ID',
    'delete_completed_tasks': 'Delete all completed tasks',
    'delete_task': 'Delete task',
    'description': 'Description',
    'due_date': 'Completion date',
    'edit_task': 'Edit Task',
    'exit': 'Exit the application',
    'help': 'Displays a list of commands on the screen',
    'priority': 'Priority',
    'search_by_category': 'Search tasks by category',
    'search_by_keyword': 'Search for a task by keyword',
    'search_by_priority': 'Search tasks by priority',
    'search_by_status': 'Search tasks by completion status',
    'search_tasks': 'Search for tasks',
    'show_all_tasks': 'View all current tasks',
    'show_tasks': 'Show tasks',
    'show_tasks_by_category': 'View tasks by category',
    'status': 'Status',
    'title': 'Title',
}

__EXCEPTION_LEXICON = {
    'attr_not_exist': 'You cannot access a non-existent attribute',
    'exception_msg': 'Error. Program terminated',
    'models_date_format_not_valid': f'Date does not match the format {settings.DATETIME_FORMAT}',
    'models_date_must_be_less_current': 'The task due date cannot be less than the current date',
    'models_fields_length_not_valid': 'Fields are not filled',
    'models_id_not_valid': 'ID must be of type int and greater than zero',
    'repository_bad_request': 'Incorrectly transmitted data',
    'repository_id_generated_failed': 'Error generating id, id attribute not found',
    'repository_object_not_found': 'Object not found in the database',
    'task_not_found': 'No tasks found',
}


def get_lexicon():
    return __COMMANDS_LEXICON, __MESSAGE_LEXICON, __ENUMS_LEXICON, __EXCEPTION_LEXICON
