def parse(build_name : str):
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