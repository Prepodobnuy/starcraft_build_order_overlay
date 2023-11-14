import tkinter as tk
from tkinter import filedialog
import os
from time import sleep


def remake(build : str):
    try:
        with open(build) as file:
            print(file.read())
            data = file.read().split("\n")
        
        for i in data:
            if i != ['']:
                part = []
                for j in i.split('\t'):
                    part.append(j[2:])
                result.append("  ".join(part))
        
        result = "\n".join(result)
        print(result)
        with open(build, 'w+') as file:
            file.write(result)
    except BaseException:
        ...

class App(tk.Tk):
    def __init__(self, builds : list[str] = ['None'], builds_names : list[str] = ['None']):
        super().__init__()

        self.resizable(False, False)
        self.geometry(f"{280}x{20 + (30 * (len(builds) + 1))}")
        self.configure(bg="#18181c")
        self.title("Select Build")
        self.place()

    def place(self):
        self.delButtons = []
        self.geometry(f"{280}x{20 + (30 * (len(builds) + 1))}")

        for i, name in enumerate(builds_names):
            tk.Button(text=name, command= lambda i=i: self.push(i, builds), width=25, height=1, bg="#18181c", fg="white", highlightbackground="#24242e").place(x=25, y=10 + (30 * i))
            tk.Button(text="Del", command=lambda i=i: (lambda index: (self.delete_build(index)))(i), width=1, height=1, bg="#18181c", fg="white", highlightbackground="#24242e").place(x=225, y=10 + (30 * i))

        self.add_btn = tk.Button(text="Add build", command= self.add_build, width=25, height=1, bg="#18181c", fg="white", highlightbackground="#24242e")
        self.add_btn.place(x=25, y=10 + (30 * (len(builds_names))))


    def delete_build(self, index:int):
        os.remove("builds/"+builds[index])
        builds_names.pop(index)
        builds.pop(index)
        for widget in self.winfo_children():
            widget.destroy()
        self.update()
        self.place()

    def add_build(self):
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
        filepath = filedialog.askopenfilename(title="Add build", filetypes=filetypes)

        if filepath:
            try:
                remake(filepath)
                newpath = "builds/" + filepath if not "/" in filepath else "builds/" + filepath.split('/')[-1]
                os.rename(filepath, newpath)

                name = filepath if not "/" in filepath else filepath.split('/')[-1]

                with open('builds/'+name) as file:
                    text = file.read().split("\n")

                result = []

                for i in text:
                    try:
                        f = i.split("\t")[0][2:]
                        s = i.split("\t")[1]
                        t = i.split("\t")[2]
                        result.append(f+s+t)
                    except BaseException:
                        ...

                with open('builds/'+name, "w+") as file:
                    file.write("\n".join(result))
                
                if not name in builds:
                    print(name.split('.')[0] + ' added')
                    builds.append(name)
                    builds_names.append(name.split('.')[0])

                for widget in self.winfo_children():
                    widget.destroy()
                self.update()
                self.place()

            except BaseException as e:
                ...

    def push(self, param, builds):
        print(f"{builds[param].split('.')[0]} selected")
        with open("selected_build", "w+") as file:
            file.write(builds[param])
            exit()

if __name__ == "__main__":
    builds = []
    builds_names = []

    for build in os.listdir("builds"):
        builds.append(build)
        builds_names.append(build.split('.')[0])

    app = App(builds, builds_names)
    app.mainloop()