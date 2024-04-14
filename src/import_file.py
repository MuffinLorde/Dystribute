import requests
import os

def import_package(package_link):
    os.system(f'git clone {package_link}')

    with open('dyst.config', 'a') as main_file:
        count = 0

        lines = main_file.readlines()

        for line in lines:
            count += 1
            line_strip = line.strip()

            print(line_strip)
