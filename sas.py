from urllib.request import urlopen
from bs4 import BeautifulSoup
from sys import argv

banner = '''                                                                                                                                                     
 #### #   #   #   ##### #   # #   #   #   #####      #### #   # ####    #   ##### ##### ####  
#     #   #  # #  #   # #   #  # #   # #    #       #     #   # #   #  # #  #   # #     #   # 
#     ##### ##### #   #  ####   #   #####   #       #      #### ####  ##### #   # ####  ####  
#     #   # #   # #   #     #  # #  #   #   #       #         # #     #   # #   # #     #     
 #### #   # #   # #   #     # #   # #   #   #        ####     # #     #   # #   # ##### #      
'''

license = '''
Copyright 2022 Ahmet Yigit Aydeniz

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

FNRM = "\x1B[0m"
FRED = "\x1B[31m"
FGRN = "\x1B[32m"
FYEL = "\x1B[33m"
FBLU = "\x1B[34m"
FMAG = "\x1B[35m"
FCYN = "\x1B[36m"
FWHT = "\x1B[37m"

BNRM = "\x1B[0m"
BRED = "\x1B[41m"
BGRN = "\x1B[42m"
BYEL = "\x1B[43m"
BBLU = "\x1B[44m"
BMAG = "\x1B[45m"
BCYN = "\x1B[46m"
BWHT = "\x1B[47m"

def parse_scripts(link):

	HTML = urlopen(link)
	soup = BeautifulSoup (HTML.read(), 'html.parser')

	print("parsing scripts:\n")

	list_ = [dictionary.get('src') for dictionary in soup.find_all('script') if dictionary.get('src')]

	for script_src in list_ :
		print(script_src)

	print("\n"+BGRN+"[Done !!!]"+BNRM+"\n")

def get_msg(link):

	inv = str(link)

	print('sending http request to the:\n' + inv)

	meta = urlopen(link)
	
	print('\nparsing http-return-message\n')
	
	u = meta.info()
	
	print(u)
	print("\n"+BGRN+"[Account Exist]"+BNRM+"\n")


def main(link):
	
	print(banner)
	print(license)
	try:
		parse_scripts(link)
		get_msg(link)
	except:
		print(BRED+"\n[Account Not Found]\n"+BNRM)

username = str(input("\nenter a username:"))

main("https://www.snapchat.com/add/"+username)
