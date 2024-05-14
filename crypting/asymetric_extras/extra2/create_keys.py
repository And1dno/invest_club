import rsa
import random


class Keygen:
    def gen_cilent_keys(self):
        client_public_key,client_private_key=rsa.newkeys(1024)

        with open(".public_key_client.txt",'wb') as file:
            file.write(client_public_key.save_pkcs1())
        file.close()

        with open(".private_key_client.txt",'wb') as file:
            file.write(client_private_key.save_pkcs1())
        file.close()

    def gen_serv_keys(self):
        serverr_public_key,serverr_private_key=rsa.newkeys(1024)

        with open(".public_key_server.txt",'wb') as file:
            file.write(serverr_public_key.save_pkcs1())
        file.close()

        with open(".private_key_server.txt",'wb') as file:
            file.write(serverr_private_key.save_pkcs1())
        file.close()


    def write_public_key_from_file(aim:str):
        with open(f".public_key_{aim}.txt", "rb") as file:
            public_key_str = file.read()
        file.close()
        return public_key_str

    def write_private_key_from_file(aim:str):
        with open(f".private_key_{aim}.txt", "rb") as file:
            private_key_str = file.read()
        file.close()
        return private_key_str