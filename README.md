# TaskManager_TestTask
Тестовое задание: Разработка консольного приложения "Менеджер задач"

## Структура проекта
'''
TaskManager_TestTask/
    ├── controllers/
        ├── command_processor.py      # Принимает команды, вызывает контроллеры
        └── task_controller.py        # Контроллеры задач
    ├── data/                         # Хранит файлы данных
    ├── lexicon/                      # Отвечает за работу с языками
    ├── models/
        ├── base_model.py             # Абстрактный класс. Базовая модель
        └── task_models.py            # Отвечает за модели задач и их валидацию
    ├── repository/
        └── file_manager.py           # Отвечает за методы работы с файлами данных
    ├── services/
        └── task_service.py           # Службы работы с задачами. Отвечают за обработку бизнес-логики
    ├── tests/
    ├── views/
        └── view.py                   # Отвечает за шаблоны отображаемой пользователю информации
    ├── config.py
    ├── enums.py
    └── main.py
    '''
