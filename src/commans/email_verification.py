from src.task_abstract import Task
from src.api_services.hunter_api_service import HunterApiService


class EmailVerification(Task):
    email: str
    task_name = 'email_verification'

    def __init__(self, task_args, storage_service):
        super().__init__(task_args, storage_service)
        self.email = task_args['email']

    def validate_task_argument(self):
        if not self.task_args.get('email'):
            raise Exception('No email was provided')

    def execute(self):
        data = HunterApiService().email_verify(self.email)
        self.storage_service.add_record(data)
