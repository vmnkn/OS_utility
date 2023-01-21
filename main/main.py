from colors import *
import os
import platform
import time
import random

commands = ['help', 'get_OS_name', 'check_directory']


def load():
    """Algorythm for load animation"""
    for i in range(1, 101):
        time.sleep(random.uniform(0.01, 0.1))
        if i < 50:
            number = f'{light_red + str(i)}'
        elif 50 < i < 90:
            number = f'{light_yellow + str(i)}'
        else:
            number = f'{light_green + str(i)}'
        print(f'\r---Loading: {number}%', end='')


def greet_user():
    """Function for greeting user"""
    print(f'\n{light_cyan + "---OS Utility---"}')
    print(f'\n{cyan + "---Commands:"}')
    for command in commands:
        print(f'\t- {command}')
    print('\n')


def get_os_name():
    """Function for print OS`s info"""
    os_name = f'{platform.system()} {platform.version()} {platform.architecture()[0]}'
    return print(f'{light_green}- OS name:\n'
                 f'- {green + os_name}\n')


def help():
    """Description for all commands"""
    commands_docs = {
        'get_OS_name': get_os_name.__doc__,
        'check_directory': check_directory.__doc__,
    }
    for func, doc in commands_docs.items():
        print(f'\n{light_yellow}- Command name: {func}'
              f'\n{yellow}- Doc: {doc}\n')


def check_directory():
    """Check directory with os module"""
    while True:
        path = input(f'{light_magenta}- Enter path: \n'
                     f'{magenta}- Example: D:\\dir\\file\n'
                     f'{magenta}- Input "exit" for exit: ')
        if path == 'exit':
            break
        load()
        try:
            print(light_magenta + '\n- Content:')
            for file in os.listdir(path):
                print(f'\t{magenta}- {file}')
        except FileNotFoundError:
            print(f'\n{light_red}- UNCORRECT PATH'
                  f'\n{red}- Try again\n')
            print('\n')


def main():
    """Main program algorythm"""
    load()
    greet_user()
    while True:
        user_input = input(light_blue + '---Input command: ')
        print(f'{blue}- COMMAND: {user_input}\n')
        if user_input == commands[0]:
            help()
        elif user_input == commands[1]:
            get_os_name()
        elif user_input == commands[2]:
            check_directory()
        elif user_input == 'exit':
            break
        else:
            print(f'\n{light_red}- UNCNOWN COMMAND'
                  f'\n{red}- Try again or input "help"\n')


main()
