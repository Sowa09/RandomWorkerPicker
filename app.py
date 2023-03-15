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
