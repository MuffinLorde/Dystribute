import requests
import os

def import_package(package_link):
    os.system(f'git clone {package_link}')
