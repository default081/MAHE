# import md5
import hashlib

counter = 0

def md5_brut():
	pass_in = input("Enter the MD5 Hash: ")
	pwfile = input("Enter the Password Dictionary: ")

	try:
		pwfile = open(pwfile, "r", encoding='utf-8')

	except:
		print("Dictionary doesn't find or doesn't exist.")

	for password in pwfile:
		fileemd5 = hashlib.md5(password.encode()).hexdigest()
		print("trying password number %s" %(password.strip()))		
		# print("trying password number %d %s" %(counter, password.strip()))		
		# counter += 1mkvfmslgjkvfnslgjvf

		if pass_in == fileemd5:
			print("\n Match found. \n Password is: %s" % password)
			break

		else:
			print("-----password not found")

md5_brut()
# df3939f11965e7e75dbc046cd9af1c67  == dad
# /root/prog/pycode/MAHE/md5_brut/dict.txt


