from src.task_abstract import Task
from src.api_services.hunter_api_service import HunterApiService


class DomainSearch(Task):
    domain: str
    task_name = 'domain_search'

    def __init__(self, task_args, storage_service):
        super().__init__(task_args, storage_service)
        self.domain = task_args['domain']

    def validate_task_argument(self):
        if not self.task_args.get('domain'):
            raise Exception('No email was provided')

    def execute(self):
        data = HunterApiService().domain_search(self.domain)
        print(data)