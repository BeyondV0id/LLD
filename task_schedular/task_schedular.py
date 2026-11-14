import uuid
from collections import deque
from enum import Enum
from queue import PriorityQueue


class TaskStatus(Enum):
    SCHEDULED: "scheduled"
    RUNNING: "running"
    COMPLETED: "completed"

class Server:
    def __init__(self, id: int, weight: int) -> None:
        self.id = id
        self.weight = weight
        self.available_at = 0

    def get_id(self) -> int:
        return self.id

    def get_available_at(self) -> int:
        return self.available_at

    def is_available(self, current_time: int) -> int:
        return self.available_at <= current_time


class Task:
    def __init__(self, id: int, duration: int, arrivalTime: int) -> None:
        self.id = uuid.uuid4().hex[:12]
        self.duration = duration
        self.arrivalTime = arrivalTime
        self.status = TaskStatus.SCHEDULED

    def get_status(self) -> TaskStatus:
        return self.status

    def get_id(self) -> str:
        return self.id

    def get_arrivalTime(self):
        return self.arrivalTime

    def get_duration(self):
        return self.duration


class TaskQueue:
    # TODO: waitingTasks,addTasks,getNextTask,isEmpty

    def __init__(self) -> None:
        self.waiting_tasks: deque[Task] = deque()

    def add_task(self, task: Task) -> None:
        self.waiting_tasks.append(task)

    def get_next_task(self) -> Task:
        return self.waiting_tasks.popleft()

    def is_empty(self) -> bool:
        size = len(self.waiting_tasks)
        return size == 0


class ServerPool:
    def __init__(self) -> None:
        self.available_servers = PriorityQueue()
        self.busy_servers = PriorityQueue()

    def add_server(self, server: Server) -> None:
        self.available_servers.put((server.weight, server.get_id(), server))

    def has_available_server(self) -> bool:
        return not self.available_servers.empty()

    def release_available_servers(self, current_time: int) -> None:

        while not self.busy_servers.empty():
            end_time, weight, server_id, server, task = self.busy_servers.get()
            
            if end_time <= current_time:
                self.available_servers.put((end_time,weight,server_id,server))

            else:
                self.busy_servers.put((end_time,weight,server_id,server,task))
                return

    def get_available_server(self):

        if not self.available_servers.empty():
            _,_,server = self.available_servers.get()
            return server

    def assign_server(self, server: Server,task: Task, current_time: int, duration: int) -> None:
        server.available_at = duration + current_time

        self.busy_servers.put((server.available_at, server.weight, server.get_id(),task))

    def next_free_time(self) -> int | None:

        if self.busy_servers.empty(): return None

        end_time, weight, server_id, server, task = self.busy_servers.get()
        self.busy_servers.put((end_time,weight,server_id,server,task))
        return

        

class TaskSchedular:
    def __init__(self, servers: list[int], tasks: list[int]) -> None:
        self.server_pool = ServerPool()

        self.task_queue = TaskQueue()
        self.current_time = 0

        for server_id,weight in enumerate(servers):
            self.server_pool.add_server(Server(server_id,weight))

        self.duration = tasks

    def process_arrivals(self) -> None:
        while self.next_task_index

