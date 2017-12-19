# import requests
# import re
# def define():
# 	url = "http://localhost/wp_test/"
# 	r = requests.get(url).text 
# 	# print (r)
# 	strings = ['<meta name=»generator» content=»WordPress 3.5>', 'test']

# 	for string in strings:
#     match = re.search(string, r)
#     if match:
#         print('Found "{}" in "{}"'.format(string, r))
#         text_pos = match.span()
#         print(r[match.start():match.end()])
#     else:
#         print('Did not find "{}"'.format(string))

# define()
# ---------------------------------------------------
# import re
# import requests
# url = "http://localhost/wp_test/"
# r = requests.get(url).text 
# print (r)
# strings = ['MySQL', 'one']
 
# for string in strings:
#     match = re.search(string, r)
#     if match:
#         print('Found "{}" in "{}"'.format(string, r))
#         text_pos = match.span()
#         print(r[match.start():match.end()])
#     else:
#         print('Did not find "{}"'.format(string))
#         
#--------------------------------------------------
import requests
file = open("testfile.txt","w") 

r = requests.get('https://www.tutorialspoint.com')

file.write(str(r.headers))
file.close() 

a = open("testfile.txt","r")
print (a.read().replace(", ", "\n"))
a.close() 









