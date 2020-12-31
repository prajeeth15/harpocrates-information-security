from steg03 import StegEncrypt,StegDecrypt
from blowfish import Blowfish

def main():

	pt = "Hi There!!! This is the secret message"
	print("secret message:",pt)
	blowfish = Blowfish("dsadasdasda", pt)
	ct = blowfish.encrypt(pt)
	print("encrypted message:",ct)
	StegEncrypt("tiger.png", ct, "enc_tiger.png")

	ct = StegDecrypt("enc_tiger.png")
	pt = blowfish.decrypt(ct)
	print("decrypted message:",pt)

main()
