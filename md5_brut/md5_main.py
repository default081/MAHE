# -*- coding: utf-8 -*-

import hashlib
import sys

counter = 0

def md5_brut():
	pass_in = input("-> Enter the MD5 Hash: ")
	pwfile = input("-> Enter the Password Dictionary: ")

	try:
		if(pwfile == "default"):
			pwfile = open("/root/prog/pycode/MAHE/auxiliary/dictionary/password.txt", "r")
			pwfile.encoding("utf-8")
		else:
			pwfile = open(pwfile, "r", encoding='utf-8')
			pwfile.encoding("utf-8")

	except:
		print("Dictionary doesn't find or doesn't exist.")

	for password in pwfile:
		fileemd5 = hashlib.md5(password.encode()).hexdigest()

		print("trying password number %s" %(password.encode()) + fileemd5)		

		if (pass_in == fileemd5):
			print("\n Match found. \n Password is: %s" % password)
			break

		else:
			print("-----password not found")
# md5_brut()


# e10adc3949ba59abbe56e057f20f883e == 123456
# # df3939f11965e7e75dbc046cd9af1c67  == dad
# # 5f4dcc3b5aa765d61d8327deb882cf99  == password
# /root/prog/pycode/MAHE/md5_brut/dict.txt
# /root/prog/pycode/MAHE/auxiliary/dictionary/password.txt
# 
# 
# password 286755fad04869ca523320acce0dc6a4

# import hashlib
# import time 

# counter = 0

# def md5_brut():
# 	pass_in = input("-> Enter the MD5 Hash: ")
# 	pwfile = input("-> Enter the Password Dictionary: ")
# 	# file = input("-> Enter the Password Dictionary: ")

# 	try:
# 		if(pwfile == "default"):
# 			pwfile = open("/root/prog/pycode/MAHE/md5_brut/dict.txt", "r")
# 		else:
# 			pwfile = open(pwfile, "r", encoding='utf-8')

# 	except:
# 		print("Dictionary doesn't find or doesn't exist.")

# 	for password in pwfile:
# 		# time.sleep(1)
# 		fileemd5 = hashlib.md5(password.encode()).hexdigest()
# 		print("trying password number %s " %(password.strip()) + fileemd5)		

# 		if (pass_in == fileemd5):
# 			print("\n Match found. \n Password is: %s" % password)
# 			break
# 			sys.exit()

# 		else:
# 			print("-----password not found")


# md5_brut()


# e10adc3949ba59abbe56e057f20f883e == 123456
# # df3939f11965e7e75dbc046cd9af1c67  == dad
# # 5f4dcc3b5aa765d61d8327deb882cf99  == password
# /root/prog/pycode/MAHE/md5_brut/dict.txt
# /root/prog/pycode/MAHE/auxiliary/dictionary/password.txt
# 

# import hashlib
# import time 

# counter = 0
# a = "password"
# fileemd5 = hashlib.md5(a.encode()).hexdigest()
# print(fileemd5)

# def md5_brut():
# 	pass_in = input("-> Enter the MD5 Hash: ")
# 	pwfile = input("-> Enter the Password Dictionary: ")

# 	try:
# 	# 	if(pwfile == "default"):
# 	# 		pwfile = open("/root/prog/pycode/MAHE/md5_brut/dict.txt", "r")
# 	# 	else:
# 	# 		pwfile = open(pwfile, "r", encoding='utf-8')
# 		pwfile = open("/root/prog/pycode/MAHE/md5_brut/dict.txt", "r", encode="utf-8")
# 	except:
# 		print("Dictionary doesn't find or doesn't exist.")

# 	for password in pwfile:
# 		fileemd5 = hashlib.md5(password.encode()).hexdigest()
# 		print("trying password number %s " %(password.strip()) + fileemd5)		

# 		if (pass_in == fileemd5):
# 			print("\n Match found. \n Password is: %s" % password)
# 			break
# 			sys.exit()

# 		else:
# 			print("-----password not found")


# md5_brut()


# e10adc3949ba59abbe56e057f20f883e == 123456
# # df3939f11965e7e75dbc046cd9af1c67  == dad
# # 5f4dcc3b5aa765d61d8327deb882cf99  == password
# /root/prog/pycode/MAHE/md5_brut/dict.txt
# /root/prog/pycode/MAHE/auxiliary/dictionary/password.txt
































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