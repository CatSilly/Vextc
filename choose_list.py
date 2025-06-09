from clear_screen import clear_screen
import time

def choose_menu(options, prompt="\n", retry_prompt="Lựa chọn không hợp lệ!"):
    while True:
        clear_screen()
        # In tiêu đề và đường viền
        print(" «( Vextc )»")
        border = " ═" * 15
        print(border)
        
        # In các lựa chọn
        for i, option in enumerate(options, 1):
            print(f" {i}. {option}")
        
        # In đường viền dưới
        print(border)
        
        try:
            choice = input(" Nhập lựa chọn: ")
            if not choice.strip():  # Kiểm tra chuỗi rỗng hoặc chỉ có khoảng trắng
                print(retry_prompt)
                time.sleep(1)
                clear_screen()
                continue
                
            choice_index = int(choice) - 1
            
            if 0 <= choice_index < len(options):
                selected_option = options[choice_index]
                return choice_index, selected_option
            else:
                print(f"{retry_prompt} (Vui lòng nhập số từ 1 đến {len(options)})")
                time.sleep(1)
                clear_screen()
                
        except ValueError:
            print(f"{retry_prompt} (Vui lòng nhập một số nguyên!)")
            time.sleep(1)
            clear_screen()
            
"""
menu_options = [" Xông thẳng", "Lén lút"]
    choice_index, selected = vertical_menu(menu_options)
    if choice_index == 0:
        print("Đang hiển thị thông tin...")
    elif choice_index == 1:
        print("Chuyển sang chế độ chỉnh sửa...")
"""