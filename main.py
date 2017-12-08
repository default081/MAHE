"""
Vadim Lepilov: CEO
David Cherednik: co-founder

MAHE: multi-platform accessible hacker environment
"""
# -*- coding: utf-8 -*- 
import sys
import auxiliary.description as d
import directory_brut.url_brut as bru

d.ASCII_ART()

def main():
	while True:
		a = input('[MAHE] <=> ')
		# print(a)
		if a == "-help" or a == "-h":
			d.help()
		if a == "scan":
			bru.call()
			break
		if a == 'exit': break



if(__name__ == '__main__'):
	main()
















