"""
Vadim Lepilov: CEO
David Cherednik: co-founder

MAHE: multi-platform accessible hacker environment
"""
# -*- coding: utf-8 -*- 
import sys
import os

import auxiliary.description as desc
import directory_brut.url_brut as brut
import admin_serach.admin as admin
import hash_brut.hash_main as hash_crack
import site_info as site_info
import SQLi as SQLi
import site_info.main_info as header

os.system('clear')

desc.ASCII_ART()

def main():
    try:
        while True:
            a = input('[MAHE] <=> ')
            if(a == "adm search"): #admin fazzer
                admin.admin_main()
            if (a == "scan"): #directory brut
                brut.call()
            if(a == "decode hash"):
                hash_crack.main()
            if (a == "get info"):
                header.main_info()
			# if(a == "combine"):
			# 	com.main()

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









