import rsa

# Генерация и сохранение ключей для сервера
server_public_key, server_private_key = rsa.newkeys(1024)
with open(".public_key_server.txt", "wb") as f:
    f.write(server_public_key.save_pkcs1())
with open(".private_key_server.txt", "wb") as f:
    f.write(server_private_key.save_pkcs1())

# Генерация и сохранение ключей для клиента
client_public_key, client_private_key = rsa.newkeys(1024)
with open(".public_key_client.txt", "wb") as f:
    f.write(client_public_key.save_pkcs1())
with open(".private_key_client.txt", "wb") as f:
    f.write(client_private_key.save_pkcs1())

print("Keys for server and client created successfully.")
