from services.task_service import TaskService


class TaskController:
    """Обрабатывает команды, связанные с книгами"""
    def __init__(self, service: TaskService):
        self.service = service
