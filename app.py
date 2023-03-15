import tkinter as tk
import tkinter.messagebox
import random


class Worker:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class WorkerManager:
    def __init__(self):
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def remove_worker(self, worker):
        self.workers.remove(worker)

    def random_pick(self):
        return random.choice(self.workers)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.worker_manager = WorkerManager()
        self.create_widgets()

    def create_widgets(self):
        pass
