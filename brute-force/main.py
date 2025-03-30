import string
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

with open('./ENCRYPTED.dat', 'rb') as f:
    encrypted_bytes = f.read()

with open('./PLAINTEXT.txt', 'r') as f:
    expected_plaintext = f.read().strip()

key = "1".ljust(16, '0').encode('utf-8')[:16]

cipher = AES.new(key, AES.MODE_ECB)
decrypted = cipher.decrypt(encrypted_bytes)

try:
    decrypted = unpad(decrypted, AES.block_size)
    print(f"Trying key: {'1'} -> Decrypted text: {decrypted.decode('utf-8')}")
    if decrypted.decode('utf-8') == expected_plaintext:  
        print("\nFound the correct key:", '1')
        print("Original plaintext:", decrypted.decode('utf-8'))
    else:
        print("The key did not match the expected plaintext.")
except Exception as e:
    print("Decryption failed:", str(e))
