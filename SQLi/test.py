

# import re
# import requests
# url = "http://www.tunesoman.com/product.php?id=200%27"
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

# -----------------------------------------------------------------------------------------------

import requests
with requests.Session() as session:
    url = "http://192.168.1.22/bWAPP/login.php" # Ваш URL с формами логина
    LOGIN = "bee" # Ваш логин
    PASSWORD = "box" # Ваш пароль
    dann = dict(login = LOGIN, password = PASSWORD) # Данные в виде словаря, которые будут отправляться в POST
    session.get(url) # Получаем страницу с формой логина
    session.post(url, dann) # Отправляем данные в POST, в session записываются наши куки
    url2 = "http://192.168.1.22/bWAPP/portal.php" # Ваш второй URL - тот с которого вам нужно спарсить данные
    r = session.get(url2) # Все! Вы получили Response. Поскольку в session записались куки авторизации - при вызове метода get() с этой сессии в Request отправляются ваши куки.
print(r.text)