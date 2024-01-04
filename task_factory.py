from email_verification import EmailVerification
from domain_search import DomainSearch


class TaskFactory:

    @staticmethod
    def get_task(task_name, object_name):
        if task_name == 'email_verification':
            return EmailVerification(object_name)
        elif task_name == 'domain_search':
            return DomainSearch()
        else:
            raise Exception("Not supported retailer")
