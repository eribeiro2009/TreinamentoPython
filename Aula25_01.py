import pyodbc
import pandas as pd

# cria uma conexão com o banco de dados SQL Server
server = "np:\\.\pipe\LOCALDB#08B3E4E7\tsql\query"
conn = pyodbc.connect(r"Driver=SQL Server; Server=np:\\.\pipe\LOCALDB#08B3E4E7\tsql\query; Database=AdventureWorks; Trusted_Connection=yes;")

# select do banco de dados
query = """
        SELECT o.CustomerId
             ,concat(p.Firstname, ' ', p.LastName) as Customer
            ,count(*) as count_orders
            ,sum(o.TotalDue) as total_order
            ,avg(o.TotalDue) as avg_order
             ,max(o.TotalDue) as max_order
            ,min(o.TotalDue) as min_oder
        FROM Sales.SalesOrderHeader o
        INNER JOIN Sales.Customer as c
        ON c.CustomerId = o.CustomerID
        INNER JOIN Person.Person as p
        ON p.BusinessEntityId = c.PersonID
        GROUP BY  o.CustomerId
                ,concat(p.Firstname, ' ', p.LastName) 

        """
df = pd.read_sql(query, conn)
print(df)

conn2 = pyodbc.connect(r'Driver=SQL Server; Server=np:\\.\pipe\LOCALDB#08B3E4E7\tsql\query; Database=inicial; Treusted_Connection=yes;')
query2 = """
            SELECT  id_emp
                   ,nome_emp
                   ,sobrenome
                   ,dt_nascimento
                   ,id_status 
                   ,id_departamento
                   ,salario
                   ,sexo
                   ,dt_admissao
            FROM dbo.empregados
        """
df2 = pd.read_sql(query2, conn2)
print(df2)
print(df2.sort_values(by=["nome_emp"]))
df2.to_csv("emp.csv") # cria o arquivo csv

