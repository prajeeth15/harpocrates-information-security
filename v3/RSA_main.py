from RSA03 import encrypt,decrypt
from steg03 import StegEncrypt,StegDecrypt

def main():

	message = "Hi There!!!"
	cipher = encrypt(message)
	print("encrypted message:",cipher)
	StegEncrypt("tiger1.png", cipher, "enc_tiger1.png")

	clear_cipher = StegDecrypt("enc_tiger1.png")
	res = decrypt(clear_cipher)

	print("decrypted message:",res)

if __name__=="__main__":
	main()
