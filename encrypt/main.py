from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

def aes_encrypt(plain_text, key):
    # Chuyển key thành 16 byte (AES-128 yêu cầu)
    key = key.ljust(16, '0').encode('utf-8')[:16]

    # Chuyển plaintext thành bytes và pad để đủ 16 byte
    data = plain_text.encode('utf-8')
    data = pad(data, AES.block_size)

    # Mã hóa AES-128 (ECB mode)
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(data)

    # Chuyển thành dạng HEX để dễ đọc
    return binascii.hexlify(encrypted).decode('utf-8')


# Đọc plaintext từ file PLAINTEXT.txt
with open('PLAINTEXT.txt', 'r') as plaintext_file:
    plain_text = plaintext_file.read().strip()

# Đọc key từ file KEY.txt
with open('KEY.txt', 'r') as key_file:
    key = key_file.read().strip()

cipher_text = aes_encrypt(plain_text, key)

# Lưu cipher text vào ENCRYTED.dat
with open('ENCRYTED.dat', 'w') as encrypted_file:
    encrypted_file.write(cipher_text)

print("Cipher text đã được lưu vào ENCRYTED.dat")