# Created by Jordan Leich on 7/27/2020

# Imports
from colored import fg, attr

reset = attr('reset')


def print_green(message_text):
    print(f'{fg("green")}{message_text}{reset}')


def print_red(message_text):
    print(f'{fg("red")}{message_text}{reset}')


def print_yellow(message_text):
    print(f'{fg("yellow")}{message_text}{reset}')


def print_blue(message_text):
    print(f'{fg("blue")}{message_text}{reset}')


def user_error(message_text):
    print_red(message_text)
