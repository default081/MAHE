# -*- coding: utf-8 -*- 
import urllib
import threading
from datetime import datetime
def test1():
	File = open("dict1.txt", 'r') 
	for line in File:
		a = 'http://maulnet.ru/' + line
		url=urllib.urlopen(a)
		if url.code == 200:
			print a, url.code, "--Ditrctoty available"
			print "-------*--------"
		elif url.code == 404:
			print a, url.code ,"--error"
			print "-------*--------"

def test2():
	File = open("dict2.txt", 'r') 
	for line in File:
		a = 'http://maulnet.ru/' + line
		url=urllib.urlopen(a)
		if url.code == 200:
			print a, url.code, "--Ditrctoty available"
			print "-------*--------"
		elif url.code == 404:
			print a, url.code ,"--error"
			print "-------*--------"



start_time = datetime.now()
# test1()
e1 = threading.Event()
e2 = threading.Event()


t1 = threading.Thread(target=test1)
t2 = threading.Thread(target=test2)


t1.start()
t2.start()

e1.set() 


t1.join()
t2.join()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))



