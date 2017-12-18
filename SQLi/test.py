

import re
import requests
url = "http://www.tunesoman.com/product.php?id=200%27"
r = requests.get(url).text 
print (r)
strings = ['MySQL', 'one']
 
for string in strings:
    match = re.search(string, r)
    if match:
        print('Found "{}" in "{}"'.format(string, r))
        text_pos = match.span()
        print(r[match.start():match.end()])
    else:
        print('Did not find "{}"'.format(string))