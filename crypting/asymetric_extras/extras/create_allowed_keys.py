import rsa
import pickle

# Генерируем несколько пар ключей и сохраняем публичные ключи в файл
public_keys = []
for _ in range(3):
    public_key, _ = rsa.newkeys(1024)
    public_keys.append(public_key)

with open("allowed_keys.txt", "wb") as file:
    pickle.dump(public_keys, file)

print("Allowed keys file created successfully.")
