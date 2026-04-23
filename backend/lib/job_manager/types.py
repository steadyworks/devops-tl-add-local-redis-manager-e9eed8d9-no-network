from enum import Enum


class RemoteJobQueue(Enum):
    MAIN_TASK_QUEUE = "main_task_queue"


class RemoteJobType(str, Enum):
    PHOTOBOOK_GENERATION = "photobook_generation"
