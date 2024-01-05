import json
from abc import ABC, abstractmethod
from services.save_service import SaveService


class Task(ABC):
    task_args: dict
    save_service: SaveService

    def __init__(self, task_args, save_service):
        self.task_args = task_args
        self.save_service = save_service
        self.validate_task_argument()

    @abstractmethod
    def validate_task_argument(self):
        raise NotImplementedError

    @abstractmethod
    def execute(self):
        raise NotImplementedError
