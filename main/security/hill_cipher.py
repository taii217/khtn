from .hash import hash
import random

class hill_cipher:
    def __init__(self, key):
        self.gen_table()
        self.arr_size=len(self.arr)
        self.key = self.char_to_int_table(hash(key))
    

    def gen_salt(self):
        salt_len = random.randint(200,400)
        salt = []
        for _ in range(salt_len):
            index_table = random.randint(0,self.arr_size-2)
            salt.append(self.arr[index_table])
        salt.append('e8605470426611edb8780242ac120002')
        return "".join(salt)
    

    def gen_table(self):
        self.arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D","E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"," ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "'", ";", ":", "<", ">", "?", "+", "_", "~"]
    

    def char_to_int_table(self, data):
        return [self.arr.index(letter) for letter in data]
    

    def int_to_char_table(self, text):
        data = [self.arr[i] for i in text]
        return "".join(data)
     

    def encrypt(self, data):
        salt = self.gen_salt()
        print('satl', salt)
        data = f"{salt}{data}"
        data = self.char_to_int_table(data)
        key_length = len(self.key)

        cipher = []
        ind_key = 0
        for m in data:
            data_cipher = (m + self.key[ind_key]) % self.arr_size
            cipher.append(data_cipher)
            ind_key = 0 if ind_key + 1 == key_length else ind_key + 1

        print('cipher_text number', cipher)
        return self.int_to_char_table(cipher)
    
    
    def decrypt(self, cipher_text):
        try:
            cipher_char = self.char_to_int_table(cipher_text)
            key_length = len(self.key)

            plaint = []
            ind_key = 0
            for m in cipher_char:
                data_plaint = (m - self.key[ind_key]) % self.arr_size
                plaint.append(data_plaint)
                ind_key = 0 if ind_key + 1 == key_length else ind_key + 1
            
            print('Plaintext number', plaint)
            plaint_text = self.int_to_char_table(plaint)
            plaint_text = plaint_text.split('e8605470426611edb8780242ac120002')[-1]

            return plaint_text
        except Exception as e:
            return '<this is not your result> !! something error!'