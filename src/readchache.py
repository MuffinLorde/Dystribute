import datetime

date_and_time = datetime.datetime.now()

def open_cache():
    with open('dystribute_cache.txt', 'r') as f:
        lines = f.readlines()

        count = 0

        for line in lines:
            count += 1
            line_strip = line.strip()
            print(f'\n{line_strip}')
