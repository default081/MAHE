import sys
import urllib.request

# fullurl = input("Enter the URL: ")
fullurl = "https://www.youtube.com/"

resp = urllib.request.urlopen(fullurl)

body = resp.read()

fullbody = body.decode("utf-8")

if("You have an error in your SQL syntax" in fullbody):
	print("this syte have a SQLI")
else:
	print("this syte dosen`t have SQLI")

# print (fullbody)