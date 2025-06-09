from text_effect import slow_print
from clear_screen import clear_screen
from colorama import init, Fore, Back, Style
import time
from Menu_game import *
init()

def fail_display(text, callback=None):
	clear_screen()
	
	slow_print(Fore.RED + Style.BRIGHT + "              Fail ", 0.05)
	print(Style.RESET_ALL + "} } "* 10)
	print("\n")
	slow_print(text, 0.05)
	print("\n")
	print("{ { "*10)
	input(" [Enter để quay lại] ")
	clear_screen()
	
	if callback: callback()
	
def complete_display(text):
	clear_screen()
	slow_print(Fore.CYAN + Style.BRIGHT + " "*15 + "Complete", 0.1)

	print(Style.RESET_ALL + "//"*20)
	print("\n")
	print(text)
	print("\n")
	print("\\"*40)

	time.sleep(1)

	# Hỏi người chơi muốn quay về menu hay thoát
	choice = input("\n[Enter để quay lại menu chính | gõ 'q' để thoát]: ")
	if choice.lower() == 'q':
		clear_screen()
		slow_print("Cảm ơn bạn đã chơi!", 0.05)
		time.sleep(2)
		clear_screen()
		exit()

	from Menu_game import hien_thi_menu
	hien_thi_menu()
	
"""Mẫu:
complete_display(" "*15 + "rất xiêm")
""