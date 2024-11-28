from datetime import datetime

from enums import TaskCategoryEnum, TaskStatusEnum
from models.base_model import AbstractModel


class Task(AbstractModel):
    def __init__(
            self,
            id: int,
            title: str,
            description: str,
            category: TaskCategoryEnum,
            due_date: datetime = None,
            status: TaskStatusEnum = None
    ):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.status = TaskStatusEnum.NOT_COMPLETED.value if not status else status

        self.validate()

    def to_dict(self) -> dict:
        return vars(self)

    def validate(self):
        pass
