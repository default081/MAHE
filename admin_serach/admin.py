import urllib.request
import threading
from datetime import datetime
import sys

event = threading.Event()
event2 = threading.Event()

def brut_part_1(ev):
	File = open("../auxiliary/dictionary/admin-panels.txt", "r")
	for line in File:
		addres = 'http://maulnet.ru/' + line
		try:
			url = urllib.request.urlopen(addres)
			if(url.code == 200):
				print(addres, url.code, "--Admin panel find")
		except urllib.error.HTTPError as error:
			pass


# def brut_part_two(ev):
# 	File = open("auxiliary/dictionary/admin-panels.txt", "r")
# 	for line in File:
# 		addres = 'http://maulnet.ru/' + line
# 		try:
# 			url = urllib.request.urlopen(address)
# 			if(url.code == 200):
# 				print(address, url.code, "--Admin panel find")
# 		except urllib.error.HTTPError as error:
# 			pass


def admin_main():
	start_time = datetime.now()

	thr = threading.Thread(target=brut_part_1, args=(event, )) # initiate threading n1
	# thr2 = threading.Thread(target=func2, args=(event2, )) #initiate threading n2

	thr.daemon = True
	# thr2.daemon = True
	 
	thr.start()
	# thr2.start()

	while True: #
	    thr.join(600)
	    # thr.join(600)
	    if not thr.isAlive():
	        break

	end_time = datetime.now()
	print('Duration: {}'.format(end_time - start_time))

admin_main()