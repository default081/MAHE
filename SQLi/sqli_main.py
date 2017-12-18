import sys
import urllib.request

def sqli_main():
		try:
			fullurl = input("-> Enter the URL: ")
			if(fullurl == "break" or fullurl == "back"):
				exit(0)
	
			try:
				resp = urllib.request.urlopen(fullurl)

				body = resp.read()

				fullbody = body.decode("utf-8")

				if("You have an error in your SQL syntax" in fullbody):
					print("this syte have a SQLI")
				else:
					print("this syte dosen`t have SQLI")
			except:
				print("    ->Error Whith URI")
				sqli_main()
		except KeyboardInterrupt:
			print("\n")
			sys.exit()

# sqli_main()
