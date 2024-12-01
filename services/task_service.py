from enums import TaskStatusEnum
from lexicon.lexicon_manager import MESSAGE_LEXICON
from models.task_models import Task
from repository.file_manager import BaseFileManager


class BaseService:
    def __init__(self, repository: BaseFileManager):
        self.repository = repository

    @staticmethod
    def get_enumerate_commands(values, methods=None, cansel_command: bool = False) -> dict[dict]:
        """Возвращает список команд для изменения статуса"""
        # Создаем вложенный словарь команд, используя генератор словарей
        commands = {str(key): {'description': value, 'method': methods[key - 1] if methods else None}
                    for key, value in enumerate(values, start=1)}
        if cansel_command:
            commands['0'] = {'description': MESSAGE_LEXICON['cancel']}
        return commands

    def get_enumerate_commands_from_enum(self, enum_type, cansel_command: bool = False):
        """Возвращает список команд для объекта enum"""
        values = self.get_enum_values(enum_type)
        commands = self.get_enumerate_commands(values, cansel_command=cansel_command)
        return commands

    def get_enum_values(self, enum_type):
        """Возвращает значения объекта enum"""
        statuses = self.get_all_enum_statuses(enum_type)
        values = [x[1].value for x in statuses]
        return values

    @staticmethod
    def get_all_enum_statuses(enum_type) -> list[tuple]:
        """Возвращает статусы объекта enum"""
        result = list()
        for name, member in enum_type.__members__.items():
            result.append((name, member))
        return result

    def get_obj_by_id(self, obj_id) -> object:
        """Возвращает объект из data по его id"""
        try:
            obj_id = int(obj_id)
            result = None
            for obj in self.repository.data:
                if obj.id == obj_id:
                    result = obj
                    break
            return result
        except ValueError:
            raise ValueError('Неверно переданные данные')


class TaskService(BaseService):
    """Отвечает за обработку бизнес-логики, связанной с моделью Task"""

    def __init__(self, repository: BaseFileManager):
        super().__init__(repository)

    def add_task(self, title, description, due_date, category, priority):
        try:
            task_id = self.repository.generate_id()
            task = Task(
                id=task_id,
                title=title,
                description=description,
                category=category,
                due_date=due_date,
                priority=priority
            )
            self.repository.add_data_obj(task)
            return task
        except ValueError:
            raise

    def get_all_tasks(self):
        return self.repository.data

    def get_tasks_by_task_attr(self, attr, keyword) -> list[Task]:
        try:
            return [task for task in self.repository.data if getattr(task, attr) == keyword]
        except AttributeError:
            raise AttributeError(f'Ошибка: атрибут "{keyword}" не найден')

    def get_tasks_by_task_keyword(self, user_input: str) -> list[Task]:
        """Ищет задачи по их названию, описанию, категории, приоритету и статусу"""
        keywords = user_input.split()
        tasks = [
            task for task in self.repository.data if (
                word.lower() in keywords for word in (
                    task.title,
                    task.description,
                    task.category,
                    task.priority,
                    task.status
                )
            )
        ]
        return tasks

    def remove_task_by_id(self, book_id: str) -> Task:
        """Удаляет задачу по ее id"""
        try:
            task = self.get_obj_by_id(book_id)
            if not task in self.repository.data:
                raise ValueError(MESSAGE_LEXICON['task_not_found'])
            self.repository.remove_data_obj(task)
            return task
        except ValueError:
            raise

    def remove_completed_task(self):
        """Удаляет все завершенные задачи"""
        completed_task = [task for task in self.repository.data if task.status == TaskStatusEnum.COMPLETED.value]
        if not completed_task:
            raise ValueError(MESSAGE_LEXICON['task_not_found'])
        for task in completed_task:
            self.repository.data.remove(task)
        self.repository.write_file()
        return completed_task
