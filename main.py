from task_factory import TaskFactory


def handle(task_name: str, object_name: str) -> None:
    """
    Start task.

    :param task_name: str
    :param object_name: str
    :return: None
    """
    task = TaskFactory.get_task(task_name, object_name)
    task.start_task()


if __name__ == '__main__':
    handle('email_verification', 'maximsidorchuk@gmail.com')
