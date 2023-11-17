import tkinter as tk
from tkinter import ttk
import time
import os
from PIL import ImageTk, Image

import keyboard


run = True

def build_parse(build_name : str):
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

            time_list.append(time)
            limit_list.append(part[0])
            timestr_list.append(part[1])
            unit_list.append(part[2])

    return limit_list, time_list, timestr_list, unit_list

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        # window configuration
        self.geometry("275x125")
        self.geometry("+20+20")  
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.configure(bg="#18181c")

        # styles
        self.exit_button_style = ttk.Style()
        self.exit_button_style.configure("Exit.TButton", foreground="white", background="#18181c", relief=tk.FLAT,  height=1, width=2)
        self.exit_button_style.map("Exit.TButton", foreground=[("active", "#d14343")], background=[("active", "#18181c")])

        self.prev_next_order_button_style = ttk.Style()
        self.prev_next_order_button_style.configure("Options.TButton", foreground="white", background="#18181c", relief=tk.FLAT,  height=1, width=2)
        self.prev_next_order_button_style.map("Options.TButton", foreground=[("active", "#707efa")], background=[("active", "#18181c")])

        self.prev_next_order_button_style = ttk.Style()
        self.prev_next_order_button_style.configure("Pause.TButton", foreground="white", background="#18181c", relief=tk.FLAT,  height=1, width=2)
        self.prev_next_order_button_style.map("Pause.TButton", foreground=[("active", "#43d16e")], background=[("active", "#18181c")])

        self.prev_next_order_button_style = ttk.Style()
        self.prev_next_order_button_style.configure("PN.TButton", foreground="white", background="#18181c", relief=tk.FLAT,  height=1, width=2)
        self.prev_next_order_button_style.map("PN.TButton", foreground=[("active", "#d4a748")], background=[("active", "#18181c")])

        # build info labels
        self.last_order = tk.Label(self, anchor="w", font=("Arial", 11), fg="#b5b5b5", bg="#18181c", highlightthickness=0, text="")
        self.prev_order = tk.Label(self, anchor="w", font=("Arial", 11), fg="#d9d9d9", bg="#18181c", highlightthickness=0, text="")
        self.curr_order = tk.Label(self, anchor="w", font=("Arial", 11), fg="#ffffff", bg="#18181c", highlightthickness=0, text="")
        self.next_order = tk.Label(self, anchor="w", font=("Arial", 11), fg="#d9d9d9", bg="#18181c", highlightthickness=0, text="")
        self.nwst_order = tk.Label(self, anchor="w", font=("Arial", 11), fg="#b5b5b5", bg="#18181c", highlightthickness=0, text="")
        
        self.last_order.place(x=23, y=0)
        self.prev_order.place(x=23, y=25)
        self.curr_order.place(x=23, y=50)
        self.next_order.place(x=23, y=75)
        self.nwst_order.place(x=23, y=100)

        self.load_build()
        
        # build icon pictures
        self.last_image = ImageTk.PhotoImage(Image.open("images/empty.png").resize((22, 22), Image.BICUBIC))
        self.prev_image = ImageTk.PhotoImage(Image.open("images/empty.png").resize((22, 22), Image.BICUBIC))
        self.curr_image = ImageTk.PhotoImage(Image.open("images/empty.png").resize((22, 22), Image.BICUBIC))
        self.next_image = ImageTk.PhotoImage(Image.open("images/empty.png").resize((22, 22), Image.BICUBIC))
        self.nwst_image = ImageTk.PhotoImage(Image.open("images/empty.png").resize((22, 22), Image.BICUBIC))

        self.image_last_label = tk.Label(image=self.last_image, bg="#1b1b24")
        self.image_prev_label = tk.Label(image=self.prev_image, bg="#1b1b24")
        self.image_curr_label = tk.Label(image=self.curr_image, bg="#1b1b24")
        self.image_next_label = tk.Label(image=self.next_image, bg="#1b1b24")
        self.image_nwst_label = tk.Label(image=self.nwst_image, bg="#1b1b24")

        self.image_last_label.place(x=0, y=0)
        self.image_prev_label.place(x=0, y=25)
        self.image_curr_label.place(x=0, y=50)
        self.image_next_label.place(x=0, y=75)
        self.image_nwst_label.place(x=0, y=100)

        # buttons
        self.exit_button = ttk.Button(style="Exit.TButton", text="✖",    command=self.end)
        self.help_button = ttk.Button(style="Options.TButton", text="🛈", command=self.info_button)
        self.pause_button = ttk.Button(style="Pause.TButton", text="⏸", command=self.pause)
        self.prev_order_button = ttk.Button(style="PN.TButton", text="↑", command=self.prev_build_order)
        self.next_order_button = ttk.Button(style="PN.TButton", text="↓", command=self.next_build_order)
        
        self.exit_button.place(x=250, y=0)
        self.help_button.place(x=250, y=25)
        self.pause_button.place(x=251, y=50)
        self.prev_order_button.place(x=250, y=75)
        self.next_order_button.place(x=250, y=100)
        
        # variables
        self.icon_list: list[str] = self.get_icons_list()
        self.build_timings: list[str] = []

        self.isplay: bool = False 
        self.paused: bool = False

        self.x: int = 20
        self.y: int = 20

        # binds
        self.bind_keys()
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<B1-Motion>", self.move_window)

        self.load_build()
        self.clear_info()

    # variable parameters funcs
    def get_icons_list(self) -> list[str]:
        return os.listdir("units")

    def get_build_lists(self) -> None:
        self.limit_list, self.time_list, self.timestr_list, self.unit_list = build_parse(self.build)
    
    def load_build(self) -> None:
        with open("selected_build") as file:
            self.build = file.read()
    
    # keybinds and buttons funcs
    def bind_keys(self) -> None:
        keyboard.add_hotkey("ctrl+b", self.change_build)
        keyboard.add_hotkey("ctrl+a", self.start_stop_build_execution)
        keyboard.add_hotkey("ctrl+p", self.pause)

    def prev_build_order(self) -> None:
        if not self.isplay: return
        self.total_time = self.time_list[self.index - 1] if self.index - 1 >= 0 else self.total_time
        self.update()

    def next_build_order(self) -> None:
        if not self.isplay: return
        self.total_time = self.time_list[self.index + 1] if self.index <= len(self.time_list) - 1 else self.total_time
        self.update()

    def info_button(self) -> None:
        if self.isplay: return
        self.last_order.configure(text="ctrl + b -> select build")
        self.prev_order.configure(text="ctrl + a -> start/stop timer")
        self.curr_order.configure(text="ctrl + p -> pause/resume build")
        self.next_order.configure(text="ctrl + [ -> previous order")
        self.nwst_order.configure(text="ctrl + ] -> next order")

    def start_stop_build_execution(self) -> None:
        print("play")
        self.isplay = not self.isplay
        if self.isplay:
            self.paused = False
            self.total_time = 0
            self.current_time = time.time() + 0.25
            time.sleep(0.25)
            
            self.load_build()

            if self.build == "":
                self.last_order.configure(text="No Build is selected")

            if self.build in os.listdir("builds"):

                inform = False

                try:
                    self.get_build_lists()
                    self.fill_images_with_icons(0)
                    self.play()
                except ValueError:
                    print("Build is broken")
                    self.last_order.configure(text="Build is broken")
                    self.isplay = False
                    inform = True

                if not inform:
                    self.clear_info()
                print("stop")
                time.sleep(0.25)
            
            else:
                self.last_order.configure(text="Selected build is not found")

    def change_build(self) -> None:
        print('changing build...')

        os.system("python buildselect.py")
        time.sleep(0.25)

        self.load_build()
        self.clear_info()

        self.update()

    def end(self):
        global run
        run = False
        self.destroy()

    def pause(self):
        self.paused = not self.paused

        if self.paused:
            self.pause_button.configure(text="▶️")
            print("paused")
        else:
            self.pause_button.configure(text="⏸")
            print("unpaused")
        time.sleep(0.25)

    # window movement funcs
    def start_move(self, event) -> None:
        self.x = event.x
        self.y = event.y                                                                                                                                                              

    def move_window(self, event) -> None:
        deltax = event.x - self.x
        deltay = event.y - self.y
        new_x = self.winfo_x() + deltax
        new_y = self.winfo_y() + deltay
        self.geometry(f"+{new_x}+{new_y}")

    # clear icons and text fields func
    def clear_info(self) -> None:
        self.last_order.configure(text="")
        self.prev_order.configure(text="")
        self.curr_order.configure(text="")
        self.next_order.configure(text="")
        self.nwst_order.configure(text="")
        if self.build != '' and self.build in os.listdir('builds'): self.last_order.configure(text=self.build.split('.')[0])

        new_image = Image.open("images/empty.png")
        new_image = new_image.resize((22, 22), Image.BICUBIC)

        self.last_image = ImageTk.PhotoImage(new_image)
        self.prev_image = ImageTk.PhotoImage(new_image)
        self.curr_image = ImageTk.PhotoImage(new_image)
        self.next_image = ImageTk.PhotoImage(new_image)
        self.nwst_image = ImageTk.PhotoImage(new_image)

        self.image_last_label.configure(image=self.last_image)
        self.image_prev_label.configure(image=self.prev_image)
        self.image_curr_label.configure(image=self.curr_image)
        self.image_next_label.configure(image=self.next_image)
        self.image_nwst_label.configure(image=self.nwst_image)

    # fill icons and text fields func
    def fill_images_with_icons(self, index: int) -> None:
        double_names = ["Ghost Academy", "Gravitic Drive", "Hydralisk", "Roach Warren", "Robotics Bay", "Robotics Facility", "Reactor"]

        upgrades = [
            "Terran Infantry Armor 1", "Terran Infantry Armor 2", "Terran Infantry Armor 3",
            "Terran Infantry Weapons 1", "Terran Infantry Weapons 2", "Terran Infantry Weapons 3",
            "Terran Ship Weapons 1", "Terran Ship Weapons 2", "Terran Ship Weapons 3",
            "Terran Vehicle Plating 1", "Terran Vehicle Plating 2", "Terran Vehicle Plating 3",
            "Terran Vehicle Weapons 1", "Terran Vehicle Weapons 2", "Terran Vehicle Weapons 3",
            "Zerg Flyer Attack 1", "Zerg Flyer Attack 2", "Zerg Flyer Attack 3",
            "Zerg Ground Carapace 1", "Zerg Ground Carapace 2", "Zerg Ground Carapace 3",
            "Zerg Melee Attacks 1", "Zerg Melee Attacks 2", "Zerg Melee Attacks 3",
            "Zerg Missile Attacks 1", "Zerg Missile Attacks 2", "Zerg Missile Attacks 3",
            "Zerg Flyer Carapace 1", "Zerg Flyer Carapace 2", "Zerg Flyer Carapace 3",
            "Protoss Air Armor 1", "Protoss Air Armor 2", "Protoss Air Armor 3",
            "Protoss Air Weapons 1", "Protoss Air Weapons 2", "Protoss Air Weapons 3",
            "Protoss Ground Armor 1", "Protoss Ground Armor 2", "Protoss Ground Armor 3",
            "Protoss Ground Weapons 1", "Protoss Ground Weapons 2", "Protoss Ground Weapons 3",
            "Protoss Shields 1", "Protoss Shields 2", "Protoss Shields 3"
            ]
        
        add_buildings = ["Tech Lab", "Reactor"]

        if index >= 2:
            try:
                unit = self.unit_list[index-2].split(',')[0] if ',' in self.unit_list[index-2] else self.unit_list[index-2]
                for add_build in add_buildings:
                    if add_build in unit:
                        unit = add_build
                        break
                for icon in self.icon_list:
                    unit = unit.split(' ')[0] if ' ' in unit and not unit in double_names and not unit in upgrades else unit
                    if unit in icon:
                        new_image = Image.open("units/"+icon)
                        new_image = new_image.resize((22, 22), Image.BICUBIC)
                        self.last_image = ImageTk.PhotoImage(new_image)
                        self.image_last_label.configure(image=self.last_image)
                        break
            except BaseException: ...

        if index >= 1:
            try:
                unit = self.unit_list[index-1].split(',')[0] if ',' in self.unit_list[index-1] else self.unit_list[index-1]
                for add_build in add_buildings:
                    if add_build in unit:
                        unit = add_build
                        break
                for icon in self.icon_list:
                    unit = unit.split(' ')[0] if ' ' in unit and not unit in double_names and not unit in upgrades else unit
                    if unit in icon:
                        new_image = Image.open("units/"+icon)
                        new_image = new_image.resize((22, 22), Image.BICUBIC)
                        self.prev_image = ImageTk.PhotoImage(new_image)
                        self.image_prev_label.configure(image=self.prev_image)
                        break
            except BaseException: ...

        try:
            unit = self.unit_list[index].split(',')[0] if ',' in self.unit_list[index] else self.unit_list[index]
            for add_build in add_buildings:
                if add_build in unit:
                    unit = add_build
                    break
            for icon in self.icon_list:
                unit = unit.split(' ')[0] if ' ' in unit and not unit in double_names and not unit in upgrades else unit
                if unit in icon:
                    new_image = Image.open("units/"+icon)
                    new_image = new_image.resize((22, 22), Image.BICUBIC)
                    self.curr_image = ImageTk.PhotoImage(new_image)
                    self.image_curr_label.configure(image=self.curr_image)
                    break
        except BaseException: ...

        try:
            unit = self.unit_list[index+1].split(',')[0] if ',' in self.unit_list[index+1] else self.unit_list[index+1]
            for add_build in add_buildings:
                if add_build in unit:
                    unit = add_build
                    break
            for icon in self.icon_list:
                unit = unit.split(' ')[0] if ' ' in unit and not unit in double_names and not unit in upgrades else unit
                if unit in icon:
                    new_image = Image.open("units/"+icon)
                    new_image = new_image.resize((22, 22), Image.BICUBIC)
                    self.next_image = ImageTk.PhotoImage(new_image)
                    self.image_next_label.configure(image=self.next_image)
                    break
        except BaseException: ...

        try:
            unit = self.unit_list[index+2].split(',')[0] if ',' in self.unit_list[index+2] else self.unit_list[index+2]
            for add_build in add_buildings:
                if add_build in unit:
                    unit = add_build
                    break
            for icon in self.icon_list:
                unit = unit.split(' ')[0] if ' ' in unit and not unit in double_names and not unit in upgrades else unit
                if unit in icon:
                    new_image = Image.open("units/"+icon)
                    new_image = new_image.resize((22, 22), Image.BICUBIC)
                    self.nwst_image = ImageTk.PhotoImage(new_image)
                    self.image_nwst_label.configure(image=self.nwst_image)
                    break
        except BaseException: ...
        
        if index + 1 == len(self.unit_list):
            new_image = Image.open("empty.png")
            new_image = new_image.resize((22, 22), Image.BICUBIC)

            self.next_image = ImageTk.PhotoImage(new_image)

            self.image_next_label.configure(image=self.next_image)
        
        if index + 2 == len(self.unit_list):
            new_image = Image.open("empty.png")
            new_image = new_image.resize((22, 22), Image.BICUBIC)

            self.nwst_image = ImageTk.PhotoImage(new_image)

            self.image_nwst_label.configure(image=self.nwst_image)
        
        self.update()

    def place_order_to_labels(self, index: int) -> None:
        if index >= 2:
            self.last_order.config(text=f"{self.timestr_list[index - 2]} [{self.limit_list[index - 2]}] {self.unit_list[index - 2]}")
        else:
            self.last_order.config(text="Start of the build")

        if index >= 1:
            self.prev_order.config(text=f"{self.timestr_list[index - 1]} [{self.limit_list[index - 1]}] {self.unit_list[index - 1]}")
        else:
            self.prev_order.config(text="...")

        self.curr_order.config(text=f"{self.timestr_list[index]} [{self.limit_list[index]}] {self.unit_list[index]}")

        try:
            self.next_order.config(text=f"{self.timestr_list[index + 1]} [{self.limit_list[index + 1]}] {self.unit_list[index + 1]}")
        except IndexError: self.next_order.config(text="...")

        try:
            self.nwst_order.config(text=f"{self.timestr_list[index + 2]} [{self.limit_list[index + 2]}] {self.unit_list[index + 2]}")
        except IndexError: self.nwst_order.config(text="End")

    # build execution func
    def play(self) -> None:
        rdy = True
        self.index = 0
        try:
            self.get_build_lists()
            self.place_order_to_labels(0)
        except ValueError:
            print("Build is broken")
            self.curr_order.configure(text="Build is broken")
            self.isplay = False
        while self.isplay:
            self.update()
            if time.time() - self.current_time >= 1 and not self.paused:
                self.current_time = time.time()
                self.total_time += 1
                rdy = True
            
            if self.paused:
                self.current_time = time.time()

            for timing in self.time_list:
                if self.total_time == timing and rdy:
                    self.index = self.time_list.index(timing)

                    try: self.place_order_to_labels(self.index)
                    except IndexError: ...
                    
                    try: self.fill_images_with_icons(self.index)
                    except IndexError: ...
                    
                    try:print(self.limit_list[self.index], self.timestr_list[self.index], self.unit_list[self.index])
                    except IndexError: ...
                    
                    rdy = False

                    break
            
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('p'):
                self.pause()
            
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('a'):
                self.isplay = False

            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('['):
                self.prev_build_order()

            if keyboard.is_pressed('ctrl') and keyboard.is_pressed(']'):
                self.next_build_order()


if __name__ == '__main__':
    while run:
        app = App()
        app.mainloop()