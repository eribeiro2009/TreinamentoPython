# funções

def exibe_mensagem(pmensagem1: str,
                   pmensagem2: str, 
                   pmensagem3: str = "mensagem vazia"):
    print(f"exibindo as 2 mensagens : {pmensagem1} e {pmensagem2}")

# chama a função exibe_mensagem
exibe_mensagem("Olá Mundo", "segunda mensagem")
exibe_mensagem("Olá tudo bem?", "segunda mensagem")
exibe_mensagem("Bora jogar bola", "segunda mensagem")
pmsg1 = "Que tal o tempo hoje?", "segunda mensagem"
pmsg2 = "Que tal o tempo amanhã?"
exibe_mensagem(pmsg1, pmsg2)



def soma(valor1:int, valor2:int):
    resultado = valor1+valor2
    print(resultado)

#chama a função soma()
soma(50,100)

def soma(valor1:int, valor2:int):
    resultado = valor1+valor2
    return resultado
    #exibe_mensagem("O resultado", "da conta é", resultado)

def media(valor1, valor2):
    media = soma(valor1, valor2)/2 
    exibe_mensagem("o resultado", "da média é:", media)
    return media
#chama a função soma() enviando parâmetros de forma explícita
soma(50,100)

#chama a função media() enviando parâmetros de forma posicional
media(10,20)

"""
    para funções:
     funções que recebem parâmetro
     funções que recebem parâmetros de forma posicinal
     funções que recebem parâmetros de forma declarada 
     funções que chama outras funções 

"""
####################################################################################################
# tratamento de erros
try:
    a = 10
    b = 0
    if b == 0:
        raise Exception("Erro divisão por zero")
    else:
        c = a/b
except:
    print("erro de calculo")
finally:
    print("final do bloco com erro ou sem erro")


######################################################################################################
# trabalhando com arquivos
######################################################################################################
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