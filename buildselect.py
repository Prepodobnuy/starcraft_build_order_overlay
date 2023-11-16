import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import requests
from bs4 import BeautifulSoup

import os


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

        # config
        self.configure(bg="#18181c")
        self.resizable(False, False)
        self.geometry(f"450x250")
        self.title("Build Select")

        self.style = ttk.Style(self)
        self.style.configure("Vertical.TScrollbar", background="#18181c", troughcolor="#18181c", gripcount=0, gripmargin=0)
        self.style.configure("Custom.TMenubutton", background="#18181c", foreground="white", width=6, height=3)

        # variables
        self.your_race_selected: str = "Any"
        self.enemy_race_selected: str = "Any"
        self.PATH: str = "build/"
        self.builds: list[str] = builds
        self.builds_names: list[str] = builds_names
        self.online_builds: list = []
        self.online_builds_hrefs: list = []

        self.place_offline_objects()

    def destroy_all_objects(self) -> None:
        for widget in self.winfo_children():
            widget.destroy()

    def get_online_builds(self):
        self.your_race_option_var = self.your_race_option_var.get()
        self.enemy_race_option_var = self.enemy_race_option_var.get()

        your_race_option_var = self.your_race_option_var
        enemy_race_option_var = self.enemy_race_option_var

        def no_nums(string:str) -> bool:
            nums = ["0","1","2","3","4","5","6","7","8","9"]
            for i in string:
                if i in nums:
                    return False
            return True

        if your_race_option_var == "Terran":
            match enemy_race_option_var:
                case "Any":
                    url = 'https://lotv.spawningtool.com/build/tvx'
                case "Terran":
                    url = 'https://lotv.spawningtool.com/build/tvt'
                case "Zerg":
                    url = 'https://lotv.spawningtool.com/build/tvz'
                case "Protoss":
                    url = 'https://lotv.spawningtool.com/build/tvp'
        elif your_race_option_var == "Zerg":
            match enemy_race_option_var:
                case "Any":
                    url = 'https://lotv.spawningtool.com/build/zvx'
                case "Terran":
                    url = 'https://lotv.spawningtool.com/build/zvt'
                case "Zerg":
                    url = 'https://lotv.spawningtool.com/build/zvz'
                case "Protoss":
                    url = 'https://lotv.spawningtool.com/build/zvp'
        elif your_race_option_var == "Protoss":
            match enemy_race_option_var:
                case "Any":
                    url = 'https://lotv.spawningtool.com/build/pvx'
                case "Terran":
                    url = 'https://lotv.spawningtool.com/build/pvt'
                case "Zerg":
                    url = 'https://lotv.spawningtool.com/build/pvz'
                case "Protoss":
                    url = 'https://lotv.spawningtool.com/build/pvp'
        else:
            url = 'https://lotv.spawningtool.com/build'

        self.url:str = url
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        build_names = soup.find_all('a')

        ban_names_list = [
            "/pvx/", "/pvp/", "/pvt/", "/pvz/",
            "/tvx/", "/tvp/", "/tvt/", "/tvz/",
            "/zvx/", "/zvp/", "/zvt/", "/zvz/",
            "/coop/", "/?", "/create/"
            ]

        for i in range(len(build_names)-1, -1, -1):
            if not '/build/' in build_names[i]['href']:
                build_names.pop(i)
                continue
            for ban in ban_names_list:
                if ban in build_names[i]['href'] or no_nums(build_names[i]['href']):
                    build_names.pop(i)
                    break

        for i in range(len(build_names)-1, -1, -1):
            if i % 2 == 0:
                build_names.pop(i)

        self.online_builds = []
        self.online_builds_hrefs = []
        
        for build_name in build_names:
            self.online_builds.append(build_name.text)
            self.online_builds_hrefs.append(build_name['href'])
        
        self.destroy_all_objects()
        self.place_online_objects()

    def place_online_objects(self) -> None:

        self.your_race_option_var = tk.StringVar()
        self.enemy_race_option_var = tk.StringVar()
        self.options = ["Any", "Terran", "Zerg", "Protoss"]

        findex = self.options.index(self.your_race_selected)
        sindex = self.options.index(self.enemy_race_selected)

        self.yours = ttk.OptionMenu(self, self.your_race_option_var, self.options[findex], *self.options, style="Custom.TMenubutton")
        self.enemy = ttk.OptionMenu(self, self.enemy_race_option_var, self.options[sindex], *self.options, style="Custom.TMenubutton")

        self.yours.place(x=250, y=190)
        self.enemy.place(x=360, y=190)

        tk.Label(text="Vs", background="#18181c", foreground="white").place(x=342, y=190)

        tk.Button(command=self.get_online_builds, text="Find Builds", relief=tk.FLAT, bg="#18181c", fg="white", height=1, width=15).place(x=317, y=219)
        tk.Button(command=lambda: (self.destroy_all_objects(), self.place_offline_objects()), text="Back", relief=tk.FLAT, bg="#18181c", fg="white", height=1, width=15).place(x=0, y=219)

        if self.online_builds != []:
            
            for index, build in enumerate(self.online_builds):
                select_build_func = lambda i=index: self.download_online_build(i)

                if index != 4:
                    tk.Button(command=select_build_func, anchor="w", justify="left", text=build, width=60, height=1, bg="#18181c", fg="white", relief=tk.FLAT).place(x=0, y=0 + (index*35))

                if index == 4:
                    tk.Button(command=select_build_func, anchor="w", justify="left", text=build, width=55, height=1, bg="#18181c", fg="white", relief=tk.FLAT).place(x=0, y=0 + (index*35))
                    break
            
            tk.Button(command= self.move_online_list_forward,text="/\\", width=1, height=1, bg="#18181c", fg="white", relief=tk.FLAT).place(x=415, y=140)
       
    def download_online_build(self, index) -> None:
        url = "https://lotv.spawningtool.com" + self.online_builds_hrefs[index]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='build-table')

        rows = table.find_all('tr')

        result: list = []
        for row in rows:
            cells = row.find_all('td')
            result.append(f"{cells[0].text[2:]}  {cells[1].text[2:]}  {cells[2].text[2:]}")

        result = "\n".join(result)

        filename = " ".join(self.online_builds[index].split('/')) if '/' in self.online_builds[index] else self.online_builds[index]

        with open(f"builds/{filename}.txt", "w+") as build:
            build.write(result)
        print(self.online_builds[index] + " installed")

        self.builds = []
        self.builds_names = []

        for build in os.listdir("builds"):
            self.builds.append(build)
            self.builds_names.append(build.split('.')[0])
        
        self.destroy_all_objects()
        self.place_online_objects()

    def place_offline_objects(self) -> None:
            
        for index, build in enumerate(self.builds_names):
            select_build_func = lambda i=index: self.select_build(i)
            delete_build_func = lambda i=index: self.delete_build(i)

            if index != 4:
                tk.Button(command=select_build_func, anchor="w", justify="left", text=build, width=55, height=1, bg="#18181c", fg="white", relief=tk.FLAT).place(x=0, y=0 + (index*35))
                tk.Button(command=delete_build_func, anchor="w", justify="left", text="Del", width=2, height=1, bg="#18181c", fg="white", relief=tk.FLAT).place(x=408, y=0 + (index*35))

            if index == 4:
                tk.Button(command=select_build_func, anchor="w", justify="left", text=build, width=48, height=1, bg="#18181c", fg="white", relief=tk.FLAT).place(x=0, y=0 + (index*35))
                tk.Button(command=delete_build_func, anchor="w", justify="left", text="Del", width=2, height=1, bg="#18181c", fg="white", relief=tk.FLAT).place(x=363, y=0 + (index*35))
                break

        self.install_build_offline = tk.Button(text="Install local build", command=self.install_local_build, relief=tk.FLAT, bg="#18181c", fg="white", height=1, width=15)
        self.install_build_online = tk.Button(text="Browse for builds", command=lambda: (self.destroy_all_objects(), self.place_online_objects()), relief=tk.FLAT, bg="#18181c", fg="white", height=1, width=15)

        self.install_build_offline.place(x=317, y=219)
        self.install_build_online.place(x=0, y=219)

        tk.Button(command= self.move_offline_list_forward,text="/\\", width=2, height=1, bg="#18181c", fg="white", relief=tk.FLAT).place(x=408, y=140)

    def move_online_list_forward(self) -> None:
        b_toappend = self.online_builds.pop(0)
        h_toappend = self.online_builds_hrefs.pop(0)

        self.online_builds.append(b_toappend)
        self.online_builds_hrefs.append(h_toappend)

        self.destroy_all_objects()
        self.place_online_objects()

    def move_offline_list_forward(self) -> None:
        b_toappend = self.builds.pop(0)
        h_toappend = self.builds_names.pop(0)

        self.builds.append(b_toappend)
        self.builds_names.append(h_toappend)

        self.destroy_all_objects()
        self.place_offline_objects()

    def install_local_build(self) -> None:
        filepath = filedialog.askopenfilename(title="Add build", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

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

                self.destroy_all_objects()
                self.place_offline_objects()

            except BaseException as e:
                ...
            
    def delete_build(self, index:int) -> None:
        try:
            os.remove("builds/" + builds[index])
        except BaseException:
            ...
        print(builds[index].split('.')[0] + " deleted")
        builds.pop(index)
        builds_names.pop(index)

        self.destroy_all_objects()
        self.place_offline_objects()
        
    def select_build(self, index:int) -> None:
        with open("selected_build", "w+") as file:
            file.write(builds[index])
        print(builds[index].split('.')[0] + " selected")

        for i in range(len(builds_names)):
            if builds_names[i] == "Selected":
                builds_names[i] = builds[i].split('.')[0]
                break
        builds_names[index] = "Selected"
        self.destroy_all_objects()
        self.place_offline_objects()

if __name__ == "__main__":
    builds = []
    builds_names = []

    for build in os.listdir("builds"):
        try:
            builds.append(build)
            builds_names.append(build.split('.')[0])
        except BaseException: ...
        
    app = App(builds, builds_names)
    app.mainloop()