from main.security.hill_cipher import hill_cipher


hill = hill_cipher('abcdef')
print('text      : ', text := 'sometimes the first step to success is the failure')
print('encryption: ', cipher := hill.encrypt(text))
print('decryption: ', plaint := hill.decrypt(cipher))


