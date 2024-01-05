from src.email_verification import EmailVerification
from src.domain_search import DomainSearch
from services.save_service import SaveService


class SaveFactory:

    @staticmethod
    def get_save_service(save_strategy):
        if save_strategy == 'to_db':
            return SaveService()
        else:
            raise Exception("Not supported retailer")


class TaskFactory:

    @staticmethod
    def get_task(task_name, task_args, save_service):
        if task_name == 'email_verification':
            return EmailVerification(task_args, save_service)
        elif task_name == 'domain_search':
            return DomainSearch(task_args, save_service)
        else:
            raise Exception("Not supported retailer")
