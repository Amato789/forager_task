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

    def save_data(self, data):
        new_data = {'email': data['email'], 'data': data}
        try:
            with open('data/email_validation.json', encoding='utf8') as file_email_verification:
                data_from_file = json.load(file_email_verification)
                data_from_file.append(new_data)
            with open('data/email_validation.json', 'w', encoding='utf8') as outfile:
                json.dump(data_from_file, outfile, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            with open('data/email_validation.json', 'w', encoding='utf8') as new_file:
                json.dump([new_data], new_file, indent=4, ensure_ascii=False)
