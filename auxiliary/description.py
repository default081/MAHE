VERSION = 0.01

def ASCII_ART():
	print(VERSION)
	print("Created by Vadim Lepilov and David Cherednik")
	print ("""                                           
 ****     ****     **     **      ** ********
/**/**   **/**    ****   /**     /**/**///// 
/**//** ** /**   **//**  /**     /**/**      
/** //***  /**  **  //** /**********/******* 
/**  //*   /** **********/**//////**/**////  
/**   /    /**/**//////**/**     /**/**      
/**        /**/**     /**/**     /**/********
//         // //      // //      // ////////                                                 
""")

def help():
	f = open('description.txt', 'r')
	print (f.read())
# help()