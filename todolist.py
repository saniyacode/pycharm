from tkinter import *

class ToDoList:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        self.task_var = StringVar()

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Task Entry and Add Button
        self.task_entry = Entry(self.master, textvariable=self.task_var, width=30, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=(20, 5))

        self.add_button = Button(self.master, text="Add Task", command=self.add_task, font=("Arial", 10, "bold"), bg="green", fg="white")
        self.add_button.grid(row=0, column=1, padx=5, pady=(20, 5))

        # Task Listbox
        self.task_listbox = Listbox(self.master, width=40, height=10, font=("Arial", 12), bg="lightyellow", selectbackground="skyblue")
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        # Scrollbar for the Task Listbox
        scrollbar = Scrollbar(self.master, orient="vertical", command=self.task_listbox.yview)
        scrollbar.grid(row=1, column=2, sticky="ns")
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        # Complete and Delete Buttons
        self.complete_button = Button(self.master, text="Mark as Completed", command=self.mark_completed, font=("Arial", 10, "bold"), bg="blue", fg="white")
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_button = Button(self.master, text="Delete Task", command=self.delete_task, font=("Arial", 10, "bold"), bg="red", fg="white")
        self.delete_button.grid(row=2, column=1, padx=5, pady=10)

        self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, END)
        for task in self.tasks:
            self.task_listbox.insert(END, task)

    def add_task(self):
        new_task = self.task_var.get().strip()
        if new_task:
            self.tasks.append(new_task)
            self.update_task_list()
            self.task_var.set("")

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks[task_index] += " (Completed)"
            self.update_task_list()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.update_task_list()

if __name__ == "__main__":
    root = Tk()
    todo_app = ToDoList(root)
    root.mainloop()
