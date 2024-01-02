def int_to_time(num):
    hours = num // 60
    minutes = num % 60
    return f"{hours:02d}:{minutes:02d}"

for i in range(6001):
    print(int_to_time(i))