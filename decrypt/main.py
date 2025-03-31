from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii


def aes_decrypt(cipher_text, key):
    # Chuyển key thành 16 byte
    key = key.ljust(16, '0').encode('utf-8')[:16]

    # Chuyển hex về bytes
    encrypted_data = binascii.unhexlify(cipher_text)

    # Giải mã
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    return decrypted_data.decode('utf-8')


# Đọc cipher_text từ ENCRYPTED.dat
with open('ENCRYTED.dat', 'r') as encrypted_file:
    cipher_text = encrypted_file.read().strip()

# Đọc key từ KEY.txt
with open('KEY.txt', 'r') as key_file:
    key = key_file.read().strip()

decrypted_text = aes_decrypt(cipher_text, key)
print(f"Decrypted Text: {decrypted_text}")

# Lưu plaintext vào PLAINTEXT.txt
with open('PLAINTEXT.txt', 'w') as plaintext_file:
    plaintext_file.write(decrypted_text)

print("Plaintext đã được lưu vào PLAINTEXT.txt")