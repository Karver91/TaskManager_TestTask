import csv
import json
from abc import ABC, abstractmethod
from datetime import date

from config import settings
from lexicon.lexicon_manager import EXCEPTION_LEXICON


class BaseFileManager(ABC):
    """Базовый класс для работы с файлом данных"""

    def __init__(self, model, data_path):
        self.model = model
        self.data_path = data_path
        self.data = self.read_file()

    @abstractmethod
    def read_file(self) -> list:
        """Читает файл. Возвращает список объектов модели"""
        raise NotImplementedError

    @abstractmethod
    def write_file(self) -> None:
        """Записывает данные в файл"""
        raise NotImplementedError

    def generate_id(self) -> int:
        """Генерирует новый id"""
        try:
            _id = 1
            if self.data:
                _id = max([item.id for item in self.data]) + 1
            return _id
        except AttributeError:
            raise AttributeError(EXCEPTION_LEXICON['repository_id_generated_failed'])

    def add_data_obj(self, obj):
        self.data.append(obj)
        self.write_file()

    def remove_data_obj(self, obj):
        try:
            self.data.remove(obj)
            self.write_file()
        except ValueError:
            raise ValueError(EXCEPTION_LEXICON['repository_object_not_found'])


class DatetimeJSONEncoder(json.JSONEncoder):
    """Кастомный энкодер. Переводит объект datetime в строку переданного формата"""

    def default(self, o):
        if isinstance(o, date):
            return o.strftime(settings.DATETIME_FORMAT)  # Преобразуем в строку переданного фората
        return super().default(o)


class JSONFileManager(BaseFileManager):
    """Отвечает за работу с JSON-файлом данных"""

    def __init__(self, model, data_path):
        super().__init__(model, data_path)

    def read_file(self) -> list:
        """Читает файл. Возвращает список объектов модели"""
        try:
            with open(self.data_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [self.model(**item) for item in data]
        except FileNotFoundError:
            return []

    def write_file(self) -> None:
        """Записывает данные в файл"""
        items = [item.to_dict() for item in self.data]
        with open(self.data_path, 'w', encoding='utf-8') as file:
            json.dump(obj=items, fp=file, ensure_ascii=False, indent=4, cls=DatetimeJSONEncoder)


class CSVFileManager(BaseFileManager):
    """Отвечает за работу с CSV-файлом данных"""

    def __init__(self, model, data_path):
        super().__init__(model, data_path)

    def read_file(self) -> list:
        """Читает файл. Возвращает список объектов модели"""
        try:
            with open(self.data_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return [self.model(**item) for item in reader]
        except FileNotFoundError:
            return []


    def write_file(self) -> None:
        try:
            items = [item.to_dict() for item in self.data]
            with open(self.data_path, 'w', encoding='utf-8') as file:
                fieldnames = items[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for item in items:
                    writer.writerow(item)
        except IndexError:
            raise
