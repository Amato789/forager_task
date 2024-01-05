from src.task import Task
from services.hunter_api_service import HunterApiService


class EmailVerification(Task):
    email: str
    task_name = 'email_verification'

    def __init__(self, task_args, save_service):
        super().__init__(task_args, save_service)
        self.email = task_args['email']

    def validate_task_argument(self):
        if not self.task_args.get('email'):
            raise Exception('No email was provided')

    def execute(self):
        data = HunterApiService().email_verify(self.email)
        self.save_service.db_add_data(email=data['email'], status=data['status'])
