import sys
import datetime
import help
import readchache
import import_file

date_and_time = datetime.datetime.now()

command = sys.argv[1]

def main_program():
    if command == 'help':
        help.help()

    if command == 'dys':
        help.version()

    if command == 'cache':
        readchache.open_cache()

    with open('dystribute_cache.txt', 'a') as f:
        f.write(f'\n{date_and_time}: {command}')

    if import_file == 'import':
        import_file.import_package(sys.argv[2])

    else:
        print('invalid argument')

main_program()
