# from PIL import Image
from stegano import lsb

def StegEncrypt(orig_image_file, messsage, encoded_image_file):
	# img = Image.open(orig_image_file)
	# encoded_image_file = "enc_" + orig_image_file
	img_encoded = lsb.hide(orig_image_file, messsage)
	img_encoded.save(encoded_image_file)

def StegDecrypt(encoded_image_file):
	clear_message = lsb.reveal(encoded_image_file)
	return clear_message


# def main():

# 	messsage = "Hello There!!"
# 	orig_image_file = "tiger.png"

# 	StegEncrypt(orig_image_file, messsage)

# 	encoded_image_file = "enc_tiger.png"

# 	res = StegDecrypt(encoded_image_file)
# 	print(res)

# main()




