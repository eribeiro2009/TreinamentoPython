from Aula23 import *
import csv
import pandas as pd


def calculo(valor1:int, valor2:int):
    return valor1+valor2

a = calculo(10,20)

print(f" valor da variavel A => {a}")


def calculo(valor1:int, valor2:int):
    x = valor1+valor2
    return x

a = calculo(10,20)
print(f"valor da variável A => {a}")
a = calculo(20,30)
print(f"valor da variável A => {a}")
a = calculo(40,50)
print(f"valor da variável A => {a}")





##########################################
# traramento de erros
try:
    a = 10
    b = 0
    if int(0) == int(0):
        print("entrou no if")
        raise Exception("Erro de divisão por zero")
    c = a/b

except Exception as error:
    print("Erro no programa =>"+str(error))

    
print("depois do bloco try/exept")

f = open("arquivo.txt")
#print(f.read())
print(f.readline())
print(f.readline())
print(f.readline())

f.close()

# loop para ler linhas por linha
f = open("arquivo.txt")
for x in f:
    print(x)

## módulos no python
## módulos criados pelo programador 
## módulos de bibliotecas do python 

x = soma(10,20)
print(f"usou a função soma que pertence a aula 23 {x}")

x = media(20,30)
print
      
deptos = [10,20,30,50,60,70,80,90]

for i in deptos:
    print(f"Media salarial do departamento {i} => {calcula_media_salarial(i)}")


# trabalhando com arquivos csv
arquivo = open("empregados.csv")

leitor = csv.reader(arquivo,delimiter=";")
for linha in leitor:
    print(linha)

print(arquivo)

arquivo.close()

nome_usuario = input("Informe o nome do usuário:")
print(f"Nome do usuário é:{nome_usuario}")
 
arquivo = "empregados.csv"
df = pd.read_csv('empregados.csv', delimiter=";")
print(df)