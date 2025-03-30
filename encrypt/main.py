from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def aes_encrypt(plain_text, key):
    key = key.ljust(16, '0').encode('utf-8')[:16]

    data = plain_text.encode('utf-8')
    data = pad(data, AES.block_size)

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(data)

    return encrypted 

with open("./PLAINTEXT.txt", 'r') as f:
    plaintext = f.read()
    
with open("./KEY.txt", 'r') as kf:
    key = kf.read().strip() 

encrypted_bytes = aes_encrypt(plaintext, key)

with open("./ENCRYPTED.dat", 'wb') as ef:  # Open in binary write mode
    ef.write(encrypted_bytes)  