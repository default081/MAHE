import datetime
# from termcolor import colored, cprint
import sys


version = 0.01

def ASCII_ART():
	# RED   = "\033[1;31m"
	# RESET = "\033[0;0m"
	# sys.stdout.write(RED)
	print("Current version: " + str(version))	
	# sys.stdout.write(RESET)
	
	print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	print ("""
	███╗   ███╗ █████╗ ██╗  ██╗███████╗	   
	████╗ ████║██╔══██╗██║  ██║██╔════╝    
	██╔████╔██║███████║███████║█████╗        
	██║╚██╔╝██║██╔══██║██╔══██║██╔══╝      
	██║ ╚═╝ ██║██║  ██║██║  ██║███████╗    
	╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    
	               .-'''''-.
	             .'         `.
	            :             :
	           :               :
	           :      _/|      :
	            :   =/_/      :
	             `._/ |     .'
	          (   /  ,|...-'
	           \_/^\/||__
	        _/~  `""~`"` \_
	     __/  -'/  `-._ `\_\__
	   /     /-'`  `\   \  \-.\
    
""")

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

               .-'''''-.
             .'         `.
            :             :
           :               :
           :      _/|      :
            :   =/_/      :
             `._/ |     .'
          (   /  ,|...-'
           \_/^\/||__
        _/~  `""~`"` \_
     __/  -'/  `-._ `\_\__
   /     /-'`  `\   \  \-.\


"""



