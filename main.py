import os
import time
import tkinter as tk
from tkinter import ttk

import keyboard
import requests
from PIL import ImageTk, Image
from bs4 import BeautifulSoup

from rc import *


def find_icon_path(unit_name:str) -> str:
    count = [(lambda i: f"x{i}")(i) for i in range(2, 21)]
    unit_name = "Reactor" if "Reactor" in unit_name else unit_name
    unit_name = "Tech Lab" if "Tech Lab" in unit_name else unit_name
    unit_name = unit_name.split(',')[0] if ',' in unit_name else unit_name 
    unit_name = unit_name.split(' (Chrono')[0] if '(Chrono Boost)' in unit_name else unit_name
    unit_name = unit_name.split(' Level')[0] + unit_name.split(' Level')[1] if ' Level' in unit_name else unit_name
    for mod in count:
        if mod in unit_name:
            unit_name = unit_name.split(" " + mod)[0]
            break

    for unit in units:
        if unit == unit_name: return units[unit]

    return empty_image

def find_builds(your_race:str="Any", enemy_race:str="Any") -> tuple[list[str], list[str]]:
    # function takes list of build orders from spawningtool.com
 
    def no_nums(string:str) -> bool:
        nums = ["0","1","2","3","4","5","6","7","8","9"]
        for i in string:
            if i in nums:
                return False
        return True

    if your_race == "Terran":
        match enemy_race:
            case "Any":
                url = 'https://lotv.spawningtool.com/build/tvx'
            case "Terran":
                url = 'https://lotv.spawningtool.com/build/tvt'
            case "Zerg":
                url = 'https://lotv.spawningtool.com/build/tvz'
            case "Protoss":
                url = 'https://lotv.spawningtool.com/build/tvp'
    elif your_race == "Zerg":
        match enemy_race:
            case "Any":
                url = 'https://lotv.spawningtool.com/build/zvx'
            case "Terran":
                url = 'https://lotv.spawningtool.com/build/zvt'
            case "Zerg":
                url = 'https://lotv.spawningtool.com/build/zvz'
            case "Protoss":
                url = 'https://lotv.spawningtool.com/build/zvp'
    elif your_race == "Protoss":
        match enemy_race:
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
    
    baseurl = url
    online_builds = []
    online_builds_hrefs = []

    for i in range(5):
        if i > 0: url = baseurl + f"/?&p={i}"
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

        for build_name in build_names:
            online_builds.append(build_name.text)
            online_builds_hrefs.append(build_name['href'])
        
    return online_builds, online_builds_hrefs

def download_build(builds:list[str], hrefs:list[str], path:str, index:int) -> None:
    # function is downloading selected build order from spawningtool.com
    url = "https://lotv.spawningtool.com" + hrefs[index]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='build-table')

    rows = table.find_all('tr')

    result: list = []
    for row in rows:
        cells = row.find_all('td')
        result.append(f"{cells[0].text[2:]}  {cells[1].text[2:]}  {cells[2].text[2:]}")

    result = "\n".join(result)

    filename = " ".join(builds[index].split('/')) if '/' in builds[index] else builds[index]
    filename = " ".join(builds[index].split('.')) if '.' in builds[index] else filename

    if not filename + ".txt" in os.listdir(path):
        with open(f"{path}/{filename}.txt", "w+") as build:
            build.write(result)
        print(builds[index] + " installed")

def build_parse(build_name : str) -> tuple[list[str], list[int], list[str], list[str]]:
    with open(f"builds/{build_name}") as file:
        data = file.read().split('\n')
    
    limit_list = []
    time_list = []
    timestr_list = []
    unit_list = []

    for i in data:
        if i != ['']:
            part = i.split('  ')
            
            if ':' in part[1]:
                time = part[1].split(':')
                time = (int(time[0]) * 60) + int(time[1])
            else:
                time = int(part[1])

            limit_list.append(part[0])
            time_list.append(time)
            timestr_list.append(part[1])
            unit_list.append(part[2])

    return limit_list, time_list, timestr_list, unit_list

