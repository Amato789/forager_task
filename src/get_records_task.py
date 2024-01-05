from src.task import Task


class GetRecordsTask(Task):
    email: str
    task_name = 'get_records'

    def __init__(self, task_args, save_service):
        super().__init__(task_args, save_service)
        self.email = task_args['email']

    def validate_task_argument(self):
        if not self.task_args.get('email'):
            raise Exception('No email was provided')

    def execute(self):
        self.save_service.get_record()
