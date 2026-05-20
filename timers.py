import time
import os

def timer():
    os.system('cls')
    print("=" * 40)
    print("       КОНСОЛЬНЫЙ ТАЙМЕР")
    print("=" * 40)
    
    seconds = int(input("Введите секунды: "))
    
    while seconds > 0:
        os.system('cls')
        print("=" * 40)
        print(f"       ОСТАЛОСЬ: {seconds} сек")
        print("=" * 40)
        time.sleep(1)
        seconds -= 1
    
    os.system('cls')
    print("=" * 40)
    print("        ⏰ ВРЕМЯ ВЫШЛО! ⏰")
    print("=" * 40)
    input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    timer()
