import rsa
import random

client_public_key,client_private_key=rsa.newkeys(1024)

with open(".public_key_client.txt",'wb') as file:
    file.write(client_public_key.save_pkcs1())
file.close()

with open(".private_key_client.txt",'wb') as file:
    file.write(client_private_key.save_pkcs1())
file.close()


serverr_public_key,serverr_private_key=rsa.newkeys(1024)

with open(".public_key_server.txt",'wb') as file:
    file.write(serverr_public_key.save_pkcs1())
file.close()

with open(".private_key_server.txt",'wb') as file:
    file.write(serverr_private_key.save_pkcs1())
file.close()