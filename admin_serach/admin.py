import urllib.request
import threading
from datetime import datetime
import sys

event = threading.Event()
event2 = threading.Event()

def brut_part_1(ev, urll, d1):

	if(d1 == "default"):
		File = open("dict/admin-panels2.txt", "r")
	else:
		File = open(d1, "r", encoding='utf-8', errors='ignore')

	for line in File:
		addres = urll + line

		try:
			url = urllib.request.urlopen(addres)
			if(url.code == 200):
				print(addres, url.code, "--Admin panel find")
				print ("-------*--------")

		except urllib.error.HTTPError as error:
			if(error.code != 200):
				pass
				# print(addres, error.code, "--Error")
				# print ("-------*--------")


def brut_part_two(ev, urll, d2):

	if(d2 == "default"):
		File = open("dict/admin-panels2.txt", "r")
	else:
		File = open(d2, "r", encoding='utf-8', errors='ignore')

	for line in File:
		addres = urll + line

		try:
			url = urllib.request.urlopen(addres)
			if(url.code == 200):
				print(addres, url.code, "--Admin panel find")
				print ("-------*--------")

		except urllib.error.HTTPError as error:
			if(error.code != 200):
				pass
				# print(addres, error.code, "--Error")
				# print ("-------*--------")


def admin_main():
	start_time = datetime.now()
	syte = input("-> Enter URI: ")
	dict1 = input(" -> Please enter the first dictionary: ")
	dict2 = input(" -> Please enter the second dictionary: ")
	thr = threading.Thread(target=brut_part_1, args=(event, syte, dict1)) # initiate threading n1
	thr2 = threading.Thread(target=brut_part_two, args=(event2, syte, dict2)) #initiate threading n2

	thr.daemon = True
	thr2.daemon = True
	 
	thr.start()
	thr2.start()

	while True: #
	    thr.join(600)
	    thr.join(600)
	    if not thr.isAlive():
	        break

	end_time = datetime.now()
	print('Duration: {}'.format(end_time - start_time))

# admin_main()