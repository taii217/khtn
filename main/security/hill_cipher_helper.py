import random


def gen_salt(arr):
    salt_len = random.randint(200, 400)
    salt = []
    for _ in range(salt_len):
        index_table = random.randint(0, len(arr)-2)
        salt.append(arr[index_table])
    salt.append('e8605470426611edb8780242ac120002')
    return "".join(salt)


def gen_table():
    return ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D","E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"," ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "'", ";", ":", "<", ">", "?", "+", "_", "~", ".", ","]


def char_to_int_table(arr: list, data):
    return [arr.index(letter) for letter in data]


def int_to_char_table(arr, text):
    data = [arr[i] for i in text]
    return "".join(data)
