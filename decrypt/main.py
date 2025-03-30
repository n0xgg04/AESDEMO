from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def aes_decrypt(encrypted_bytes, key):
    key = key.ljust(16, '0').encode('utf-8')[:16]

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)

    return decrypted

with open("./ENCRYPTED.dat", 'rb') as ef:  
    encrypted_bytes = ef.read()

with open("./KEY.txt", 'r') as kf:
    key = kf.read().strip()

decrypted_bytes = aes_decrypt(encrypted_bytes, key)

with open("./PLAINTEXT.txt", 'wb') as df:  
    df.write(decrypted_bytes)  