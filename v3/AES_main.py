from AES import AES
from AES import unpad
from steg03 import StegEncrypt, StegDecrypt
from AES02 import Encryptor
import time

def main():

	# text = "Two One Nine TwoTwo One Nine abcd"
	# key = "Thats My Kung Fu"
	# iv = "given initializa"

	# obj = AES(key)
	# cipher = obj.encrypt_cbc(text,iv)
	# enctext = ""
	# for i in cipher:
	# 	for j in i:
	# 		enctext +=chr(j)

	# print(enctext)
	# StegEncrypt("tiger.png",enctext,"enc_tiger.png")


	# clear_text = StegDecrypt("enc_tiger.png")

	# decrypt_key = "Thats My Kung Fu"
	# iv = "given initializa"
	# obj = AES(key)
	# msg = obj.decrypt_cbc(clear_text,iv)
	# msgstr = ""
	# for i in msg:
	# 	for j in i:
	# 		msgstr +=chr(j)

	# print(unpad(msgstr))

	text = "Hi There!!! This is the secret message"
	key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
	enc = Encryptor(key)

	cipher = enc.encrypt(text,key)
	print(cipher)
	# StegEncrypt("tiger.png", cipher, "enc_tiger.png")

	# clear_cipher = StegDecrypt("enc_tiger.png")
	# time.sleep(5)

	clear_text = enc.decrypt(cipher,key)

	print(str(clear_text))


main()
