import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_time(seconds):
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins:02d}:{secs:02d}"

def timer():
    clear_screen()
    print("=" * 50)
    print("       КОНСОЛЬНЫЙ ТАЙМЕР")
    print("=" * 50)
    
    try:
        seconds = int(input("\nВведите секунды: "))
        
        while seconds > 0:
            clear_screen()
            print("=" * 50)
            print(f"       ОСТАЛОСЬ: {format_time(seconds)}")
            print("=" * 50)
            time.sleep(1)
            seconds -= 1
        
        clear_screen()
        print("=" * 50)
        print("         ⏰ ВРЕМЯ ВЫШЛО! ⏰")
        print("=" * 50)
        print('\a')  # Звук
        input("\nНажмите Enter для выхода...")
        
    except ValueError:
        print("Ошибка! Введите число!")
        input("Нажмите Enter...")

if __name__ == "__main__":
    timer()