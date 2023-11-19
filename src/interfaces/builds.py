import requests
from bs4 import BeautifulSoup

import os


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