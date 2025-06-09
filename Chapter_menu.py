import time
from clear_screen import clear_screen
from text_effect import slow_print
from chapter_1 import *
from colorama import init, Fore, Back, Style
init()

def hien_thi_menu():
    while True:
        clear_screen()
        slow_print("\n           Chọn Chapter", 0.05)
        print("═"*30)
        print("1. Đột Nhập Bảo Tàng [DNBT]")
        print("\n2. [Coming soon]")
        print("\n3. [Coming soon]")
        print("\n4. [Coming soon]")
        print("\n5. [Coming soon]")
        print("═"*30)
        print("6. Thoát")
        print("═"*30)
        lua_chon = input("Nhập lựa chọn của bạn (1-6): ")

        if lua_chon == "6":
            clear_screen()
            slow_print(" Gặp tao 3 giờ sáng... ", 0.1)
            time.sleep(1)
            exit()
            
        elif lua_chon == "1":
            chuc_nang_1()
        elif lua_chon == "2":
            chuc_nang_2()
        elif lua_chon == "3":
            chuc_nang_3()
        elif lua_chon == "4":
            chuc_nang_4()
        elif lua_chon == "5":
            chuc_nang_5()
        else:
            print("\nLựa chọn không hợp lệ!")
            input(" [Nhấn Enter để tiếp tục]")
            
def chuc_nang_1():
    clear_screen()
    cut_scene()
    
def chuc_nang_2():
    clear_screen()
    slow_print(Fore.LIGHTMAGENTA_EX + " Koomi: bạn ơi, chapter chưa ra đâu mà nhấn nhấn gì? :3 ", 0.05)
    input(Style.RESET_ALL + "\n[Enter để quay trở lại]")
    
def chuc_nang_3():
    clear_screen()
    slow_print(Fore.LIGHTMAGENTA_EX + " Koomi: bạn ơi, chapter chưa ra đâu mà nhấn nhấn gì? :3 ", 0.05)
    input(Style.RESET_ALL + "\n[Enter để quay trở lại]")
    
def chuc_nang_4():
    clear_screen()
    slow_print(Fore.LIGHTMAGENTA_EX + " Koomi: bạn ơi, chapter chưa ra đâu mà nhấn nhấn gì? :3 ", 0.05)
    input(Style.RESET_ALL + "\n[Enter để quay trở lại]")
    
def chuc_nang_5():
    clear_screen()
    slow_print(Fore.LIGHTMAGENTA_EX + " Koomi: bạn ơi, chapter chưa ra đâu mà nhấn nhấn gì? :3 ", 0.05)
    input(Style.RESET_ALL + "\n[Enter để quay trở lại]")
    
if __name__ == '__main__':
	hien_thi_menu()