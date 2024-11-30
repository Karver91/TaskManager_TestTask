import enum

from lexicon.lexicon_manager import ENUMS_LEXICON


class TaskCategoryEnum(enum.Enum):
    WORK = ENUMS_LEXICON['WORK']
    PERSONAL = ENUMS_LEXICON['PERSONAL']
    EDUCATION = ENUMS_LEXICON['EDUCATION']


class TaskStatusEnum(enum.Enum):
    COMPLETED = ENUMS_LEXICON['COMPLETED']
    NOT_COMPLETED = ENUMS_LEXICON['NOT_COMPLETED']


class TaskPriorityEnum(enum.Enum):
    HIGH = ENUMS_LEXICON['HIGH']
    MEDIUM = ENUMS_LEXICON['MEDIUM']
    LOW = ENUMS_LEXICON['LOW']
