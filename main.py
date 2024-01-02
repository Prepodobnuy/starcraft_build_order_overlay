import os
import time

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

import keyboard
import requests
from bs4 import BeautifulSoup


def find_icon_path(unit_name:str) -> str:
    units = {
        # buildings
        "Assimilator":"assets/icons/Protoss/Buildings/Assimilator.jpg",
        "Cybernetics Core":"assets/icons/Protoss/Buildings/Cybernetics Core.jpg",
        "Dark Shrine":"assets/icons/Protoss/Buildings/Dark Shrine.jpg",
        "Fleet Beacon":"assets/icons/Protoss/Buildings/Fleet Beacon.jpg",
        "Forge":"assets/icons/Protoss/Buildings/Forge.jpg",
        "Gateway":"assets/icons/Protoss/Buildings/Gateway.jpg",
        "Nexus":"assets/icons/Protoss/Buildings/Nexus.jpg",
        "Photon Cannon":"assets/icons/Protoss/Buildings/Photon Cannon.jpg",
        "Pylon":"assets/icons/Protoss/Buildings/Pylon.jpg",
        "Robotics Bay":"assets/icons/Protoss/Buildings/Robotics Bay.jpg",
        "Robotics Facility":"assets/icons/Protoss/Buildings/Robotics Facility.jpg",
        "Shield Battery":"assets/icons/Protoss/Buildings/Shield Battery.jpg",
        "Stargate":"assets/icons/Protoss/Buildings/Stargate.jpg",
        "Templar Archives":"assets/icons/Protoss/Buildings/Templar Archives.jpg",
        "Twilight Council":"assets/icons/Protoss/Buildings/Twilight Council.jpg",

        "Armory":"assets/icons/Terran/Buildings/Armory.jpg",
        "Barracks":"assets/icons/Terran/Buildings/Barracks.jpg",
        "Bunker":"assets/icons/Terran/Buildings/Bunker.jpg",
        "Command Center":"assets/icons/Terran/Buildings/Command Center.jpg",
        "Engineering Bay":"assets/icons/Terran/Buildings/Engineering Bay.jpg",
        "Factory":"assets/icons/Terran/Buildings/Factory.jpg",
        "Fusion Core":"assets/icons/Terran/Buildings/Fusion Core.jpg",
        "Ghost Academy":"assets/icons/Terran/Buildings/Ghost Academy.jpg",
        "Missile Turret":"assets/icons/Terran/Buildings/Missile Turret.jpg",
        "Orbital Command":"assets/icons/Terran/Buildings/Orbital Command.jpg",
        "Planetary Fortress":"assets/icons/Terran/Buildings/Planetary Fortress.jpg",
        "Reactor":"assets/icons/Terran/Buildings/Reactor.jpg",
        "Refinery":"assets/icons/Terran/Buildings/Refinery.jpg",
        "SensorTower":"assets/icons/Terran/Buildings/SensorTower.jpg",
        "Starport":"assets/icons/Terran/Buildings/Starport.jpg",
        "Supply Depot":"assets/icons/Terran/Buildings/Supply Depot.jpg",
        "Tech Lab":"assets/icons/Terran/Buildings/Tech Lab.jpg",

        "Baneling Nest":"assets/icons/Zerg/Buildings/Baneling Nest.jpg",
        "Evolution Chamber":"assets/icons/Zerg/Buildings/Evolution Chamber.jpg",
        "Extractor":"assets/icons/Zerg/Buildings/Extractor.jpg",
        "Greater Spire":"assets/icons/Zerg/Buildings/Greater Spire.jpg",
        "Hatchery":"assets/icons/Zerg/Buildings/Hatchery.jpg",
        "Hive":"assets/icons/Zerg/Buildings/Hive.jpg",
        "Hydralisk Den":"assets/icons/Zerg/Buildings/Hydralisk Den.jpg",
        "Infestation Pit":"assets/icons/Zerg/Buildings/Infestation Pit.jpg",
        "Lair":"assets/icons/Zerg/Buildings/Lair.jpg",
        "Lurker Den":"assets/icons/Zerg/Buildings/Lurker Den.jpg",
        "Nydus Network":"assets/icons/Zerg/Buildings/Nydus Network.jpg",
        "Roach Warren":"assets/icons/Zerg/Buildings/Roach Warren.jpg",
        "Spawning Pool":"assets/icons/Zerg/Buildings/Spawning Pool.jpg",
        "Spine Crawler":"assets/icons/Zerg/Buildings/Spine Crawler.jpg",
        "Spire":"assets/icons/Zerg/Buildings/Spire.jpg",
        "Spore Crawler":"assets/icons/Zerg/Buildings/Spore Crawler.jpg",
        "Ultralisk Cavern":"assets/icons/Zerg/Buildings/Ultralisk Cavern.jpg",

        # units
        "Adept":"assets/icons/Protoss/Units/Adept.jpg",
        "Archon":"assets/icons/Protoss/Units/Archon.jpg",
        "Carrier":"assets/icons/Protoss/Units/Carrier.jpg",
        "Colossus":"assets/icons/Protoss/Units/Colossus.jpg",
        "Dark Templar":"assets/icons/Protoss/Units/Dark Templar.jpg",
        "Disruptor":"assets/icons/Protoss/Units/Disruptor.jpg",
        "High Templar":"assets/icons/Protoss/Units/High Templar.jpg",
        "Immortal":"assets/icons/Protoss/Units/Immortal.jpg",
        "Mothership":"assets/icons/Protoss/Units/Mothership.jpg",
        "Observer":"assets/icons/Protoss/Units/Observer.jpg",
        "Oracle":"assets/icons/Protoss/Units/Oracle.jpg",
        "Phoenix":"assets/icons/Protoss/Units/Phoenix.jpg",
        "Probe":"assets/icons/Protoss/Units/Probe.jpg",
        "Sentry":"assets/icons/Protoss/Units/Sentry.jpg",
        "Stalker":"assets/icons/Protoss/Units/Stalker.jpg",
        "Tempest":"assets/icons/Protoss/Units/Tempest.jpg",
        "Voidray":"assets/icons/Protoss/Units/Voidray.jpg",
        "Warp Prism":"assets/icons/Protoss/Units/Warp Prism.jpg",
        "Zealot":"assets/icons/Protoss/Units/Zealot.jpg",

        "Banshee":"assets/icons/Terran/Units/Banshee.jpg",
        "Battlecruiser":"assets/icons/Terran/Units/Battlecruiser.jpg",
        "Cyclone":"assets/icons/Terran/Units/Cyclone.jpg",
        "Ghost":"assets/icons/Terran/Units/Ghost.jpg",
        "Hellion":"assets/icons/Terran/Units/Hellion.jpg",
        "Liberator":"assets/icons/Terran/Units/Liberator.jpg",
        "Marauder":"assets/icons/Terran/Units/Marauder.jpg",
        "Marine":"assets/icons/Terran/Units/Marine.jpg",
        "Medivac":"assets/icons/Terran/Units/Medivac.jpg",
        "Raven":"assets/icons/Terran/Units/Raven.jpg",
        "Reaper":"assets/icons/Terran/Units/Reaper.jpg",
        "SCV":"assets/icons/Terran/Units/SCV.jpg",
        "Siege Tank":"assets/icons/Terran/Units/Siege.jpg",
        "Thor":"assets/icons/Terran/Units/Thor.jpg",
        "Viking":"assets/icons/Terran/Units/Viking.jpg",
        "Widow Mine":"assets/icons/Terran/Units/Widow Mine.jpg",

        "Baneling":"assets/icons/Zerg/Units/Baneling.jpg",
        "Brood Lord":"assets/icons/Zerg/Units/Brood Lord.jpg",
        "Broodling":"assets/icons/Zerg/Units/Broodling.jpg",
        "Corruptor":"assets/icons/Zerg/Units/Corruptor.jpg",
        "Drone":"assets/icons/Zerg/Units/Drone.jpg",
        "Hydralisk":"assets/icons/Zerg/Units/Hydralisk.jpg",
        "Infestor":"assets/icons/Zerg/Units/Infestor.jpg",
        "Lurker":"assets/icons/Zerg/Units/Lurker.jpg",
        "Mutalisk":"assets/icons/Zerg/Units/Mutalisk.jpg",
        "Overlord":"assets/icons/Zerg/Units/Overlord.jpg",
        "Queen":"assets/icons/Zerg/Units/Queen.jpg",
        "Ravager":"assets/icons/Zerg/Units/Ravager.jpg",
        "Roach":"assets/icons/Zerg/Units/Roach.jpg",
        "Swarm Host":"assets/icons/Zerg/Units/Swarm Host.jpg",
        "Ultralisk":"assets/icons/Zerg/Units/Ultralisk.jpg",
        "Viper":"assets/icons/Zerg/Units/Viper.jpg",
        "Zergling":"assets/icons/Zerg/Units/Zergling.jpg",

        # upgrades
        "Protoss Air Armor 1":"assets/icons/Protoss/Upgrades/Protoss Air Armor 1.jpg",
        "Protoss Air Armor 2":"assets/icons/Protoss/Upgrades/Protoss Air Armor 2.jpg",
        "Protoss Air Armor 3":"assets/icons/Protoss/Upgrades/Protoss Air Armor 3.jpg",
        "Protoss Air Weapons 1":"assets/icons/Protoss/Upgrades/Protoss Air Weapons 1.jpg",
        "Protoss Air Weapons 2":"assets/icons/Protoss/Upgrades/Protoss Air Weapons 2.jpg",
        "Protoss Air Weapons 3":"assets/icons/Protoss/Upgrades/Protoss Air Weapons 3.jpg",
        "Protoss Ground Armor 1":"assets/icons/Protoss/Upgrades/Protoss Ground Armor 1.jpg",
        "Protoss Ground Armor 2":"assets/icons/Protoss/Upgrades/Protoss Ground Armor 2.jpg", 
        "Protoss Ground Armor 3":"assets/icons/Protoss/Upgrades/Protoss Ground Armor 3.jpg",
        "Protoss Ground Weapons 1":"assets/icons/Protoss/Upgrades/Protoss Ground Weapons 1.jpg",
        "Protoss Ground Weapons 2":"assets/icons/Protoss/Upgrades/Protoss Ground Weapons 2.jpg",
        "Protoss Ground Weapons 3":"assets/icons/Protoss/Upgrades/Protoss Ground Weapons 3.jpg", 
        "Protoss Shields 1":"assets/icons/Protoss/Upgrades/Protoss Shields 1.jpg", 
        "Protoss Shields 2":"assets/icons/Protoss/Upgrades/Protoss Shields 2.jpg", 
        "Protoss Shields 3":"assets/icons/Protoss/Upgrades/Protoss Shields 3.jpg", 
        "Anion Pulse Crystals":"assets/icons/Protoss/Upgrades/Anion Pulse Crystals.jpg", 
        "Blink":"assets/icons/Protoss/Upgrades/Blink.jpg", 
        "Charge":"assets/icons/Protoss/Upgrades/Charge.jpg", 
        "Extended Thermal Lance":"assets/icons/Protoss/Upgrades/Extended Thermal Lance.jpg", 
        "Flux Vanes":"assets/icons/Protoss/Upgrades/Flux Vanes.jpg", 
        "Gravitic Boosters":"assets/icons/Protoss/Upgrades/Gravitic Boosters.jpg", 
        "Gravitic Drive":"assets/icons/Protoss/Upgrades/Gravitic Drive.jpg", 
        "Psionic Storm":"assets/icons/Protoss/Upgrades/Psionic Storm.jpg", 
        "Resonating Glaives":"assets/icons/Protoss/Upgrades/Resonating Glaives.jpg", 
        "Shadow Stride":"assets/icons/Protoss/Upgrades/Shadow Stride.jpg", 
        "Tectonic Destabilizers":"assets/icons/Protoss/Upgrades/Tectonic Destabilizers.jpg", 
        "Warp Gate":"assets/icons/Protoss/Upgrades/Warp Gate.jpg", 

        "Terran Infantry Armor 1":"assets/icons/Terran/Upgrades/Terran Infantry Armor 1.jpg",
        "Terran Infantry Armor 2":"assets/icons/Terran/Upgrades/Terran Infantry Armor 2.jpg",
        "Terran Infantry Armor 3":"assets/icons/Terran/Upgrades/Terran Infantry Armor 3.jpg",
        "Terran Infantry Weapons 1":"assets/icons/Terran/Upgrades/Terran Infantry Weapons 1.jpg",
        "Terran Infantry Weapons 2":"assets/icons/Terran/Upgrades/Terran Infantry Weapons 2.jpg",
        "Terran Infantry Weapons 3":"assets/icons/Terran/Upgrades/Terran Infantry Weapons 3.jpg",
        "Terran Vehicle Plating 1":"assets/icons/Terran/Upgrades/Terran Vehicle Plating 1.jpg",
        "Terran Vehicle Plating 2":"assets/icons/Terran/Upgrades/Terran Vehicle Plating 2.jpg", 
        "Terran Vehicle Plating 3":"assets/icons/Terran/Upgrades/Terran Vehicle Plating 3.jpg",
        "Terran Vehicle Weapons 1":"assets/icons/Terran/Upgrades/Terran Vehicle Weapons 1.jpg",
        "Terran Vehicle Weapons 2":"assets/icons/Terran/Upgrades/Terran Vehicle Weapons 2.jpg",
        "Terran Vehicle Weapons 3":"assets/icons/Terran/Upgrades/Terran Vehicle Weapons 3.jpg",
        "Terran Ship Weapons 1":"assets/icons/Terran/Upgrades/Terran Ship Weapons 1.jpg",
        "Terran Ship Weapons 2":"assets/icons/Terran/Upgrades/Terran Ship Weapons 2.jpg",
        "Terran Ship Weapons 3":"assets/icons/Terran/Upgrades/Terran Ship Weapons 3.jpg",
        "Advanced Ballistics":"assets/icons/Terran/Upgrades/Advanced Ballistics.jpg",
        "Cloaking Field":"assets/icons/Terran/Upgrades/Cloaking Field.jpg",
        "Combat Shield":"assets/icons/Terran/Upgrades/Combat Shield.jpg",
        "Concussive Shells":"assets/icons/Terran/Upgrades/Concussive Shells.jpg",
        "Corvid Reactor":"assets/icons/Terran/Upgrades/Corvid Reactor.jpg",
        "Drilling Claws":"assets/icons/Terran/Upgrades/Drilling Claws.jpg",
        "Enhanced Shockwaves":"assets/icons/Terran/Upgrades/Enhanced Shockwaves.jpg",
        "Hisec Auto Tracking":"assets/icons/Terran/Upgrades/Hisec Auto Tracking.jpg",
        "Hurricane Thrusters":"assets/icons/Terran/Upgrades/Hurricane Thrusters.jpg",
        "Hyperflight Rotors":"assets/icons/Terran/Upgrades/Hyperflight Rotors.jpg",
        "Infernal Pre-Igniter":"assets/icons/Terran/Upgrades/Infernal Pre-Igniter.jpg",
        "Neosteel Armor":"assets/icons/Terran/Upgrades/Neosteel Armor.jpg",
        "Permanent Cloaking":"assets/icons/Terran/Upgrades/Permanent Cloaking.jpg",
        "Smart Servos":"assets/icons/Terran/Upgrades/Smart Servos.jpg",
        "Stimpack":"assets/icons/Terran/Upgrades/Stimpack.jpg",
        "Weapon Refit":"assets/icons/Terran/Upgrades/Weapon Refit.jpg",

        "Zerg Flyer Carapace 1":"assets/icons/Zerg/Upgrades/Zerg Flyer Carapace 1.jpg",
        "Zerg Flyer Carapace 2":"assets/icons/Zerg/Upgrades/Zerg Flyer Carapace 2.jpg", 
        "Zerg Flyer Carapace 3":"assets/icons/Zerg/Upgrades/Zerg Flyer Carapace 3.jpg",
        "Zerg Flyer Weapons 1":"assets/icons/Zerg/Upgrades/Zerg Flyer Attack 1.jpg",
        "Zerg Flyer Weapons 2":"assets/icons/Zerg/Upgrades/Zerg Flyer Attack 2.jpg",
        "Zerg Flyer Weapons 3":"assets/icons/Zerg/Upgrades/Zerg Flyer Attack 3.jpg",
        "Zerg Ground Carapace 1":"assets/icons/Zerg/Upgrades/Zerg Ground Carapace 1.jpg",
        "Zerg Ground Carapace 2":"assets/icons/Zerg/Upgrades/Zerg Ground Carapace 2.jpg",
        "Zerg Ground Carapace 3":"assets/icons/Zerg/Upgrades/Zerg Ground Carapace 3.jpg",
        "Zerg Melee Weapons 1":"assets/icons/Zerg/Upgrades/Zerg Melee Attacks 1.jpg",
        "Zerg Melee Weapons 2":"assets/icons/Zerg/Upgrades/Zerg Melee Attacks 2.jpg",
        "Zerg Melee Weapons 3":"assets/icons/Zerg/Upgrades/Zerg Melee Attacks 3.jpg",
        "Zerg Missile Weapons 1":"assets/icons/Zerg/Upgrades/Zerg Melee Attacks 1.jpg",
        "Zerg Missile Weapons 2":"assets/icons/Zerg/Upgrades/Zerg Melee Attacks 2.jpg",
        "Zerg Missile Weapons 3":"assets/icons/Zerg/Upgrades/Zerg Melee Attacks 3.jpg",
        "Anabolic Synthesis":"assets/icons/Zerg/Upgrades/Anabolic Synthesis.jpg",
        "Burrow":"assets/icons/Zerg/Upgrades/Burrow.jpg",
        "Centrifugal Hooks":"assets/icons/Zerg/Upgrades/Centrifugal Hooks.jpg",
        "Chitinous Plating":"assets/icons/Zerg/Upgrades/Chitinous Plating.jpg",
        "Glial Reconstitution":"assets/icons/Zerg/Upgrades/Glial Reconstitution.jpg",
        "Grooved Spines":"assets/icons/Zerg/Upgrades/Grooved Spines.jpg",
        "Metabolic Boost":"assets/icons/Zerg/Upgrades/Metabolic Boost.jpg",
        "Muscular Augments":"assets/icons/Zerg/Upgrades/Muscular Augments.jpg",
        "Neural Parasite":"assets/icons/Zerg/Upgrades/Neural Parasite.jpg",
        "Pathogen Glands":"assets/icons/Zerg/Upgrades/Pathogen Glands.jpg",
        "Pneumatized Carapace":"assets/icons/Zerg/Upgrades/Pneumatized Carapace.jpg",
        "Seismic Spines":"assets/icons/Zerg/Upgrades/Seismic Spines.jpg",
        "Tunneling Claws":"assets/icons/Zerg/Upgrades/Tunneling Claws.jpg"
    }

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

    return "assets/empty.png"

