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
        # Form

        tk.Label(self, text="Imię").grid(row=0, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self, text="Nazwisko").grid(row=1, column=0)
        self.surname_entry = tk.Entry(self)
        self.surname_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self, text="Dodaj pracownika", command=self.add_worker)
        self.add_button.grid(row=3, column=0, columnspan=2)

        pass
