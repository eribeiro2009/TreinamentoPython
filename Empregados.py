import tkinter as tk 
from tkinter import *
from tkinter import messagebox
import pyodbc
from datetime import date

# sqllocaldb info LocalDB1

def conecta_banco():
    conn = pyodbc.connect(r'Driver=SQL Server; Server=np:\\.\pipe\LOCALDB#2808E6CB\tsql\query; Database=inicial; Treusted_Connection=yes;')
    return conn


def pesquisa_emp():
    idEmp = entry_IdEmp.get()
    if idEmp == '':
        messagebox.showinfo("Erro!", "Favor informar ID do Empregado!")
        return False
    
    conn = conecta_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT id_emp FROM dbo.empregados WHERE id_emp= ?",idEmp)
    achou = cursor.fetchone()
    if not achou:
        messagebox.showinfo("Erro!","ID do Empregado não cadastrado")
        return False
    
    query = """
    Select   nome_emp
            ,sobrenome
            ,dt_nascimento
            ,id_status
            ,id_departamento
            ,salario
            ,sexo
            ,dt_admissao
            ,id_cargo
    FROM dbo.empregados 
    WHERE id_emp = ?
    """
    cursor.execute(query,idEmp)
    data = cursor.fetchall()
    nome_emp = data[0].nome_emp   
    entry_nomeEmp.insert(0,nome_emp)
    sobrenome = data[0].sobrenome 
    entry_sobreNome.insert(0,sobrenome)
    dt_nascimento = data[0].dt_nascimento  
    entry_dtNascimento.insert(0,dt_nascimento)
    #id_status = data[0].id_status   
    #vars.insert(0,id_status)
    id_departamento = data[0].id_departamento  
    entry_idDep.insert(0,id_departamento)
    salario = data[0].salario   
    entry_salario.insert(0,salario)
    sexo = data[0].sexo   
    cv2.insert(0,sexo)
    dt_admissao = data[0].dt_admissao   
    entry_dtAdmissao.insert(0,dt_admissao)
    #id_cargo = data[0].id_cargo 
    #cv.insert(0,id_cargo)


def exit_form():
    response = messagebox.askquestion("Sair", "Deseja Sair?")
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
    sexo = cv2.get()
    dtAdmissao = entry_dtAdmissao.get()
    funcao = cv.get()

    # valida o empregado
    if not valida_idEmp(idEmp):
        return
    
    if not valida_nomeEmp(nomeEmp):
        return
    
    if not valida_sobrenome(sobrenome):
        return
    
    if not valida_dtNascimento(dtNascimento):
        return

    if not valida_idStatus(idStatus):
        return
    
    # valida o departamento
    if not valida_idDep(idDep):
        return
    
    if not valida_salario(salario):
        return

    if not valida_dtAdmissao(dtAdmissao):
        return
    
    
    #connecta no banco SQL Server Local incial
    conn = conecta_banco()
    cursor = conn.cursor()

    #comando_insert = """
    #INSERT INTO dbo.empregados(id_emp, nome_emp, sobrenome, dt_nascimento,
    #    id_status, id_departamento, salario, sexo, dt_admissao, id_cargo) Values(?,?,?,?,?,?,?,?,?,?) 
    #"""
    comando_insert = """
    INSERT INTO dbo.empregados(id_emp, nome_emp, sobrenome, dt_nascimento,
        id_status, id_departamento, salario, sexo, dt_admissao, id_cargo) Values(?,?,?,?,?,?,?,?,?,?) 
    """
    #cursor.execute(comando_insert, idEmp, nomeEmp, sobrenome, dtNascimento, idStatus, idDep, salario, sexo, dtAdmissao, funcao)
    cursor.execute(comando_insert, idEmp, nomeEmp, sobrenome, dtNascimento, idStatus, idDep, salario, sexo, dtAdmissao, funcao)
    conn.commit()
    cursor.close()
    conn.close()
    messagebox.showinfo("Salvo", "Dados Gravados com Sucesso!")


    entry_IdEmp.delete(0,END)
    entry_nomeEmp.delete(0,END)
    entry_sobreNome.delete(0,END)
    entry_dtNascimento.delete(0,END)
    entry_idDep.delete(0,END)
    entry_salario.delete(0,END)
    entry_dtAdmissao.delete(0,END)


    


