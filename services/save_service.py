from abc import ABC, abstractmethod


class SaveService(ABC):
    db_name: str

    @abstractmethod
    def add_record(self, data_args):
        raise NotImplementedError

    @abstractmethod
    def update_record(self, data_args):
        raise NotImplementedError

    @abstractmethod
    def get_record(self):
        raise NotImplementedError

    @abstractmethod
    def delete_record(self, email):
        raise NotImplementedError
