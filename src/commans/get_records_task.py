from src.task_abstract import Task


class GetRecordTask(Task):
    email: str
    task_name = 'get_records'

    def __init__(self, task_args, storage_service):
        super().__init__(task_args, storage_service)
        self.email = task_args['email']

    def validate_task_argument(self):
        if not self.task_args.get('email'):
            raise Exception('No email was provided')

    def execute(self):
        self.storage_service.get_record(self.email)
