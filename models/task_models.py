from datetime import datetime

from config import settings
from enums import TaskCategoryEnum, TaskStatusEnum, TaskPriorityEnum
from models.base_model import AbstractModel


class Task(AbstractModel):
    def __init__(
            self,
            id: int,
            title: str,
            description: str,
            category: TaskCategoryEnum,
            due_date: datetime,
            priority: TaskPriorityEnum,
            status: TaskStatusEnum = None
    ):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = TaskStatusEnum.NOT_COMPLETED.value if not status else status

        self.validate()

    def to_dict(self) -> dict:
        return vars(self)

    def validate(self):
        if not isinstance(self.id, int) or self.id < 0:
            raise ValueError("ID должен относится к типу int и быть больше нуля")
        for value in (self.title, self.description, self.category, self.priority, self.due_date, self.status):
            self._validate_len_value(value)
        self._validate_due_date_format()


    def _validate_due_date_format(self):
        try:
            if isinstance(self.due_date, str):
                self.due_date = datetime.strptime(self.due_date, settings.DATETIME_FORMAT)
            if self.due_date < datetime.now():
                raise ValueError('Дата выполнения задания не может быть меньше текущей')
        except ValueError:
            raise ValueError(f'Дата не соответствует формату {settings.DATETIME_FORMAT}')


    @staticmethod
    def _validate_len_value(value):
        if isinstance(value, str) and len(value) < 1:
            raise ValueError('Поля не заполнены')
