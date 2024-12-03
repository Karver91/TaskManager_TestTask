from config import settings

__MESSAGE_LEXICON = {
    'add_task_info': 'Для добавления новой задачи вам необходимо указать название задачи, ее описание, '
                     'срок ее выполнения; а так же выбрать категорию задачи и приоритет ее выполнения',
    'add_task_success': 'Задача успешно добавлена',
    'available_commands': 'Доступные команды:',
    'deleted_success': 'Удаление успешно завершено!',
    'edit_task_success': 'Редактирование прошло успешно!',
    'enter_id': 'Введите id задачи',
    'exit_command_msg': 'Программа завершена\n'
                        'До новых встреч!',
    'help_command_info': 'Чтобы увидеть список команд введите "help"',
    'input_msg': 'Ввод',
    'input_task_date': f'Введите дату выполнения задачи в формате {settings.DATETIME_FORMAT}',
    'input_task_description': 'Введите описание',
    'input_task_title': 'Введите название задачи',
    'invalid_command': 'Введена неверная команда. Попробуйте еще раз',
    'main_menu_label': '(Главное меню)',
    'search_by_keyword_info': 'Ключевым словом может быть название задачи, описание, категория, приоритет или статус',
    'select_category': 'Выберете категорию',
    'select_priority': 'Выберете приоритет',
    'select_status': 'Выберете статус',
    'unknown_command': 'Неизвестная команда. Введите "help" для списка команд',
    'welcome_message': 'Добро пожаловать в наш Менеджер задач!\n'
                       'Элементом управления является набор простейших текстовых команд',
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
    'category': 'Категория',
    'cancel': 'Отмена',
    'delete_by_id': 'Удалить задачу по ее ID',
    'delete_completed_tasks': 'Удаление всех завершенных задач',
    'delete_task': 'Удалить задачу',
    'description': 'Описание',
    'due_date': 'Дата выполнения',
    'edit_task': 'Редактировать задачу',
    'exit': 'Выход из приложения',
    'help': 'Выводит список команд на экран',
    'priority': 'Приоритет',
    'search_by_category': 'Поиск задач по категории',
    'search_by_keyword': 'Поиск задач по ключевому слову',
    'search_by_priority': 'Поиск задач по приоритету',
    'search_by_status': 'Поиск задач по статусу выполнения',
    'search_tasks': 'Поиск задач',
    'show_all_tasks': 'Просмотр всех текущих задач',
    'show_tasks': 'Показать задачи',
    'show_tasks_by_category': 'Просмотр задач по категориям',
    'status': 'Статус',
    'title': 'Название',
}

__EXCEPTION_LEXICON = {
    'attr_not_exist': 'Нельзя обращаться к несуществующему атрибуту',
    'exception_msg': 'Ошибка. Программа завершена',
    'models_date_format_not_valid': f'Дата не соответствует формату {settings.DATETIME_FORMAT}',
    'models_date_must_be_less_current': 'Дата выполнения задания не может быть меньше текущей',
    'models_fields_length_not_valid': 'Поля не заполнены',
    'models_id_not_valid': 'ID должен относится к типу int и быть больше нуля',
    'repository_bad_request': 'Неверно переданные данные',
    'repository_id_generated_failed': 'Ошибка генерации id, не найден атрибут id',
    'repository_object_not_found': 'Объект не обнаружен в базе',
    'task_not_found': 'Задач не найдено',
}


def get_lexicon():
    return __COMMANDS_LEXICON, __MESSAGE_LEXICON, __ENUMS_LEXICON, __EXCEPTION_LEXICON
