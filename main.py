"""
Vadim Lepilov: CEO
David Cherednik: co-founder

MAHE: multi-platform accessible hacker environment
"""
# -*- coding: utf-8 -*- 
import sys
# import directory_brut.url_brut
import auxiliary.description as d
import directory_brut.url_brut as bru

d.ASCII_ART()

def main():
	while True:
		a = input('[MAHE] <=> ')
		# print(a)
		if a == "-help" or a == "-h":
			f = open('auxiliary/description.txt', 'r')
			print (f.read())
		if a == "scan":
			bru.call()
			break
		if a == 'exit': break



if(__name__ == '__main__'):
	main()



# import time
# import sys
# animation = "|/-\\"
# for i in range(100):
#     time.sleep(0.01)
#     sys.stdout.write(animation[i % len(animation)])
#     sys.stdout.flush()
# print("End!")
















