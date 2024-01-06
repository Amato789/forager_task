from src.commans.email_verification import EmailVerification
from src.commans.domain_search import DomainSearch
from src.commans.get_records_task import GetRecordTask
from src.commans.delete_records_task import DeleteRecordTask
from src.services.storage_service_sqlite import SQLiteSaveService
from src.services.storage_service_json import JSONSaveService
from src.storage_service_abstract import StorageService
from src.task_abstract import Task


class SaveFactory:

    @staticmethod
    def get_save_service(save_strategy: str) -> StorageService:
        if save_strategy == 'to_db':
            return SQLiteSaveService()
        elif save_strategy == 'to_file':
            return JSONSaveService()
        else:
            raise Exception('Not supported retailer')


class TaskFactory:

    @staticmethod
    def get_task(command: str, command_args: dict, storage_service: StorageService) -> Task:
        if command == 'email_verification':
            return EmailVerification(command_args, storage_service)
        elif command == 'domain_search':
            return DomainSearch(command_args, storage_service)
        elif command == 'get_record':
            return GetRecordTask(command_args, storage_service)
        elif command == 'delete_record':
            return DeleteRecordTask(command_args, storage_service)
        else:
            raise Exception('Not supported retailer')