def valida_idEmp(idEmp):

    # verifica se o campo esta preenchido ou vazio e caso ele estiver vazio retorna como False 
    if idEmp == '':
        messagebox.showinfo("Erro!", "Favor informar ID do Empregado!")
        return False
    
    # conecta no banco incial
    conn = conecta_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT id_emp FROM dbo.empregados WHERE id_emp= ?",idEmp)
    achou = cursor.fetchone()
    if achou:
        messagebox.showinfo("Erro!","ID do Empregado já cadastrado")
        return False
    
    return True

def valida_nomeEmp(nomeEmp):

    if nomeEmp == '':
        messagebox.showinfo("Erro!", "Favor Informar Nome do Empregado!")
        return False
    
    return True

def valida_sobrenome(sobrenome):

    if sobrenome == '':
        messagebox.showinfo("Erro!", "Favor Informar Sobrenome do Empregado!")
        return False
    
    return True

def valida_dtNascimento(dtNascimento):

    if dtNascimento == '':
        messagebox.showinfo("Erro!", "Favor Informar data de nascimento do Empregado!")
        return False
    
    if dtNascimento[0:3] > "2008":
        messagebox.showinfo("Erro!", "Data de nascimento inválida!")
        return False
    
    return True

def valida_dtAdmissao(dtAdmissao):

    if dtAdmissao == '':
        messagebox.showinfo("Erro!", "Favor informar a data de admissão do Empregado!")
        return False
    
    hoje = date.today()

    if dtAdmissao > str(hoje):
        messagebox.showinfo("Erro!", "Data de Admissão inválida!")
        return False
    
    return True

def valida_idStatus(idStatus):

    if idStatus == 0:
        messagebox.showinfo("Erro!", "Favor Informar o id status do Empregado!")
        return False
        
    return True

def valida_salario(salario):

    if salario == '':
        messagebox.showinfo("Erro!", "Favor Informar o Salario do Empregado!")
        return False
    
    if int(salario) not in range(1400, 30000):
        messagebox.showinfo("Erro!", "Salario fora do range!")
        return False
        
    return True

def valida_idDep(p_idDep):

    if p_idDep == '':
        messagebox.showinfo("Erro!", "Favor informar ID do Departamento!")
        return False
    
    # conecta no banco incial
    conn = conecta_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT id_dep FROM dbo.departamentos WHERE id_dep= ?",p_idDep)
    achou = cursor.fetchone()
    if achou is None:
        messagebox.showinfo("Erro no departamento","ID do Departamento não cadastrado!")
        return False
    
    return True

# cria a janela principal
root = tk.Tk()
root.title("Formulário de Empregados")
root.geometry("1000x500")
small_icon = tk.PhotoImage(file="iconedeformulario.png")
large_icon = tk.PhotoImage(file="iconedefomulariolarge.png")
root.iconphoto(False, large_icon, small_icon)
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

sexo = ("M", "F")
cv2 = StringVar()
drplist2 = OptionMenu(root, cv2, *sexo)
drplist2.config(width=25)
cv2.set("M")

label_sexo = Label(root, text="Selecione o Sexo:", width=15, font=("arial",8), background="white").place(x=25, y=310)
drplist2.place(x=148, y=300)

label_dtAdmissao = tk.Label(root, text="Data Admissao:", background="white").place(x=35, y=270)
entry_dtAdmissao = tk.Entry(root, background="light gray")
entry_dtAdmissao.place(x=150, y=270)

funcoes = ("Analista de Sistemas", "Encanador", "Gerente", "Ajudante")
cv = StringVar()
drplist = OptionMenu(root, cv, *funcoes)
drplist.config(width=25)
cv.set("Gerente")

label_funcao = Label(root, text="Selecione a Função:", width=15, font=("arial",8), background="white")
label_funcao.place(x=25, y=330)
drplist.place(x=148, y=330)

# botão de envio
idEmp = entry_IdEmp
button_submit = tk.Button(root, text="Enviar", command=submit_form, height=1, width=20, background="gray").place(x=250, y=420)
 
# botão de pesquisa
button_pesquisar = tk.Button(root, text="Pesquisar", command=pesquisa_emp, height=1, width=20, background="gray").place(x=450, y=420)

# botão sair
button_sair = tk.Button(root, text="Sair", command=exit_form, height=1, width=20, background="gray").place(x=650, y=420)

# inica o loop para manter a tela ativa
root.mainloop()







