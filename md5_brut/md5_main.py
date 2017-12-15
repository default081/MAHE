# import hashlib
# import sys

# counter = 0

# def md5_brut():
# 	pass_in = input("-> Enter the MD5 Hash: ")
# 	pwfile = input("-> Enter the Password Dictionary: ")
# 	# file = input("-> Enter the Password Dictionary: ")

# 	try:
# 		# if(file == "default"):
# 		# 	pwfile = open("/root/prog/pycode/MAHE/md5_brut/dict.txt", "r", encoding="utf-8")
# 		# elif(file != "default"):
# 		pwfile = open(pwfile, "r", encoding='utf-8')
# 	except:
# 		print("Dictionary doesn't find or doesn't exist.")

# 	for password in pwfile:
# 		fileemd5 = hashlib.md5(password.encode()).hexdigest()
# 		print("trying password number %s" %(password.strip()))		

# 		if (pass_in == fileemd5):
# 			print("\n Match found. \n Password is: %s" % password)
# 			break

# 		else:
# 			print("-----password not found")


# e10adc3949ba59abbe56e057f20f883e == 123456
# # df3939f11965e7e75dbc046cd9af1c67  == dad
# # 5f4dcc3b5aa765d61d8327deb882cf99  == password
# /root/prog/pycode/MAHE/md5_brut/dict.txt
# /root/prog/pycode/MAHE/auxiliary/dictionary/password.txt

import hashlib
import time 

counter = 0

def md5_brut():
	pass_in = input("-> Enter the MD5 Hash: ")
	# pwfile = input("-> Enter the Password Dictionary: ")
	file = input("-> Enter the Password Dictionary: ")

	try:
		if(file == "default"):
			pwfile = open("/root/prog/pycode/MAHE/md5_brut/dict.txt", "r", encoding="ISO-8859-1")
		else:
			pwfile = open(pwfile, "r", encoding='utf-8')

	except:
		print("Dictionary doesn't find or doesn't exist.")

	for password in pwfile:
		time.sleep(1)
		fileemd5 = hashlib.md5(password.encode()).hexdigest()
		print("trying password number %s " %(password.strip()) + fileemd5)		

		if (pass_in == fileemd5):
			print("\n Match found. \n Password is: %s" % password)
			break
			sys.exit()

		else:
			print("-----password not found")


# md5_brut()