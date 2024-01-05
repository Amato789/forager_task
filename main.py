from src.task_factory import TaskFactory, SaveFactory


def handle(command: str, task_args: dict, save_strategy: str) -> None:
    save_service = SaveFactory.get_save_service(save_strategy)
    task = TaskFactory.get_task(command, task_args, save_service)
    task.execute()


if __name__ == '__main__':
    # handle('email_verification', {'email': 'maximsidorchuk@gmail.com'}, 'to_file')
    # handle('get_records', {'email': 'maximsidorchuk@gmail.com'}, 'to_file')
    # handle('delete_records', {'email': 'maximsidorchuk@gmail.com'}, 'to_file')
    handle('domain_search', {'domain': 'stripe.com'}, 'to_file')
