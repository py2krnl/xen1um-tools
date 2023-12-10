import os

RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"


def clear_screen():
    os.system("clear")


def xen_print(text, color_code, bold = True):
    print_str = BOLD + color_code + text + RESET
    if bold != True:
        print_str = color_code + text + RESET
    print(print_str)