class App(tk.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.set_variables()
        self.configure_app()
        self.place_runtime()

    def remove_all_widgets(self) -> None:
        widgets = self.winfo_children()
        for widget in widgets:
            widget.destroy()

    # -- Config funcs --

    def set_variables(self) -> None:
        with open('assets/lastbuild') as file:
            self.selected_build = file.read()

        self.exit_button_style = ttk.Style()
        self.exit_button_style.configure("SCO.TButton", foreground=font_color, background=bg_color, relief=tk.FLAT,  height=1, width=2)
        self.exit_button_style.map("SCO.TButton", foreground=[("active", "#5a5af2")], background=[("active", bg_color)])
        
        self.exit_button_style = ttk.Style()
        self.exit_button_style.configure("RACE.TButton", foreground=font_color, background=bg_color, relief=tk.FLAT,  height=1, width=8)
        self.exit_button_style.map("RACE.TButton", foreground=[("active", "#5a5af2")], background=[("active", bg_color)])
        
        self.exit_button_style = ttk.Style()
        self.exit_button_style.configure("LONG.TButton", foreground=font_color, background=bg_color, relief=tk.FLAT,  height=1, width=25)
        self.exit_button_style.map("LONG.TButton", foreground=[("active", "#5a5af2")], background=[("active", bg_color)])

        self.builds: list = os.listdir("builds")
        self.isplay: bool = False
        self.paused: bool = False
        self.locked: bool = False

    def configure_app(self) -> None:
        self.geometry("240x115")
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.configure(bg=bg_color)

        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<B1-Motion>", self.move_window)
        keyboard.add_hotkey("ctrl+a", self.start_stop_build_execution)

    # -- Window movement funcs --
        
    def lock(self) -> None:
        self.locked = not self.locked

    def start_move(self, event) -> None:
        if self.locked: return
        self.x = event.x
        self.y = event.y                                                                                                                                                              

    def move_window(self, event) -> None:
        if self.locked: return
        deltax = event.x - self.x
        deltay = event.y - self.y
        new_x = self.winfo_x() + deltax
        new_y = self.winfo_y() + deltay
        self.geometry(f"+{new_x}+{new_y}")

    # -- Object place funcs --

    def place_runtime(self) -> None:
        # places objects which is needed for build display
        self.remove_all_widgets()

        # Labels

        self.prev_order = tk.Label(self, anchor='w', font=("Arial", font_size), fg=font_color, bg=bg_color, highlightthickness=0, text="")
        self.curr_order = tk.Label(self, anchor='w', font=("Arial", font_size), fg=font_color, bg=bg_color, highlightthickness=0, text="")
        self.next_order = tk.Label(self, anchor='w', font=("Arial", font_size), fg=font_color, bg=bg_color, highlightthickness=0, text="")
        self.last_order = tk.Label(self, anchor='w', font=("Arial", font_size), fg=font_color, bg=bg_color, highlightthickness=0, text="")
        
        self.selected_build_label = tk.Label(self, anchor='w', font=("Arial", font_size), fg=font_color, bg=bg_color, highlightthickness=0, width=30, text=self.selected_build)
        self.timer = tk.Label(self, anchor='w', font=("Arial", font_size), fg=font_color, bg=bg_color, highlightthickness=0, text="00:00")

        # Images

        self.prev_image = ImageTk.PhotoImage(Image.open(empty_image).resize((22, 22), Image.BICUBIC))
        self.curr_image = ImageTk.PhotoImage(Image.open(empty_image).resize((22, 22), Image.BICUBIC))
        self.next_image = ImageTk.PhotoImage(Image.open(empty_image).resize((22, 22), Image.BICUBIC))
        self.last_image = ImageTk.PhotoImage(Image.open(empty_image).resize((22, 22), Image.BICUBIC))

        self.prev_order_image = tk.Label(image=self.prev_image, bg=bg_color)
        self.curr_order_image = tk.Label(image=self.curr_image, bg=bg_color)
        self.next_order_image = tk.Label(image=self.next_image, bg=bg_color)
        self.last_order_image = tk.Label(image=self.last_image, bg=bg_color)

        #font_color=#d4d4d4
        #bg_color=#18181a

        # Buttons

        self.exit_button = ttk.Button(style="SCO.TButton", text='✖', command=self.destroy)
        self.lock_button = ttk.Button(style="SCO.TButton", text='🔒', command=self.lock)

        self.builds_button = ttk.Button(style="SCO.TButton", text='🛈', command=self.place_build_select)
        self.download_button = ttk.Button(style="SCO.TButton", text='↓', command=self.place_build_online_parameters)

        self.prev_order.place(x=22, y=0)
        self.curr_order.place(x=22, y=22)
        self.next_order.place(x=22, y=44)
        self.last_order.place(x=22, y=66)

        self.selected_build_label.place(x=46, y=93)

        self.prev_order_image.place(x=0, y=0)
        self.curr_order_image.place(x=0, y=22)
        self.next_order_image.place(x=0, y=44)
        self.last_order_image.place(x=0, y=66)

        self.exit_button.place(x=215, y=0)
        self.lock_button.place(x=215, y=22)

        self.builds_button.place(x=0, y=90)
        self.download_button.place(x=22, y=90)
        self.timer.place(x=180, y=3)

    def prev_build(self):
        self.builds.insert(0, self.builds.pop())
        self.place_build_select()

    def next_build(self):
        self.builds.append(self.builds.pop(0))
        self.place_build_select()

    def select_build(self, index: int) -> None:
        with open("assets/lastbuild", "w+") as file:
            file.write(self.builds[index])
        self.selected_build = self.builds[index]
        self.place_runtime()

    def delete_build(self, index:int) -> None:
        os.remove("builds/"+self.builds[index])
        self.builds.pop(index)
        self.place_build_select()

    def place_build_select(self) -> None:
        # places objects which is needed for build selecting
        self.remove_all_widgets()
        
        build_names: list = []

        try:
            for build in self.builds:
                build_names.append(build.split('.tx')[0])

            for i in range(len(build_names)):
                if i == 5:
                    break
                if i == 0:
                    ttk.Button(style="LONG.TButton", text=build_names[i], command= lambda index=i: self.select_build(index)).place(x=22, y=0)
                    ttk.Button(style="SCO.TButton", text="Dl", command= lambda index=i: self.delete_build(index)).place(x=0, y=0)
                    continue
                ttk.Button(style="LONG.TButton", text=build_names[i], command= lambda index=i: self.select_build(index)).place(x=22, y=22*i)
                ttk.Button(style="SCO.TButton", text="Dl", command= lambda index=i: self.delete_build(index)).place(x=0, y=22*i)
        except Exception as e: ...

        # Buttons

        self.exit_button = ttk.Button(style="SCO.TButton", text='✖', command=self.destroy)
        self.lock_button = ttk.Button(style="SCO.TButton", text='🔒', command=self.lock)
        self.back_button = ttk.Button(style="SCO.TButton", text='<', command=self.place_runtime)
        self.prev_build_button = ttk.Button(style="SCO.TButton", text="↑", command=self.prev_build)
        self.next_build_button = ttk.Button(style="SCO.TButton", text="↓", command=self.next_build)

        self.exit_button.place(x=215, y=0)
        self.lock_button.place(x=215, y=22)
        self.back_button.place(x=195, y=0)
        if len(self.builds) > 5: 
            self.prev_build_button.place(x=215, y=66)
            self.next_build_button.place(x=215, y=88)

    def change_your_race(self):
        race = self.your_race_button.cget("text")
        res = ""
        match race:
            case "Terran":
                res = "Zerg"
            case "Zerg":
                res = "Protoss"
            case "Protoss":
                res = "Any"
            case "Any":
                res = "Terran"
        self.your_race_button.configure(text=res)
        self.update()

    def change_enemy_race(self):
        race = self.enemy_race_button.cget("text")
        res = ""
        match race:
            case "Terran":
                res = "Zerg"
            case "Zerg":
                res = "Protoss"
            case "Protoss":
                res = "Any"
            case "Any":
                res = "Terran"
        self.enemy_race_button.configure(text=res)
        self.update()
    
    def build_search(self):
        self.online_builds, self.online_builds_hrefs = find_builds(self.your_race_button.cget("text"), self.enemy_race_button.cget("text"))
        self.place_build_online_download()

    def place_build_online_parameters(self) -> None:
        # places objects which is needed for online build search
        self.remove_all_widgets()
        
        # Labels

        tk.Label(self, anchor='w', font=("Arial", font_size), fg=font_color, bg=bg_color, highlightthickness=0, text="Vs").place(x=66, y=3)

        # Buttons

        self.your_race_button = ttk.Button(style="RACE.TButton", text="Terran", command=self.change_your_race)
        self.enemy_race_button = ttk.Button(style="RACE.TButton", text="Terran", command=self.change_enemy_race)

        self.exit_button = ttk.Button(style="SCO.TButton", text='✖', command=self.destroy)
        self.lock_button = ttk.Button(style="SCO.TButton", text='🔒', command=self.lock)
        self.back_button = ttk.Button(style="SCO.TButton", text='<', command=self.place_runtime)
        self.search_button = ttk.Button(style="RACE.TButton", text='Search', command=self.build_search)

        self.your_race_button.place(x=0, y=0)
        self.enemy_race_button.place(x=88, y=0)

        self.exit_button.place(x=215, y=0)
        self.lock_button.place(x=215, y=22)
        self.back_button.place(x=195, y=0)
        self.search_button.place(x=170, y=87)

    def online_build_prev(self) -> None:
        self.online_builds.insert(0, self.online_builds.pop())
        self.online_builds_hrefs.insert(0, self.online_builds_hrefs.pop())
        self.place_build_online_download()

    def online_build_next(self) -> None:
        self.online_builds.append(self.online_builds.pop(0))
        self.online_builds_hrefs.append(self.online_builds_hrefs.pop(0))
        self.place_build_online_download()

    def place_build_online_download(self) -> None:
        # places objects which is needed for online build download
        self.remove_all_widgets()

        try:

            for i in range(len(self.online_builds)):
                if i == 5:
                    break
                if i == 0:
                    ttk.Button(style="LONG.TButton", text=self.online_builds[i], command= lambda index=i: (download_build(self.online_builds, self.online_builds_hrefs, "builds", index), self.set_variables())).place(x=0, y=0)
                    continue
                ttk.Button(style="LONG.TButton", text=self.online_builds[i], command= lambda index=i: (download_build(self.online_builds, self.online_builds_hrefs, "builds", index), self.set_variables())).place(x=0, y=22*i)
        except Exception as e: ...
        
        # Buttons

        self.exit_button = ttk.Button(style="SCO.TButton", text='✖', command=self.destroy)
        self.lock_button = ttk.Button(style="SCO.TButton", text='🔒', command=self.lock)
        self.back_button = ttk.Button(style="SCO.TButton", text='<', command=self.place_runtime)
        self.prev_build_button = ttk.Button(style="SCO.TButton", text="↑", command=self.online_build_prev)
        self.next_build_button = ttk.Button(style="SCO.TButton", text="↓", command=self.online_build_next)
        if len(self.online_builds) > 5: 
            self.prev_build_button.place(x=215, y=66)
            self.next_build_button.place(x=215, y=88)

        self.exit_button.place(x=215, y=0)
        self.lock_button.place(x=215, y=22)
        self.back_button.place(x=195, y=0)
        pass

    # -- Runtime funcs --

    def update_runtime_images(self, index:int) -> None:
        if index >= 1:
            try:
                new_image = Image.open(find_icon_path(self.unit_list[index-1]))
                new_image = new_image.resize((22, 22), Image.BICUBIC)
                self.prev_image = ImageTk.PhotoImage(new_image)
                self.prev_order_image.configure(image=self.prev_image)
            except BaseException: ...

        try:
            new_image = Image.open(find_icon_path(self.unit_list[index]))
            new_image = new_image.resize((22, 22), Image.BICUBIC)
            self.curr_image = ImageTk.PhotoImage(new_image)
            self.curr_order_image.configure(image=self.curr_image)
        except BaseException: ...

        try:
            new_image = Image.open(find_icon_path(self.unit_list[index+1]))
            new_image = new_image.resize((22, 22), Image.BICUBIC)
            self.next_image = ImageTk.PhotoImage(new_image)
            self.next_order_image.configure(image=self.next_image)
        except BaseException: ...

        try:
            new_image = Image.open(find_icon_path(self.unit_list[index+2]))
            new_image = new_image.resize((22, 22), Image.BICUBIC)
            self.nwst_image = ImageTk.PhotoImage(new_image)
            self.last_order_image.configure(image=self.nwst_image)
        except BaseException: ...
        
    def update_runtime_labels(self, index:int) -> None:
        if index >= 1: self.prev_order.config(text=f"{self.timestr_list[index - 1]} [{self.limit_list[index - 1]}] {self.unit_list[index - 1]}")
        else: self.prev_order.config(text="...")

        self.curr_order.config(text=f"{self.timestr_list[index]} [{self.limit_list[index]}] {self.unit_list[index]}")

        try: self.next_order.config(text=f"{self.timestr_list[index + 1]} [{self.limit_list[index + 1]}] {self.unit_list[index + 1]}")
        except IndexError: self.next_order.config(text="...")

        try: self.last_order.config(text=f"{self.timestr_list[index + 2]} [{self.limit_list[index + 2]}] {self.unit_list[index + 2]}")
        except IndexError: self.last_order.config(text="End")    

    def play(self) -> None:

        def int_to_time(num):
            hours = num // 60
            minutes = num % 60
            return f"{hours:02d}:{minutes:02d}"
        
        self.current_time: float = time.time()
        self.runtime_index: int = 0
        self.total_time: int = 0
        rdy = True
        while self.isplay:
            self.update()
            if self.paused: self.current_time = time.time()
            
            if time.time() - self.current_time >= 1 and not self.paused:
                self.current_time = time.time()
                self.total_time += 1
                rdy = True
            
            if rdy:
                for timing in self.time_list:
                    if self.total_time != timing: continue
                    
                    rdy = False
                    self.runtime_index = self.time_list.index(timing)

                    try: self.update_runtime_images(self.runtime_index)
                    except IndexError: ...
                        
                    try: self.update_runtime_labels(self.runtime_index)
                    except IndexError: ...
                        
                    try:print(self.limit_list[self.runtime_index], self.timestr_list[self.runtime_index], self.unit_list[self.runtime_index])
                    except IndexError: ...
                        
                    break

            self.timer.configure(text=int_to_time(self.total_time))

            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('p'):
                self.paused = not self.paused
                
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('a'):
                self.isplay = not self.isplay

    def start_stop_build_execution(self) -> None:
        time.sleep(0.1)
        self.isplay = not self.isplay
        print(self.selected_build)
        if self.isplay:
            try:
                self.limit_list, self.time_list, self.timestr_list, self.unit_list = build_parse(self.selected_build)
                self.play()

            except Exception as e:
                print(e)
                self.place_runtime()
                self.prev_order.configure(text="Build is broken")
        if not self.isplay:
            self.place_runtime()
            time.sleep(0.1)


if __name__ == "__main__":
    app = App()
    app.mainloop()