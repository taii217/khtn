from zipfile import ZipFile
from main.helper.file_helper import merge_file, read_file, write_file_split, write_file
from main.security.hill_cipher import hill_cipher
import os

from main.smtp.smtp import check_otp

def encryption_list(hill: hill_cipher, data):
    ciphers = []
    for d in data:
        cip = hill.encrypt(d)
        ciphers.append(cip)
    return ciphers


def decryption_list(hill, data):
    plains = []
    for d in data:
        pla = hill.decrypt(d)
        plains.append(pla)
    return plains


def encrypt_file(email, password, path_plaint, is_hidden: bool = False):
    hill = hill_cipher(password)

    data = [email] + read_file(path_plaint)
    path = path_plaint.split(os.sep)
    file_name = path.pop(-1).split('.')[-2]
    direction = "/".join(path)

    ciphers = encryption_list(hill, data)

    path_1 = f'{direction}/{file_name}_encryption_1.txt'
    path_2 = f'{direction}/{file_name}_encryption_2.txt'

    sucess, msg = write_file_split(path1=path_1, path2=path_2, data=ciphers, is_hidden=is_hidden)
    print('path 1: ', path_1)
    print('path 1: ', path_2)
    return 'Mã hoá thành công' if sucess else msg


def decrypt_file(password, path_1, path_2):
    hill = hill_cipher(password)
    data_raw = merge_file(path1=path_1, path2=path_2)

    email = hill.decrypt(data_raw.pop(0))
    if not check_otp(email):
        return 'otp thất bại'

    ###
    print('Đang giải nén...')

    plains = decryption_list(hill, data_raw)

    path = path_1.split(os.sep)
    file_name = path.pop(-1).split('_')[-3]
    direction = "/".join(path)
    write_file(f"{direction}/{file_name}_sucess.txt", plains)
    ###
    return 'Giải nén thành công !!'
        
