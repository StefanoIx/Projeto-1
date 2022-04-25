decrescente = True
numero = 1
valor = int(input("Digite o primeiro número da sequencia: "))
i = 0

while numero != 0 and decrescente:
        numero = int(input("Digite o proximo número da sequencia [%d]: " %(i+1)))
        if valor < numero or valor == numero: 
                decrescente = False
        i += 1
if decrescente == True:
	print ("A ordem é decrescente.")
else:
	print ("A ordem nao é decrescente.")
