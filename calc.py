import tkinter as tk

root = tk.Tk()
root.title("Calculadora")

# Frames
frame_principal = tk.Frame(root)
frame_principal.pack(expand=True, fill="both")

frame_soma = tk.Frame(root)
frame_subtracao = tk.Frame(root)
frame_multiplicao = tk.Frame(root)
frame_divisao = tk.Frame(root)

v1_var = tk.StringVar()
v2_var = tk.StringVar()
resul_som_var = tk.StringVar(value="0")

resul_sub_var = tk.StringVar(value="0")

resul_mul_var = tk.StringVar(value="0")

resul_div_var = tk.StringVar(value="0")

frame_atual = None



# Função que mostra a tela da soma
def abrir_soma():
    global frame_atual
    frame_principal.pack_forget()
    frame_soma.pack(expand=True, fill="both")
    frame_atual = frame_soma

def abrir_subtracao():
    global frame_atual
    frame_principal.pack_forget()
    frame_subtracao.pack(expand=True, fill="both")
    frame_atual = frame_subtracao
    
def abrir_multiplicacao():
    global frame_atual
    frame_principal.pack_forget()
    frame_multiplicao.pack(expand=True, fill="both")
    frame_atual = frame_multiplicao
    
def abrir_divisao():
    global frame_atual
    frame_principal.pack_forget()
    frame_divisao.pack(expand=True, fill="both")
    frame_atual = frame_divisao

def voltar():
    global frame_atual
    frame_atual.pack_forget()
    frame_principal.pack(expand=True, fill="both")
    frame_atual = None
        

# Função que calcula a soma
def calcular_soma():
    try:
        v1 = float(v1_var.get())
        v2 = float(v2_var.get())
        resul_som = v1 + v2
        resul_som_var.set(str(resul_som))
    except ValueError:
        resul_som_var.set("Erro: digite números válidos")

def calcular_subtracao():
    try:
        v1 = float(v1_var.get())
        v2 = float(v2_var.get())
        resul_sub = v1 - v2
        resul_sub_var.set(str(resul_sub))
    except ValueError:
        resul_sub_var.set("Erro: digite números válidos")

def calcular_multiplicacao():
    try:
        v1 = float(v1_var.get())
        v2 = float(v2_var.get())
        resul_mul = v1 * v2
        resul_mul_var.set(str(resul_mul))
    except ValueError:
        resul_mul_var.set("Erro: digite números válidos")

def calcular_divisao():
    try:
        v1 = float(v1_var.get())
        v2 = float(v2_var.get())
        resul_div = v1 / v2
        resul_div_var.set(str(resul_div))
    except ValueError:
        resul_div_var.set("Erro: digite números válidos")
    

# Widgets da tela principal
label_escolhaOp = tk.Label(frame_principal, text="Escolha a operação")
label_escolhaOp.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

botao_soma = tk.Button(frame_principal, text="Soma", command=abrir_soma)
botao_soma.grid(row=1, column=0, padx=10, pady=10)

botao_subtracao = tk.Button(frame_principal, text="Subtração", command=abrir_subtracao)
botao_subtracao.grid(row=1, column=1, padx=10, pady=10)

botao_multiplicacao = tk.Button(frame_principal, text="Multiplicação", command=abrir_multiplicacao)
botao_multiplicacao.grid(row=2, column=0, padx=10, pady=10)

botao_divisao = tk.Button(frame_principal, text="Divisão", command=abrir_divisao)
botao_divisao.grid(row=2, column=1, padx=10, pady=10)

# botoes da tela soma
entrada_v1 = tk.Entry(frame_soma, textvariable=v1_var)
entrada_v1.grid(row=0, column=0, padx=10, pady=10)

entrada_v2 = tk.Entry(frame_soma, textvariable=v2_var)
entrada_v2.grid(row=1, column=0, padx=10, pady=10)

botao_calcular = tk.Button(frame_soma, text="Calcular", command=calcular_soma)
botao_calcular.grid(row=2, column=0, padx=10, pady=10)

label_resultado = tk.Label(frame_soma, textvariable=resul_som_var)
label_resultado.grid(row=3, column=0, padx=10, pady=10)

botao_voltar = tk.Button(frame_soma, text="Voltar", command=voltar)
botao_voltar.grid(row=4, column=0, pady=10)

# botoes da tela subtracao
entrada_v1 = tk.Entry(frame_subtracao, textvariable=v1_var)
entrada_v1.grid(row=0, column=0, padx=10, pady=10)

entrada_v2 = tk.Entry(frame_subtracao, textvariable=v2_var)
entrada_v2.grid(row=1, column=0, padx=10, pady=10)

botao_calcular = tk.Button(frame_subtracao, text="Calcular", command=calcular_subtracao)
botao_calcular.grid(row=2, column=0, padx=10, pady=10)

label_resultado = tk.Label(frame_subtracao, textvariable=resul_sub_var)
label_resultado.grid(row=3, column=0, padx=10, pady=10)

botao_voltar = tk.Button(frame_subtracao, text="Voltar", command=voltar)
botao_voltar.grid(row=4, column=0, pady=10)

# botoes da tela multiplicacao
entrada_v1 = tk.Entry(frame_multiplicao, textvariable=v1_var)
entrada_v1.grid(row=0, column=0, padx=10, pady=10)

entrada_v2 = tk.Entry(frame_multiplicao, textvariable=v2_var)
entrada_v2.grid(row=1, column=0, padx=10, pady=10)

botao_calcular = tk.Button(frame_multiplicao, text="Calcular", command=calcular_multiplicacao)
botao_calcular.grid(row=2, column=0, padx=10, pady=10)

label_resultado = tk.Label(frame_multiplicao, textvariable=resul_mul_var)
label_resultado.grid(row=3, column=0, padx=10, pady=10)

botao_voltar = tk.Button(frame_multiplicao, text="Voltar", command=voltar)
botao_voltar.grid(row=4, column=0, pady=10)

# botoes da tela multiplicacao
entrada_v1 = tk.Entry(frame_divisao, textvariable=v1_var)
entrada_v1.grid(row=0, column=0, padx=10, pady=10)

entrada_v2 = tk.Entry(frame_divisao, textvariable=v2_var)
entrada_v2.grid(row=1, column=0, padx=10, pady=10)

botao_calcular = tk.Button(frame_divisao, text="Calcular", command=calcular_divisao)
botao_calcular.grid(row=2, column=0, padx=10, pady=10)

label_resultado = tk.Label(frame_divisao, textvariable=resul_div_var)
label_resultado.grid(row=3, column=0, padx=10, pady=10)

botao_voltar = tk.Button(frame_divisao, text="Voltar", command=voltar)
botao_voltar.grid(row=4, column=0, pady=10)

root.mainloop()