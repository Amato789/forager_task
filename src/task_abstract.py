from abc import ABC, abstractmethod
from src.storage_service_abstract import StorageService


class Task(ABC):
    task_args: dict
    storage_service: StorageService

    def __init__(self, task_args, storage_service):
        self.task_args = task_args
        self.storage_service = storage_service
        self.validate_task_argument()

    @abstractmethod
    def validate_task_argument(self):
        raise NotImplementedError

    @abstractmethod
    def execute(self):
        raise NotImplementedError
