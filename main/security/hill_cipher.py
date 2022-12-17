from .hill_cipher_helper import char_to_int_table, gen_salt, gen_table, int_to_char_table
from .hash import hash


class hill_cipher:
    def __init__(self, key):
        self.arr = gen_table()
        self.arr_size = len(self.arr)
        self.key = char_to_int_table(self.arr, hash(key))
     

    def encrypt(self, data):
        salt = gen_salt(self.arr)
        data = f"{salt}{data}"
        data = char_to_int_table(self.arr, data)
        key_length = len(self.key)

        cipher = []
        ind_key = 0
        for m in data:
            data_cipher = (m + self.key[ind_key]) % self.arr_size
            cipher.append(data_cipher)
            ind_key = 0 if ind_key + 1 == key_length else ind_key + 1

        return int_to_char_table(self.arr, cipher)
    
    
    def decrypt(self, cipher_text):
        try:
            cipher_char = char_to_int_table(self.arr, cipher_text)
            key_length = len(self.key)

            plaint = []
            ind_key = 0
            for m in cipher_char:
                data_plaint = (m - self.key[ind_key]) % self.arr_size
                plaint.append(data_plaint)
                ind_key = 0 if ind_key + 1 == key_length else ind_key + 1
            
            plaint_text = int_to_char_table(self.arr, plaint)
            plaint_text = plaint_text.split('e8605470426611edb8780242ac120002')[-1]

            return plaint_text
        except Exception as e:
            return '<this is not your result> !! something error!'
