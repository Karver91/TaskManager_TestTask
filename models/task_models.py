from datetime import datetime

from config import settings
from enums import TaskCategoryEnum, TaskStatusEnum, TaskPriorityEnum
from lexicon.lexicon_manager import EXCEPTION_LEXICON
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

    def __setattr__(self, key, value):
        if not key in ['id', 'title', 'description', 'category', 'due_date', 'priority', 'status']:
            raise AttributeError(EXCEPTION_LEXICON['attr_not_exist'])
        value = self.validate(key, value)
        super().__setattr__(key, value)

    def __str__(self):
        return f'<ID: {self.id} Title: {self.title}>'

    def __repr__(self):
        return f'<ID: {self.id} Title: {self.title}>'


    def to_dict(self) -> dict:
        return vars(self)

    def validate(self, key, value):
        if key == 'id':
            if not isinstance(value, int) or value < 0:
                raise ValueError(EXCEPTION_LEXICON['models_id_not_valid'])
        elif key in ('title', 'description', 'category', 'priority', 'status'):
            self.__validate_len_value(value)
        elif key == 'due_date':
            self.__validate_len_value(value)
            value = self.__validate_due_date_format(value)
        return value

    @staticmethod
    def __validate_due_date_format(value):
        try:
            if isinstance(value, str):
                value = value.strip()
                value = datetime.strptime(value, settings.DATETIME_FORMAT)
                return value
        except ValueError as e:
            raise ValueError(EXCEPTION_LEXICON['models_date_format_not_valid'])

    @staticmethod
    def __validate_len_value(value):
        if isinstance(value, str) and len(value) < 1:
            raise ValueError(EXCEPTION_LEXICON['models_fields_length_not_valid'])

    # def validate_date_not_less_current(self):
    #     if self.due_date < datetime.now():
    #         raise ValueError(EXCEPTION_LEXICON['models_date_must_be_less_current'])
