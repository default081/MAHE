# -*- coding: utf-8 -*-

import hashlib
import sys

def md5_brut():
	pass_in = input("-> Enter the MD5 Hash: ")
	pwfile = input("-> Enter the Password Dictionary: ")

	try:
		if(pwfile == "default"):
			pwfile = open("dict/password.txt", "r",  encoding='utf-8', errors='ignore')
		else:
			pwfile = open(pwfile, "r", encoding='utf-8', errors='ignore')

	except:
		print("Dictionary doesn't find or doesn't exist.")

	for password in pwfile:
		fileemd5 = hashlib.md5(password.encode().strip()).hexdigest()
		# print("trying password number %s " %(password.encode()) + fileemd5)	
			
		if (pass_in == fileemd5):
			print("\n Match found. \n Password is: %s" % password)
			break
		else:
			pass
# md5_brut()


# e10adc3949ba59abbe56e057f20f883e == 123456
# # df3939f11965e7e75dbc046cd9af1c67  == dad
# # 5f4dcc3b5aa765d61d8327deb882cf99  == password
# d8578edf8458ce06fbc5bb76a58c5ca4 == qwerty


























# import md5
# import sys

# counter = 0

# def md5_brut():
# 	pass_in = raw_input("-> Enter the MD5 Hash: ")
# 	pwfile = raw_input("-> Enter the Password Dictionary: ")

# 	try:
# 		if(pwfile == "default"):
# 			pwfile = open("/root/prog/pycode/MAHE/auxiliary/dictionary/password.txt", "r")
# 		else:
# 			pwfile = open(pwfile, "r")

# 	except:
# 		print("Dictionary doesn't find or doesn't exist.")

# 	for password in pwfile:
# 		fileemd5 = md5.new(password.strip()).hexdigest()
# 		print("trying password number %s" %(password.strip()) + fileemd5)		

# 		if (pass_in == fileemd5):
# 			print("\n Match found. \n Password is: %s" % password)
# 			break

# 		else:
# 			print("-----password not found")
# md5_brut()