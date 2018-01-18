import datetime
from termcolor import colored, cprint
import sys
from . import ascii_art as art

version = 0.01

def ASCII_ART():
	RED   = "\033[1;31m"
	RESET = "\033[0;0m"
	sys.stdout.write(RED)
	print("Current version: " + str(version))	
	sys.stdout.write(RESET)
	
	print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	art.ascii_a()

def help():
	descript_file = open('auxiliary/description.txt', 'r')
	print (descript_file.read())




""" 
     ☺/ <~~{hello, what do u whant to do?}
    /[]
     /\
    ☺/ <~~{╔╦╦╦═╦╗╔═╦═╦══╦═╗}             
   /[]	  {║║║║╩╣╚╣═╣║║║║║╩╣}             
    /\    {╚══╩═╩═╩═╩═╩╩╩╩═╝}   

"""



