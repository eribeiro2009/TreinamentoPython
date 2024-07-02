"""
este é um comentario de mutiplas linhas

hoje vamos trabalhar com string
"""

a = "Hello World"

#imprime o array completo da string
print(a)

#imprime o array da string na posição 5
print(a[5])

#imprime o array da string começnado na posição zero até a posição 10
print(a[0:10])

carros = ["Sportage", "EcoSport", "Spin"]
print(carros[2])

a = """ Esta é umas string bem longa
que possui várias linhas
que podem ser lidas e imprimidas
"""

print (a)

###########################################################################################
# fazendo looping
###########################################################################################

a = "banana" 
for x in a:
    print(x)
    print('Está dentro do loop')
print("Fora do loop")

############################################################################################
# verificar o tamanho de uma string
a = "Hoje na cidade de São Paulo está um dia ensolarado"

# função len() retorna o tamanho de uma string
print(len(a))

############################################################################################
# verifica se existe um caracter ou string numa string => função in
txt = "As melhores coisas da vida é a liberdade"
print("liberdade" in txt)
print("beleza" in txt)

if "liberdade" in txt:
    print("achou a palavra")
else:
    print("não achou a palavra")

if "laranja" not in txt:
    print("não achou essa palavra")
else:
    print("achou essa palavra")

# slicing de string
#imprime a string completa
print(txt)

#imprime da posição 0 até a posição 10
print(txt[0:10])

# imprime do inicio até a posição 5
print(txt[:5]) 

# imprime a partir da posição 5
print(txt[5:])

print(txt[-5:-2])


##########################################################################################
# modificando uma string
##########################################################################################
# um igual = é atribuição
# dois iguais seguidos == é sinal de comparação

a = "Edilson"
b = "edilson"

print(a.upper() == b.upper())
print(a.lower() == b.lower())


"""
upper transforma em maíusculo
lower trasforma em minúsculo
forma de uso

variavel_string.upper()
variavel_string.lower()
exemplo:
a.upper()
b.lower()
 
"""

#########################################################################################
# removendo espaços em branco

a = "    Olá Mundo  "
b = " Bom dia"
print(a+b)
print(a.strip()+b.strip())

print("o valor da variável a é"+a)

# f string
print(f"o valor da variável a é {a}")
print(f"os valores das variaveis {a} {b}")

x = f"o valor da variável a é {a}"
print(x)

# usando f para formatar casas decimais
price = 59 # int
print(type(price))
txt = f"O preço é {price:.2f}" # float
print(txt)
price2 = float(price)
print(price)
print(price2)