import requests
import json
from task import Task


class EmailVerification(Task):
    API_KEY = 'b7a19832219fb4b4f1c1532b821b340945672961'
    task_name = 'email_verification'

    # url = f'https://api.hunter.io/v2/email-verifier?email={object_name}&api_key={API_KEY}'

    def __init__(self, object_name):
        self.object_name = object_name
        self.url = f'https://api.hunter.io/v2/email-verifier?email={self.object_name}&api_key={self.API_KEY}'

    def start_task(self):
        response = self.get_info()
        self.save_data(task_name=self.task_name, data=response)

    def get_info(self):
        res = requests.get(self.url)
        response = json.loads(res.text)["data"]
        return response
