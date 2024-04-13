import datetime

program_version = '0.1 (alpha)'
date_and_time = datetime.datetime.now()

def help():
    print('Dystribute is a general purpose package manager made for Windows')
    print('-help        : prints all available commands')
    print('-dys         : prints what informatiom of the Dystribute version you have')
    print('-cache       : prints all actions you have done with Dystribute')

def version():
    print('Dystribute is a general purpose package manager made for Windows')
    print(f'\nversion: {program_version}')
