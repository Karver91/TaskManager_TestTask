from repository.file_manager import BaseFileManager


class BaseService:
    def __init__(self, repository: BaseFileManager):
        self.repository = repository


class TaskService(BaseService):
    """Отвечает за обработку бизнес-логики, связанной с моделью Task"""
    def __init__(self, repository: BaseFileManager):
        super().__init__(repository)
