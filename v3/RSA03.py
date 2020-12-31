import random

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def xgcd(a, b):
    x, old_x = 0,1
    y, old_y = 1, 0

    while(b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y

def chooseE(totient):
    while(True):
        e = random.randrange(2, totient)

        if gcd(e, totient) == 1:
            return e

def encrypt(message, file_name = 'public_keys.txt', block_size = 2):
    try:
        fo = open(file_name, 'r')
    except FileNotFoundError:
        print('The file is not found')
    else:
        n = int(fo.readline())
        e = int(fo.readline())
        fo.close()

        encrypted_blocks = []
        ciphertext = -1

        if len(message) > 0:
            ciphertext = ord(message[0])

        for i in range(1, len(message)):
            if i % block_size == 0:
                encrypted_blocks.append(ciphertext)
                ciphertext = 0

            ciphertext = ciphertext * 1000 + ord(message[i])

        encrypted_blocks.append(ciphertext)

        for i in range(len(encrypted_blocks)):
            encrypted_blocks[i] = str((encrypted_blocks[i]**e) % n)

        encrypted_message = " ".join(encrypted_blocks)

        return encrypted_message

def decrypt(blocks, block_size = 2):
    fo = open('private_keys.txt', 'r')
    n = int(fo.readline())
    d = int(fo.readline())
    fo.close()

    list_blocks = blocks.split(' ')
    int_blocks = []

    for s in list_blocks:
        int_blocks.append(int(s))

    message = ""

    for i in range(len(int_blocks)):
        int_blocks[i] = (int_blocks[i]**d) % n

        tmp = ""

        for c in range(block_size):
            tmp = chr(int_blocks[i] % 1000) + tmp
            int_blocks[i] //= 1000

        message += tmp

    return message


# def main():

#     # while True:
#     #     ch = int(input("Choice:"))
#     #     if ch==1:
#     #         message = "Hi There!!!"
#     #         x = encrypt(message)
#     #         print(x)
#     #     elif ch==2:
#     #         x = input("Cipher:")
#     #         res = decrypt(x)
#     #         print(res)
#     #     elif ch==3:
#     #         break
        
#     message = "Hi There!!!"
#     x = encrypt(message)
#     print(x)
#     res = decrypt(x)
#     print(res)
  

# main()

