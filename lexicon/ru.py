from config import settings

__MESSAGE_LEXICON = {
    'available_commands': 'Доступные команды:',
    'exit_command_msg': 'Программа завершена\n'
                        'До новых встреч!',
    'help_command_info': 'Чтобы увидеть список команд введите "help"',
    'input_msg': 'Ввод',
    'welcome_message': 'Добро пожаловать в наш Менеджер задач!\n'
                       'Элементом управления является набор простейших текстовых команд',
    'unknown_command': 'Неизвестная команда. Введите "help" для списка команд',
    'add_task_info': 'Для добавления новой задачи вам необходимо указать название задачи, ее описание, '
                     'срок ее выполнения; а так же выбрать категорию задачи и приоритет ее выполнения',
    'input_task_title': 'Введите название задачи',
    'input_task_description': 'Введите описание',
    'input_task_date': f'Введите дату выполнения задачи в формате {settings.DATETIME_FORMAT}',
    'add_task_success': 'Задача успешно добавлена',
    'task_not_found': 'Задач не найдено',
    'title': 'Название',
    'description': 'Описание',
    'category': 'Категория',
    'due_date': 'Дата выполнения',
    'priority': 'Приоритет',
    'status': 'Статус',
    'cancel': 'Отмена',
    'select_category': 'Выберете категорию',
    'select_priority': 'Выберете приоритет',
    'select_status': 'Выберете статус',
    'invalid_command': 'Введена неверная команда. Попробуйте еще раз',
    'show_all_tasks': 'Просмотр всех текущих задач',
    'show_tasks_by_category': 'Просмотр задач по категориям',
    'search_by_keyword': 'Поиск задач по ключевому слову',
    'search_by_category': 'Поиск задач по категории',
    'search_by_priority': 'Поиск задач по приоритету',
    'search_by_status': 'Поиск задач по статусу выполнения',
    'search_by_keyword_info': 'Ключевым словом может быть название задачи, описание, категория, приоритет или статус',
    'delete_by_id': 'Удалить задачу по ее ID',
    'deleted_success': 'Удаление успешно завершено!',
    'delete_completed_tasks': 'Удаление всех завершенных задач'
}

__ENUMS_LEXICON = {
    'WORK': 'Работа',
    'PERSONAL': 'Личное',
    'EDUCATION': 'Обучение',
    'COMPLETED': 'Выполнена',
    'NOT_COMPLETED': 'Не выполнена',
    'HIGH': 'Высокий',
    'MEDIUM': 'Средний',
    'LOW': 'Низкий'
}

__COMMANDS_LEXICON = {
    'add_task': 'Добавить задачу',
    'show_tasks': 'Показать задачи',
    'search_tasks': 'Поиск задач',
    'delete_task': 'Удалить задачу',
    'help': 'Выводит список команд на экран',
    'exit': 'Выход из приложения'
}

__EXCEPTION_LEXICON = {
    'exception_msg': 'Ошибка. Программа завершена',
    'models_id_not_valid': 'ID должен относится к типу int и быть больше нуля',
    'models_date_must_be_less_current': 'Дата выполнения задания не может быть меньше текущей',
    'models_date_format_not_valid': f'Дата не соответствует формату {settings.DATETIME_FORMAT}',
    'models_fields_length_not_valid': 'Поля не заполнены',
    'repository_id_generated_failed': 'Ошибка генерации id, не найден атрибут id',
    'repository_object_not_found': 'Объект не обнаружен в базе'
}


def get_lexicon():
    return __COMMANDS_LEXICON, __MESSAGE_LEXICON, __ENUMS_LEXICON, __EXCEPTION_LEXICON
