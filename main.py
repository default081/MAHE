"""
Vadim Lepilov: CEO
David Cherednik: co-founder

MAHE: multi-platform accessible hacker environment
"""
# -*- coding: utf-8 -*- 
import sys
import os
import keyboard 

import auxiliary.description as desc
import directory_brut.url_brut as brut
import admin_serach.admin as admin
import md5_brut.md5_main as md5_crack

desc.ASCII_ART()

def main():
	try:
		while True:
			a = input('[MAHE] <=> ')

			if (a == "adm search"): #admin fazzer
				admin.admin_main()

			if (a == "scan"): #directory brut
				brut.call()

			if (a == "md5 compare"): #md5 hash compare
				md5_crack.md5_brut()

			
			if (a == 'exit' or a == "quit"): 
				break
			if (a == "-help" or a == "-h"):
				desc.help()
			if (a == "clear"):
				os.system('clear')

	except KeyboardInterrupt:
		print("\n")
		sys.exit()

main()


#TODO
#определение версии ОС
#определение платформы и технологий
#поиск всех доменов и субдоменов
#порты
#поиск shared hosting












