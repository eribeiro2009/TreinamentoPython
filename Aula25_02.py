from tkinter import *
from time import strftime

# cria uma função para atualizar o relógio
def atualiza_relogio():
    horario_atual = strftime("%H:%M:%S %p")
    rotulo_relogio.config(text=horario_atual)
    rotulo_relogio.after(1000, atualiza_relogio)

# cria a janela principal
janela = Tk()
janela.title("Relógio Digital")

#cria o rótulo para exigir o relógio 
rotulo_relogio = Label(
    janela,
    font=("Arial",40, "bold"),
    background="light green",
    foreground="white"
)

# posiciona o relógio no centro da janela
rotulo_relogio.pack(anchor="center")

# incia a atualização automática do relógio
atualiza_relogio()

# incia o loop principal da interface 
janela.mainloop()