import tkinter as tk
import os

# Pega o caminho da pasta onde o script está salvo para não dar erro de "arquivo não encontrado"
diretorio_atual = os.path.dirname(__file__)


root = tk.Tk()
root.title("Jogo dos Baldes")


try:
    pasta_assets = "assets"
    img1 = tk.PhotoImage(file=os.path.join(diretorio_atual, pasta_assets, "balde.png"))
    img2 = tk.PhotoImage(file=os.path.join(diretorio_atual, pasta_assets, "balde_cheio.png"))
except tk.TclError:
    print("as imagens nao foram encontradas na pasta do codigo")

b3_max = 3
b5_max = 5

b3 = 0
b3_var = tk.StringVar()
b3_var.set(f"b3 = {b3}")

b5 = 0
b5_var = tk.StringVar()
b5_var.set(f"b5 = {b5}")

desperdicio = 0
desperdicio_var = tk.StringVar()
desperdicio_var.set(f"desperdicio = {desperdicio}")

contagem = 0
contagem_var = tk.StringVar()
contagem_var.set(f"passos = {contagem}")

vitoria = False
tela_vitoria = None

def verificar_vitoria():
    if b5 == 4:
        global vitoria, tela_vitoria
        vitoria = True
        frame.pack_forget()

        tela_vitoria = tk.Frame(root)
        tela_vitoria.pack(expand=True, fill="both", padx=50, pady=50)
        
        tk.Label(tela_vitoria, text="🏆", font=("Arial", 50)).pack()
        tk.Label(tela_vitoria, text="PARABÉNS!", font=("Arial", 20, "bold")).pack()
        tk.Label(tela_vitoria, text=f"Você conseguiu 4L com {desperdicio}L de desperdício e {contagem} passos.").pack(pady=10)

        
        tk.Button(tela_vitoria, text="Jogar Novamente", command=reiniciar_jogo).pack(pady=20)

def reiniciar_jogo():
    global b3, b5, desperdicio, tela_vitoria
    if vitoria == True:
        tela_vitoria.pack_forget()
        frame.pack()

        b5 = 0
        b5_var.set(f"b5 = {b5}")
        
        b3 = 0
        b3_var.set(f"b3 = {b3}")

        desperdicio = 0
        desperdicio_var.set(f"desperdicio = {desperdicio}")

        label_img1.config(image=img1)
        label_img2.config(image=img1)

def contar():
    global contagem
    contagem += 1
    contagem_var.set(f"passos = {contagem}")

if b3 > b3_max:
    desperdicio = b3 - b3_max
    b3 = b3_max

if b5 > b5_max:
    desperdicio = b5 - b3_max
    b5 = b5_max

def despejar_para_3():
    global b3, b5, desperdicio
    espaco = b3_max - b3
    transferido = min(b5, espaco)
    
    b3 += transferido
    b5 -= transferido
    b3_var.set(f"b3 = {b3}")
    b5_var.set(f"b5 = {b5}")
    
    if b3 > 0:
        label_img2.config(image=img2)
    else:
        label_img2.config(image=img1)

    if b5 > 0:
        label_img1.config(image=img2)
    else:
        label_img1.config(image=img1)
    
    verificar_vitoria()
    contar()

def despejar_para_5():
    global b3, b5
    espaco = b5_max - b5
    transferido = min(b3, espaco)
    
    b3 -= transferido
    b5 += transferido
    b3_var.set(f"b3 = {b3}")
    b5_var.set(f"b5 = {b5}")

    if b3 > 0:
        label_img2.config(image=img2)
    else:
        label_img2.config(image=img1)

    if b5 > 0:
        label_img1.config(image=img2)
    else:
        label_img1.config(image=img1)

    verificar_vitoria()
    contar()

def trocar_btn1():
    global b5
    label_img1.config(image=img2)
    b5 = b5_max
    b5_var.set(f"b5 = {b5}")
    verificar_vitoria()
    contar()

def trocar_btn2():
    global b3
    label_img2.config(image=img2)
    b3 = b3_max
    b3_var.set(f"b3 = {b3}")
    verificar_vitoria()
    contar()

def esvaziar_balde3l():
    global b3, desperdicio
    b3 = 0
    b3_var.set(f"b3 = {b3}")
    label_img2.config(image=img1)
    desperdicio += 3
    desperdicio_var.set(f"desperdicio = {desperdicio}")
    contar()

def esvaziar_balde5l():
    global b5, desperdicio
    b5 = 0
    b5_var.set(f"b5 = {b5}")
    label_img1.config(image=img1)
    desperdicio += 5
    desperdicio_var.set(f"desperdicio = {desperdicio}")
    contar()

frame = tk.Frame(root)
frame.pack(padx=30, pady=30)

#imagens
label_img1 = tk.Label(frame, image=img1)
label_img1.grid(row=0, column=0, columnspan=2, padx=20)

label_img2 = tk.Label(frame, image=img1)
label_img2.grid(row=0, column=2, columnspan=2, padx=20)

#botoes b3 b5
label_b3 = tk.Label(frame, textvariable=b5_var)
label_b3.grid(row=1, column=1, columnspan=2, padx=20)

label_b5 = tk.Label(frame, textvariable=b3_var)
label_b5.grid(row=1, column=2, columnspan=2, padx=20)

#botoes de encher
botao1 = tk.Button(frame, text="Encher balde 5L", command=trocar_btn1, width=15)
botao1.grid(row=2, column=0, columnspan=2, pady=10)

botao2 = tk.Button(frame, text="Encher balde 3L", command=trocar_btn2, width=15)
botao2.grid(row=2, column=2, columnspan=2, pady=10)

#acoes balde 5l
botao3 = tk.Button(frame, text="Esvaziar", command=esvaziar_balde5l)
botao3.grid(row=3, column=0, padx=5, pady=10)

botao4 = tk.Button(frame, text="Transferir agua", command=despejar_para_3)
botao4.grid(row=3, column=1, padx=5, pady=10)

#acoes balde 3l
botao5 = tk.Button(frame, text="Esvaziar", command=esvaziar_balde3l)
botao5.grid(row=3, column=2, padx=5, pady=10)

botao6 = tk.Button(frame, text="Transferir agua", command=despejar_para_5)
botao6.grid(row=3, column=3, padx=5, pady=10)

label_desperdicio = tk.Label(frame, textvariable=desperdicio_var)
label_desperdicio.grid(row=4, column=1, padx=10)

label_contagem = tk.Label(frame, textvariable=contagem_var)
label_contagem.grid(row=4, column=1, columnspan=4, padx=40)

root.mainloop()