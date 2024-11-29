import enum


class TaskCategoryEnum(enum.Enum):
    WORK = 'Работа'
    PERSONAL = 'Личное'
    EDUCATION = 'Обучение'


class TaskStatusEnum(enum.Enum):
    COMPLETED = 'Выполнена'
    NOT_COMPLETED = 'Не выполнена'


class TaskPriorityEnum(enum.Enum):
    HIGH = 'высокий'
    MEDIUM = 'средний'
    LOW = 'низкий'
