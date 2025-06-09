import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        print("\033[H\033[J", end="", flush=True)
