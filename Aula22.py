# tuples
frutas = ("apples", "banana", "pinneapple")

print(frutas)

# imprime o tamanho de um tuple
print(len(frutas))

# imprime o tipo da lista
print(type(frutas))

# collection to Python
# list => flexível
# tuple => não permite alterar
# set => não permite alterar e não permite membros duplicados
# dict

# imprime o 1o item
print(frutas[0])

#imprime de trás para frente
print(frutas[-1])

# como o tuple não pode ser alterado, converter um tuple numa lista
frutas2 = list(frutas)

# depois de criar uma lista com base no tuple, adicionar 1 item
frutas2.append("mango")
print(frutas2)

# fazendo um loop num tuple
for i in frutas:
    print(i)

# criando um novo tuple a partir de outros dois
tuple1 = (10,20,30,40)
tuple2 = (50,60,70,80)
tuple3 = tuple1 + tuple2
print(tuple3)


######################################################################################################
# set
thisset = {"maça", "banana", "abacate", "maça"}
print(thisset)

for i in thisset:
    print(i)

# teste se exitse um membro específico num set
print("banana" in thisset)

# unir 2 sets em um único
set1 = {"a", "b", "c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

# usando operados | para unir
set4 = set1 | set2
print(set4)

##################################################################################################
# novo tipo de coleção: dict

mydict = { 
    "marca": "Jeep",
    "modelo": "Renegade",
    "ano": "2022"
}

print(mydict)

# imprime uma parte específica
print(mydict["marca"])

#imprime as chaves de um dict
x = mydict.keys()
print(x)

#imprime os valores do dict
y = mydict.values()
print(y)

# altera o valor de uma chave
mydict.update({"ano": 2023})

print(mydict)

# adicionar uma nova key-value
mydict["cor"] = "branco"
print(mydict)

# usando update para adicionar uma nova categoria
mydict.update({"ipva_pago": "sim"})
print(mydict)

# removendo um item do dict
mydict.pop("modelo")
print(mydict)

# apaga apenas uma celula da lista
del mydict["ano"]
print(mydict)

#apaga todos os itens do dict
mydict.clear()
print(mydict)

mydict = { 
    "marca": "Jeep",
    "modelo": "Renegade",
    "ano": "2022"
}

for x in mydict.values():
    print(x)

for x in mydict.keys():
    print(x)

for x,y in mydict.items():
    print(x,y)

# clonar um dict
novodict = mydict.copy()
print(novodict)

outrodict = dict(mydict)
print(outrodict)

# nested (aninhado) dict
nestdict = {
    "Carro1" : {
        "marca" : "Jeep",
        "modelo" : "Renegade",
        "ano" : 2020,
        "cor" : "branca"
    },
    "Carro2" : {
        "marca" : "Hyundai",
        "modelo" : "HB20",
        "ano" : 2019,
        "cor" : "azul"
    },
    "Carro3" :{
        "marca" : "Ford",
        "modelo" : "Ka",
        "ano" : 2008,
        "cor" : "preto"
    }
}

print(nestdict)

for x,y in nestdict.items():
    print(x,y)
    print("------------------------------------------------------------------------------")

print(nestdict["Carro1"])