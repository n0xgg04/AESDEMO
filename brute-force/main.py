from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii
import string
import itertools
import time  # Import time module to measure duration

# Đọc cipher text từ ENCRYPTED.dat
with open('ENCRYTED.dat', 'r') as encrypted_file:
    cipher_text = encrypted_file.read().strip()
encrypted_bytes = binascii.unhexlify(cipher_text)

# Đọc plaintext mục tiêu từ PLAINTEXT.txt
with open('PLAINTEXT.txt', 'r') as plaintext_file:
    target_plaintext = plaintext_file.read().strip()

# Tập ký tự: số và chữ in thường
charset = string.digits + string.ascii_lowercase  # gồm 0-9 và a-z

found = None
keys_tried = 0
start_time = time.time()  # Start timing

# Duyệt qua các độ dài key từ 1 đến 3 ký tự
for length in range(1, 10):
    for candidate_tuple in itertools.product(charset, repeat=length):
        candidate = ''.join(candidate_tuple)
        keys_tried += 1

        # Chuyển candidate thành key 16 byte bằng cách thêm '0' về bên phải
        key = candidate.ljust(16, '0').encode('utf-8')[:16]
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted = cipher.decrypt(encrypted_bytes)
        try:
            decrypted = unpad(decrypted, AES.block_size)
            if decrypted.decode('utf-8') == target_plaintext:
                found = candidate
                elapsed_time = time.time() - start_time  # Calculate elapsed time
                print("\nTìm thấy key đúng:", candidate)
                print("Plaintext ban đầu:", decrypted.decode('utf-8'))
                print(f"Số giây tốn: {elapsed_time:.2f} giây")  # Print elapsed time
                break
        except Exception:
            pass

        # In ra số key đã thử mỗi 1000 key (có thể điều chỉnh nếu cần)
        if keys_tried % 1000 == 0:
            print(f"Đã thử: {keys_tried} key")

    if found:
        break

if not found:
    print("Không tìm thấy key phù hợp")

print(f"Tổng số key đã thử: {keys_tried}")
