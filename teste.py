import tkinter as tk

root = tk.Tk()             # Cria a janela principal
root.title("Minha Janela") # Título da janela
root.geometry("300x200")   # Tamanho da janela (largura x altura)

tk.Label(root, text="Problema dos baldes").pack()
tk.Label(root, text="Há dois baldes, um de 5 Litros e outro de 3 litros").pack()
tk.Label(root, text="Uma fonte de agua ilimitada").pack()
tk.Label(root, text="No balde não há nenhuma medida de volume").pack()
tk.Label(root, text="O desafio é alcançar o número de 4L").pack()
root.mainloop()     