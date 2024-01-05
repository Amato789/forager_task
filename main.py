from src.task_factory import TaskFactory, SaveFactory


def handle(task_name: str, task_args: dict, save_strategy: str) -> None:
    save_service = SaveFactory.get_save_service(save_strategy)
    task = TaskFactory.get_task(task_name, task_args, save_service)
    task.execute()


if __name__ == '__main__':
    handle('email_verification', {'email': 'miannahabibi@gmail.com'}, 'to_db')
