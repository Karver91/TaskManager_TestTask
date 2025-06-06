# TaskManager_TestTask
Разработка консольного приложения "Менеджер задач"

В основу проекта лег архитекутрный шаблон mvc с разделением логики на слои, что позволяет легко расширять и модифицировать функционал программы

Программа поддерживает мультиязычность. Это позволяет проекту адаптироваться к различным языковым требованиям без значительных изменений в коде. Изменить язык работы можно в config.py

Репозиторий построен на базе абстрактного базового класса, который задает интерфейс для работы с файлами данных; это позволяет расширить его функционал при необходимости работой с файлами формата CSV или любыми другими.

### Функционал приложения реализован полностью
#### Программа позволяет:
- Добавлять новую задачу
- Удалять задачу 
- Редактировать задачу
- Просматривать задачи
- Искать задачу

## Структура проекта
```
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
```
## Тестовое задание

Тестовое задание: Разработка консольного приложения "Менеджер задач"

**Цель:**
Создать приложение для управления списком задач с возможностью добавления,
выполнения, удаления и поиска задач.

### Основные возможности:
1. **Просмотр задач:**
- Просмотр всех текущих задач.
- Просмотр задач по категориям (например, работа, личное, обучение).
2. **Добавление задачи:**
- Добавление новой задачи с указанием названия, описания, категории, срока
выполнения и приоритета (низкий, средний, высокий).
3. **Изменение задачи:**
- Редактирование существующей задачи.
- Отметка задачи как выполненной.
4. **Удаление задачи:**
- Удаление задачи по идентификатору или категории.
5. **Поиск задач:**
- Поиск по ключевым словам, категории или статусу выполнения.

### Требования к программе:
1. **Интерфейс:**
- Приложение должно работать через консоль (CLI), без использования веб-
или графических интерфейсов (без использования фреймворков по типу
Django, Flask и тд).
2. **Хранение данных:**
- Данные должны сохраняться в формате JSON или CSV.
- Каждая задача должна иметь уникальный идентификатор.
3. **Информация о задаче:**
- Поля задачи: название, описание, категория, срок выполнения, приоритет,
статус (выполнена/не выполнена).

#### Дополнительные требования:
1. **Тестирование:**
- Написать тесты с использованием pytest для проверки функций добавления,
выполнения, поиска и удаления задач.
2. **Обработка ошибок:**
- Программа должна обрабатывать невалидные данные (например,
неправильные даты или пустые поля).

### Оценка:
1. **Архитектура и структура данных:**
- Правильное использование структур данных (списки, словари).
- Организация кода по функциям или классам.
2. **Качество кода:**
- Читаемость и стиль кода (соответствие PEP8).
- Наличие комментариев и типизация.
3. **Объектно-ориентированный подход:**
- Разделение логики на классы (например, Task, TaskManager).
4. **Покрытие тестами:**
- Наличие и качество тестов, покрывающих основные функции.
