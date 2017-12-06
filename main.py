"""
Vadim Lepilov: CEO
David Cherednik: 

MAHE: multi-platform accessible hacker environment
"""
# -*- coding: utf-8 -*- 
import sys
import auxiliary.description as d

d.ASCII_ART()

def main():
	while True:
		a = input('[MAHE] <=> ')
		print(a)
		if a == "-help" or a == "-h":
			# print(d.help())
			f = open('auxiliary/description.txt', 'r')
			print (f.read())	
		if a == 'exit': break

main()



# import time
# import sys
# animation = "|/-\\"
# for i in range(100):
#     time.sleep(0.01)
#     sys.stdout.write(animation[i % len(animation)])
#     sys.stdout.flush()
# print("End!")
















