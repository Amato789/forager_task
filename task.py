import json
from abc import ABC


class Task(ABC):
    url: str
    email: str
    domain: str
    task_name: str

    def start_task(self):
        raise NotImplementedError

    def save_data(self, task_name, data):
        if task_name == 'email_verification':
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
