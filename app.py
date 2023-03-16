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

        # List
        tk.Label(self, text="Pracownicy").grid(row=4, column=0)
        self.worker_listbox = tk.Listbox(self)
        self.worker_listbox.grid(row=5, column=0, columnspan=2)

        self.pick_button = tk.Button(self, text="Wylosuj pracownika", command=self.pick_worker)
        self.pick_button.grid(row=6, column=0, columnspan=2)

        self.delete_button = tk.Button(self, text="Usuń pracownika", command=self.delete_worker)
        self.delete_button.grid(row=7, column=0, columnspan=2)

        self.pack()

    def add_worker(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        listbox = self.worker_listbox.get(0, 'end')

        for item in listbox:
            if name in item and surname in item:
                tk.messagebox.showinfo("Pracownik istnieje", f"Pracownik {name} {surname} istnieje")
                break
        else:
            worker = Worker(name, surname)
            self.worker_manager.add_worker(worker)
            self.worker_listbox.insert(tk.END, f"{worker.name} {worker.surname}")

    def pick_worker(self):
        if self.worker_manager.workers:
            random_worker = self.worker_manager.random_pick()
            tk.messagebox.showinfo("Random worker", f"{random_worker.name} {random_worker.surname}")
        else:
            tk.messagebox.showinfo("Brak pracowników", "Nie można wylosować")

    def delete_worker(self):
        delete_worker = self.worker_listbox.curselection()
        if delete_worker:
            worker = self.worker_manager.workers[delete_worker[0]]
            self.worker_listbox.delete(delete_worker[0])
            self.worker_manager.remove_worker(worker)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
