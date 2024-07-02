dolarHoje = 5.67
dolarOntem = 5.56
dolar = 5.67

print(f'A cotação do dólar hoje é {dolar}')
print(f'A cotação do dólar hoje é: {dolarHoje} e a cotação de otem era {dolarOntem}')

price = 59

txt = f"O preço é {price:.2f} em reais"
print(txt)

txt = f"Preço convertido em reais => {dolarHoje*300}"
print(txt)

txt = 'Todos os seres \n humanos são \'animais\''
print(txt)


#### métodos para tratar strings Iniciais Maiusculas
txt = 'edilson marcos ribeiro'
print(txt.capitalize())

firstName = 'edilson'
middleName = 'marcos'
lastName = 'ribeiro'
print(f'{firstName.capitalize()} {middleName.capitalize()} {lastName.capitalize()}' )

# transformando tudo em maiusculo
print(f'{firstName.upper()} {middleName.upper()} {lastName.upper()}' ) 

# transformando tudo em minusculo
print(f'{firstName.lower()} {middleName.lower()} {lastName.lower()}' )

# retorna a quantidade de vezes 
txt = 'Eu amo maçãs. A razão de eu gostar de maçãs é porque elas são saudáveis'
print(txt.count('maçã')) 

if txt.count('maçã') >= 2:
    print('palavra maçã aparece mais de 1 vez')
else:
    print('a palavra maçã aparece 1 ou nenhuma vez')

# este método procura por uma palavra dentro de uma string e retorna a posição
txt = 'A cidade de São Paulo é muito grande'
print(txt.find('muito'))

# este metodo verifica se a string contém somente números
a = 10
b = '20'
if b.isnumeric():
    c = a+int(b)
 
print(f'o valor da variável c é {c}')

####################################################################################
# trabalhando com listas 
####################################################################################

lista1 = ['HB20', 'ESCOSPORT', 'FIAT TORO', 'SPORTAGE', 'FORD KA', 'ACCORD']
print( lista1[3])

# trocando nomes das posições da lista
lista1[0:1] = ['RENEGADE', 'FUSCA']

# adicionando mais um item na lsita
lista1.append('MERIVA')

# ordena a lista
lista1.sort()

# looping para imprimir cada posição da lista
for i in lista1:
    print(f'O carro atual da lista é {i}')

