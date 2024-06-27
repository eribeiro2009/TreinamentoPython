#este é um cometário
# para cada linha de um comentário precisa ter um # na frente

x = 15
y = "John Wayne"
print("Este é o valor de x =>", x)
print("Este é o valor de y =>", y)
print(f"Este é o valor de y => {y}")
print(f"Estes são os valores de x e y => {x} {y}")
print("Hello World!") #a partir daqui é um cometário

# regras para nomes de variável
# não pode começar com número -- sempre começa com letra a2
# não pode ter simbolo... 
# não pode ter traço -
# não poder ter espaço no nome da variável nome_emp

# como atribuir valores a uma variável

x, y, z = "Laranja", "Banana", "Melancia"
print(x,y,z)

x = y = z = "Laranja"
print(x,y,z)

# analisando data type
# data types numéricos
# int, float, complex

x = 1 #int
y = 2.8 #float
z = 1j #complex

print(type(x))
print(type(y))
print(type(z))

# casting = muda o data type de uma variável
x = int(1)
y = int(2.8)
z = int("3")
print(x,y,z)

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x,y,z,w)

# strings
x = str("s1")
y = str(2)
a = 3.2
z = str(a)
print(x,y,z)

