from src.storage_service_abstract import StorageService
import json


class JSONSaveService(StorageService):
    file_name = 'email_verification.json'

    def add_record(self, data_args):
        new_data = {'email': data_args['email'], 'data': data_args}
        try:
            with open(f'{self.file_name}', encoding='utf8') as file_email_verification:
                data_from_file = json.load(file_email_verification)

                data_index = None

                for i in range(len(data_from_file)):
                    if data_from_file[i]['email'] == data_args['email']:
                        data_index = i

                if data_index is None:
                    data_from_file.append(new_data)
                    print('New data add')
                else:
                    data_from_file[data_index] = new_data
                    print('Data updated')

            with open(f'{self.file_name}', 'w', encoding='utf8') as outfile:
                json.dump(data_from_file, outfile, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            with open(f'{self.file_name}', 'w', encoding='utf8') as new_file:
                json.dump([new_data], new_file, indent=4, ensure_ascii=False)

    def update_record(self, data_args):
        pass

    def get_record(self, email):
        try:
            with open(f'{self.file_name}', encoding='utf8') as file_email_verification:
                data_from_file = json.load(file_email_verification)
                for i in data_from_file:
                    if i['email'] == email:
                        print(i)
        except FileNotFoundError:
            raise FileNotFoundError

    def delete_record(self, email):
        try:
            with open(f'{self.file_name}', encoding='utf8') as file_email_verification:
                data_from_file = json.load(file_email_verification)

                data_index = None

                for i in range(len(data_from_file)):
                    if data_from_file[i]['email'] == email:
                        data_index = i

                if data_index is None:
                    print('No found email in file')
                else:
                    del data_from_file[data_index]
                    print('Data deleted')

            with open(f'{self.file_name}', 'w', encoding='utf8') as outfile:
                json.dump(data_from_file, outfile, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            raise FileNotFoundError
