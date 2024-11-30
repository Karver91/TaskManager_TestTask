from lexicon.lexicon_manager import MESSAGE_LEXICON
from models.task_models import Task
from repository.file_manager import BaseFileManager


class BaseService:
    def __init__(self, repository: BaseFileManager):
        self.repository = repository

    def get_status_commands(self, enum_obj, cansel_command: bool = False) -> dict[dict]:
        """Возвращает список команд для изменения статуса"""
        statuses = self.get_all_enum_statuses(enum_obj)
        status_values = [x[1].value for x in statuses]
        commands = {str(key): {'description': value} for key, value in enumerate(status_values, start=1)}
        if cansel_command:
            commands['0'] = {'description': MESSAGE_LEXICON['cancel']}
        return commands

    @staticmethod
    def get_all_enum_statuses(enum_obj) -> list[tuple]:
        """Возвращает статусы объекта enum"""
        result = list()
        for name, member in enum_obj.__members__.items():
            result.append((name, member))
        return result


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
