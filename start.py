import os
from main.helper.system_helper import debugger_is_active
from system_helper import decrypt_file, encrypt_file


path_plaint = "C:/Users/taiin/OneDrive/computer/test/plaint.txt"



def menu():
    print('1. encryption file')
    print('2. decryption file')
    command = input('number command: ')
    os.system('cls')
    match command:
        case '1':
            case1()
        case '2':
            case2()
        case _:
            print("not recognize command, try again")


def case1():
    email = input('email: ')
    password = input('password: ')
    path_plaint = input('insert path file: ').replace('"','')
    is_hidden = int(input('is_hidden(0|1): '))
    msg = encrypt_file(email, password, path_plaint, is_hidden)
    print(msg)


def case2():
    password = input('password: ')
    path_1 = input('insert path_1 file: ').replace('"', '')
    path_2 = input('insert path_2 file: ').replace('"', '')
    msg = decrypt_file(password, path_1, path_2)
    print(msg)


if __name__ == "__main__":
    if debugger_is_active():
        print('Chương trình không cho phép chạy trong debug/sanbox')
    else:
        os.system('cls')
        try:
            while True:
                print("------------------------------------")
                menu()
        except KeyboardInterrupt:
            print('interrupted!')

            

