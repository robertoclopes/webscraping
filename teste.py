'''
idade = 10

if idade >= 18:
	print("maior")
else:
	print("menor")
'''
'''
arq = open('arquivo.txt', 'w')
arq.write('python is nice\n')
arq.write('curso de bs4')
arq.close()
'''
'''
arq = open('arquivo.txt', 'r')
print(arq.read())
arq.close()
'''
'''
with open('arquivo.txt', 'r') as f:
	print(f.read())
'''
'''
cont = 1
while cont <= 10:
	print('mensagem',cont)
	cont += 1
'''
'''
for _ in range(1, 10, 2):	#1 ate 10 de 2 em 2
	print('mensagem2')
'''
def media(n1,n2):
	media = (n1+n2)/2
	return media

r=media(10,20)
print(r)