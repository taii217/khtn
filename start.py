import os
from system_helper import decrypt_file, encrypt_file


path_plaint = "C:/Users/taiin/OneDrive/computer/test/plaint.txt"



def menu():
    print('1. encryption file')
    print('2. encryption file')
    command = input('number command: ')
    match command:
        case 1:
            password = input('password: ')
            path_plaint = input('insert path file: ')
            is_hidden = input('is_hidden(0|1): ')
            msg = encrypt_file(password, path_plaint, is_hidden)
            print(msg)
        case 2:
            password = input('password: ')
            path_1 = input('insert path_1 file: ')
            path_2 = input('insert path_2 file: ')
            decrypt_file(password, path_1, path_2)
        case _:
            print("not recognize command, try again")


try:
    while True:
        menu()
        os.system('cls')
except KeyboardInterrupt:
    print('interrupted!')


            

