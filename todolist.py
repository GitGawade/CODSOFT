import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.configure(bg='lightblue')

        self.listbox = tk.Listbox(root, bg='white')
        self.listbox.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add task", command=self.add_task, bg='green', fg='white')
        self.add_button.pack()

        self.del_button = tk.Button(root, text="Delete task", command=self.del_task, bg='red', fg='white')
        self.del_button.pack()

        self.update_button = tk.Button(root, text="Update task", command=self.update_task, bg='yellow', fg='black')
        self.update_button.pack()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Warning", "Please enter a task.")

    def del_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
            self.tasks.pop(selected_task_index)
        except:
            messagebox.showinfo("Warning", "Please select a task to delete.")

    def update_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            new_task = self.entry.get()
            self.listbox.delete(selected_task_index)
            self.listbox.insert(selected_task_index, new_task)
            self.tasks[selected_task_index] = new_task
            self.entry.delete(0, tk.END)
        except:
            messagebox.showinfo("Warning", "Please select a task to update.")

def main():
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()

