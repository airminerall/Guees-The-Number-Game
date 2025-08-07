import random
import time
import colorama
from colorama import Fore

nyawa = int(input("Pilih nyawa kamu : "))


angka_acak = random.randint(1,100)



while nyawa > 0:
    try:
        tebakan = int(input("Silahkan Masukan Tebakan Anda : "))

        if tebakan == angka_acak:
            print("Mikir Dulu Yaa....")
            time.sleep(1)
            print(f"{Fore.GREEN}Selamat Anda Menemukan Angka Acak Tersebut !")
            break
        
        elif tebakan > angka_acak:
            print("Mikir Dulu Yaa....")
            time.sleep(1)
            print(f"{Fore.RED}Kegedean Woi")
        else:
            print("Mikir Dulu Yaa....")
            time.sleep(1)
            print(f"{Fore.RED}Kekecilan Woi")

        nyawa -= 1
    except ValueError:
        print("Masukin Berupa Angka dari 1-100 woi")

if nyawa == 0:
    print("Cupu amat dah gitu aja gatau belajar lagi sana", angka_acak)



