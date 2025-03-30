from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii


def aes_encrypt(plain_text, key):
    key = key.ljust(16, '0').encode('utf-8')[:16]

    data = plain_text.encode('utf-8')
    data = pad(data, AES.block_size)

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(data)

    return binascii.hexlify(encrypted).decode('utf-8')