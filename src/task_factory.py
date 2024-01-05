from src.email_verification import EmailVerification
from src.domain_search import DomainSearch
from src.get_records_task import GetRecordsTask
from src.delete_records_task import DeleteRecordTask
from services.saveservice_sqlite import SQLiteSaveService
from services.saveservice_json import JSONSaveService


class SaveFactory:

    @staticmethod
    def get_save_service(save_strategy):
        if save_strategy == 'to_db':
            return SQLiteSaveService()
        elif save_strategy == 'to_file':
            return JSONSaveService()
        else:
            raise Exception("Not supported retailer")


class TaskFactory:

    @staticmethod
    def get_task(command, task_args, save_service):
        if command == 'email_verification':
            return EmailVerification(task_args, save_service)
        elif command == 'domain_search':
            return DomainSearch(task_args, save_service)
        elif command == 'get_records':
            return GetRecordsTask(task_args, save_service)
        elif command == 'delete_records':
            return DeleteRecordTask(task_args, save_service)
        else:
            raise Exception("Not supported retailer")
