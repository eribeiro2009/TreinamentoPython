
# lista usada 
lista = ["Brasil", "Estados Unidos", "China", "Japão"]

# remove um item da lista 
lista.remove("Brasil")
print(lista)

# remove um item de uma posição especifíca (index)
lista.pop(0)
print(lista)

#se não indicar qual o index remove o último
lista.pop()
print(lista)

# deleta um item de uma posição index específica
lista = ["Brasil", "Estados Unidos", "China", "Japão"]
del lista[0]
print(lista)

# deleta a variável lista
del lista
#print(lista) # não funciona pois a variávvel foi excluida

lista = ["Brasil", "Estados Unidos", "China", "Japão"]

# limpa todos os elementos da lista dexando-a vazia
lista.clear()
print(f"Tenta imprimir a lista vazia => {lista}")

# fazendo um looping  numa lista usando While
lista = ["Brasil", "Estados Unidos", "China", "Japão"] 
for i in lista:
    print(i)

# fazendo a mesma coisa usando while
i = 0
print(len(lista))
while i < len(lista):
    print(lista[i])
    print(f"valor atual do i =>{i}")
    i = i + 1

frutas = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in frutas:
    if "a" in x:
        newlist.append(x)

print(f"Imprime o conteudo da nova lista {newlist}")

for x in newlist:
    print(f"imprime o elemento atual da lista {x.upper()}")

# ordenando uma lista
novalista = [100,50,65,82,23,38]
novalista.sort()
print(f"imprime a lista ordenada {novalista}")

# como ordenar uma lista em ordem reversa 
novalista = [100,50,65,82,23,38]
novalista.sort(reverse=True)
print(f"imprime a lista ordenada de forma reversa a anterior {novalista}")

# fazer uma cópia de uma lista
outralista = novalista.copy()
print(outralista)

# outra forma de copiar uma cópia de uma lista
minhalista = list(outralista)
print(minhalista)

# juntando duas listas 
list1 = [10,20,30,40]
list2 = [50,60,70,80]
list3 = list1 + list2 
print(list3)