def find_builds(your_race:str="Any", enemy_race:str="Any"):
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

def download_build(builds:list[str], hrefs:list[str], path:str, index:int):
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

def read_conf() -> str:
    parameters:list = []

    with open("settings.conf") as config:
        data = config.read()
    
    data = data.split('\n')
    for line in data:
        parameters.append(line.split('=')[1])

    fs:int = int(parameters[0])
    fc:str = parameters[1]
    bgc:str = parameters[2]
    emp:str = parameters[3]

    return fs, fc, bgc, emp

def write_conf(font_size:int|None, font_color:str|None, bg_color:str|None, empty_image:str|None) -> None:
    font_size:int = 12 if font_size == None else font_size
    font_color:str = "#d4d4d4" if font_color == None else font_color
    bg_color:str = "#18181a" if bg_color == None else bg_color
    empty_image:str = "assets/empty.png" if empty_image == None else empty_image
    data:str = f"font_size={font_size}\nfont_color={font_color}\nbg_color={bg_color}\nempty_image={empty_image}"
    
    with open("settings.conf", "w+") as file:
        file.write(data)

class App(tk.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.set_variables()
        self.configure_app()
        self.place_runtime()

    def set_variables(self) -> None:
        self.font_size, self.font_color, self.bg_color, self.empty_image = read_conf()

        with open('assets/lastbuild') as file:
            self.selected_build = file.read()

        self.exit_button_style = ttk.Style()
        self.exit_button_style.configure("SCO.TButton", foreground=self.font_color, background=self.bg_color, relief=tk.FLAT,  height=1, width=2)
        self.exit_button_style.map("SCO.TButton", foreground=[("active", "#5a5af2")], background=[("active", self.bg_color)])
        
        self.exit_button_style = ttk.Style()
        self.exit_button_style.configure("RACE.TButton", foreground=self.font_color, background=self.bg_color, relief=tk.FLAT,  height=1, width=8)
        self.exit_button_style.map("RACE.TButton", foreground=[("active", "#5a5af2")], background=[("active", self.bg_color)])
        
        self.exit_button_style = ttk.Style()
        self.exit_button_style.configure("LONG.TButton", foreground=self.font_color, background=self.bg_color, relief=tk.FLAT,  height=1, width=25)
        self.exit_button_style.map("LONG.TButton", foreground=[("active", "#5a5af2")], background=[("active", self.bg_color)])

        self.builds: list = os.listdir("builds")
        self.isplay: bool = False
        self.paused: bool = False
        self.locked: bool = False

    def configure_app(self) -> None:
        self.geometry("240x115")
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.configure(bg=self.bg_color)

        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<B1-Motion>", self.move_window)
        keyboard.add_hotkey("ctrl+a", self.start_stop_build_execution)

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

    def remove_all_widgets(self) -> None:
        widgets = self.winfo_children()
        for widget in widgets:
            widget.destroy()

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

        self.prev_order = tk.Label(self, anchor='w', font=("Arial", self.font_size), fg=self.font_color, bg=self.bg_color, highlightthickness=0, text="")
        self.curr_order = tk.Label(self, anchor='w', font=("Arial", self.font_size), fg=self.font_color, bg=self.bg_color, highlightthickness=0, text="")
        self.next_order = tk.Label(self, anchor='w', font=("Arial", self.font_size), fg=self.font_color, bg=self.bg_color, highlightthickness=0, text="")
        self.last_order = tk.Label(self, anchor='w', font=("Arial", self.font_size), fg=self.font_color, bg=self.bg_color, highlightthickness=0, text="")
        
        self.selected_build_label = tk.Label(self, anchor='w', font=("Arial", self.font_size), fg=self.font_color, bg=self.bg_color, highlightthickness=0, width=30, text=self.selected_build)
        self.timer = tk.Label(self, anchor='w', font=("Arial", self.font_size), fg=self.font_color, bg=self.bg_color, highlightthickness=0, text="00:00")

        # Images

        self.prev_image = ImageTk.PhotoImage(Image.open(self.empty_image).resize((22, 22), Image.BICUBIC))
        self.curr_image = ImageTk.PhotoImage(Image.open(self.empty_image).resize((22, 22), Image.BICUBIC))
        self.next_image = ImageTk.PhotoImage(Image.open(self.empty_image).resize((22, 22), Image.BICUBIC))
        self.last_image = ImageTk.PhotoImage(Image.open(self.empty_image).resize((22, 22), Image.BICUBIC))

        self.prev_order_image = tk.Label(image=self.prev_image, bg=self.bg_color)
        self.curr_order_image = tk.Label(image=self.curr_image, bg=self.bg_color)
        self.next_order_image = tk.Label(image=self.next_image, bg=self.bg_color)
        self.last_order_image = tk.Label(image=self.last_image, bg=self.bg_color)

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

        self.selected_build_label.place(x=70, y=94)

        self.prev_order_image.place(x=0, y=0)
        self.curr_order_image.place(x=0, y=22)
        self.next_order_image.place(x=0, y=44)
        self.last_order_image.place(x=0, y=66)

        self.exit_button.place(x=215, y=0)
        self.lock_button.place(x=44, y=90)

        self.builds_button.place(x=0, y=90)
        self.download_button.place(x=22, y=90)
        self.timer.place(x=180, y=4)

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

        tk.Label(self, anchor='w', font=("Arial", self.font_size), fg=self.font_color, bg=self.bg_color, highlightthickness=0, text="Vs").place(x=66, y=3)

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
        self.back_button = ttk.Button(style="SCO.TButton", text='<', command=self.place_runtime)
        self.prev_build_button = ttk.Button(style="SCO.TButton", text="↑", command=self.online_build_prev)
        self.next_build_button = ttk.Button(style="SCO.TButton", text="↓", command=self.online_build_next)
        if len(self.online_builds) > 5: 
            self.prev_build_button.place(x=215, y=66)
            self.next_build_button.place(x=215, y=88)

        self.exit_button.place(x=215, y=0)
        self.back_button.place(x=195, y=0)
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()