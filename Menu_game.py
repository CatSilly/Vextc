import os
import time
from Chapter_menu import hien_thi_menu
from text_effect import loading_anima
from text_effect import slow_print

def clear_screen():
    """Xóa màn hình console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Hiển thị menu chính"""
    clear_screen()
    slow_print("             Vextc", 0.05)
    print("═"*30)
    print("1. Bắt đầu")
    print("2. Thông tin game")
    print("3. Thoát game")
    print("═"*30)

def new_game():
    clear_screen()
    print("\n")
    time.sleep(2)
    hien_thi_menu()
            
def about_game():
    """Hiển thị thông tin game"""
    clear_screen()
    slow_print("            THÔNG TIN GAME", 0.05)
    print("═"*50)
    print(" Tên game: Vextc")
    print(" Phiên bản: Chapter_1")
    print(" Tác giả: Sillycat")
    print(" Ngày phát hành: 2025")
    print("═"*50)
    print(" Một số thông tin đặc biệt vui lòng đọc file README.md")
    print("═"*50)
    input("\nNhấn Enter để quay lại menu chính...")

def main():
    """Hàm chính điều khiển game"""
    while True:
        loading_anima(dur=3)
        display_menu()
        choice = input("Lựa chọn của bạn (1-3): ")
        
        if choice == '1':
            new_game()
            clear_screen()
        elif choice == '2':
            about_game()
            clear_screen()
        elif choice == '3':
            clear_screen()
            slow_print(" :/ ", 0.1)
            time.sleep(1)
            exit()
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 3.")
            time.sleep(1)

if __name__ == "__main__":
    main()