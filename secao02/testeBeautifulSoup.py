from bs4 import BeautifulSoup

with open('arquivo.html','r') as f:
	soup_string = BeautifulSoup(f.read(),'html.parser')	#html.parser eh o parser padrao do beautiful soup
	print(soup_string)