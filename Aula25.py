import pandas as pd

mylist = {

    'Cars': ['BMW', 'Volvo', 'Ford'],
    'Prices' : [120000, 220000, 180000]
}

print(mylist)

df = pd.DataFrame(mylist)
print(df)

#listar somente uma linha específica
print(df.loc[0])

# listas quantas linhas tem um dataframe
print(f"Max_rows {pd.options.display.max_rows}")

df = pd.read_csv("empregados.csv")

# lista de forma ordena por idade
print(df.sort_values(by=["Idade", "Salário"]))