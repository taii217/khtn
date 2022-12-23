from zipfile import ZipFile
from system_helper import encryption_list, decryption_list
from main.helper.file_helper import merge_file, read_file, write_file_split, write_file
from main.security.hill_cipher import hill_cipher

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


def encrypt_file(password, path_plaint, is_hidden: bool = False):
    hill = hill_cipher(password)

    data = read_file(path_plaint)
    path = path_plaint.split('/')
    file_name = path.pop(-1).split('.')[-2]
    direction = "/".join(path)

    ciphers = encryption_list(hill, data)

    path_1 = f'{direction}/{file_name}_encryption_1.txt'
    path_2 = f'{direction}/{file_name}_encryption_2.txt'

    sucess, msg = write_file_split(
        path1=path_1, path2=path_2, data=ciphers, is_hidden=is_hidden)
    if not sucess:
        return msg

    with ZipFile(f'{file_name}_1.zip', 'w') as zip1:
        zip1.write(path_1)

    with ZipFile(f'{file_name}_2.zip', 'w') as zip1:
        zip1.write(path_2)

    return 'Thành công'


def decrypt_file(password, path_1, path_2):
    hill = hill_cipher(password)
    data_raw = merge_file(path1=path_1, path2=path_2)
    plains = decryption_list(hill, data_raw)

    path = path_1.split('/')
    file_name = path.pop(-1).split('_')[-3]
    direction = "/".join(path)

    write_file(f"{direction}/{file_name}_sucess.txt", plains)


path_plaint = "C:/Users/taiin/OneDrive/computer/test/plaint.txt"

# print('data: ', data)
# print('ciphers: ', ciphers)
# print('data_raw: ', data_raw)
# print('plains: ', plains)
