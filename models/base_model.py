from abc import ABC, abstractmethod


class AbstractModel(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def validate(self, name, value):
        raise NotImplementedError
