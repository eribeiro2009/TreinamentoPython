import tkinter as tk 
from tkinter import *
from tkinter import messagebox
import pyodbc

# sqllocaldb info LocalDB1

def exit_form():
    response = messagebox.askquestion("Sair", "Deseja Sair?", icon="warnning")
    if response == "yes":
        exit()

def submit_form():
    idEmp = entry_IdEmp.get()
    nomeEmp = entry_nomeEmp.get()
    sobrenome = entry_sobreNome.get()
    dtNascimento = entry_dtNascimento.get()
    idStatus = vars.get()
    idDep = entry_idDep.get()
    salario = entry_salario.get()
    funcao = cv.get()

    if not valida_idEmp(idEmp):
        return

    #connecta no banco SQL Server Local incial
    conn = pyodbc.connect(r'Driver=SQL Server; Server=np:\\.\pipe\LOCALDB#6AE522D0\tsql\query; Database=inicial; Treusted_Connection=yes;')
    cursor = conn.cursor()

    comando_insert = """
    INSERT INTO dbo.empregados(id_emp, nome_emp, sobrenome, dt_nascimento,
        id_status, id_departamento, salario, id_cargo) Values(?,?,?,?,?,?,?,?) 
    """
    cursor.execute(comando_insert, idEmp, nomeEmp, sobrenome, dtNascimento, idStatus, idDep, salario, funcao)
    conn.commit()
    cursor.close()
    conn.close()

def valida_idEmp(idEmp):

    if idEmp == '':
        messagebox.showinfo("Erro!", "Favor informar ID do Empregado!")
        return False
    
    # conecta no banco incial
    conn = pyodbc.connect(r'Driver=SQL Server; Server=np:\\.\pipe\LOCALDB#6AE522D0\tsql\query; Database=inicial; Treusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("SELECT id_emp FROM dbo.empregados WHERE id_emp= ?",idEmp)
    achou = cursor.fetchone()
    if achou:
        messagebox.showinfo("ID do Empregado já cadastrado")
        return False
    
    return True

# cria a janela principal
root = tk.Tk()
root.title("Formulário de Empregados")
root.geometry("1000x500")
root.config(background="white")

title = Label(root, text="Formulário de Registro de Empregados",
              width=30, font=("bold, 14"),
              background="white")
title.place(x=300, y=13)

# criar e posicionar os campos e rótulos na tela
label_idEmp = Label(root, text="Id Emp: ", background="white")
label_idEmp.place(x=80, y=55)
entry_IdEmp = tk.Entry(root, background="light gray")
entry_IdEmp.place(x=150, y=55)

label_nomeEmp = tk.Label(root, text="Nome Emp", background="white")
label_nomeEmp.place(x=60, y=80)
entry_nomeEmp = tk.Entry(root, background="light gray", width=20)
entry_nomeEmp.place(x=150, y=80)

label_sobreNome = tk.Label(root, text="Sobrenome", background="white")
label_sobreNome.place(x=60, y=105)
entry_sobreNome = tk.Entry(root, background="light gray")
entry_sobreNome.place(x=150, y=105)

label_dtNascimento = tk.Label(root, text="Data de Nascimento", background="white")
label_dtNascimento.place(x=10, y=130)
entry_dtNascimento = tk.Entry(root, background="light gray")
entry_dtNascimento.place(x=150, y=130)

label_idStatus = tk.Label(root, text="Id Status", background="white").place(x=70, y=155)

vars = IntVar()
Radiobutton(root, text="Ativo", padx=5, variable=vars, value=1, background="white").place(x=150, y=155)
Radiobutton(root, text="Desligado", padx=10, variable=vars, value=2, background="white").place(x=215, y=155)
Radiobutton(root, text="Afastado", padx=15, variable=vars, value=3, background="white").place(x=300, y=155)

label_idDep = tk.Label(root, text="Id Departamento:", background="white").place(x=30, y=190)
entry_idDep = tk.Entry(root, background="light gray")
entry_idDep.place(x=150, y=190)

label_salario = tk.Label(root, text="Salário:", background="white").place(x=80, y=230)
entry_salario = tk.Entry(root, background="light gray")
entry_salario.place(x=150, y=230)

funcoes = ("Analista de Sistemas", "Encanados", "Gerente", "Ajudante")
cv = StringVar()
drplist = OptionMenu(root, cv, *funcoes)
drplist.config(width=25)
cv.set("Gerente")

label_funcao = Label(root, text="Selecione a Função:", width=15, font=("arial",8), background="white")
label_funcao.place(x=25, y=270)
drplist.place(x=148, y=260)

# botão de envio
idEmp = entry_IdEmp
button_submit = tk.Button(root, text="Enviar", command=submit_form, height=1, width=20, background="gray").place(x=300, y=420)
 
# botão sair
button_sair = tk.Button(root, text="Sair", command=exit_form, height=1, width=20, background="gray").place(x=550, y=420)

# inica o loop para manter a tela ativa
root.mainloop()







