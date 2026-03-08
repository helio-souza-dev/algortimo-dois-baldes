b3_max = 3

b5_max = 5

b3 = 0
b5 = 0

resposta = ""

desperdicio = 0

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

def despejar_para_5():
    global b3, b5
    espaco = b5_max - b5
    transferido = min(b3, espaco)
    
    b3 -= transferido
    b5 += transferido

    
print("Problema dos baldes")
print("Há dois baldes, um de 5 Litros e outro de 3 litros")
print("Uma fonte de agua ilimitada")
print("No balde não há nenhuma medida de volume")
print("O desafio é alcançar o número de 4L")


    

while(b5 != 4):
    while True:
        resposta = input("Deseja encher o balde de 3 litros? S/N\n").strip().upper()
        if resposta in ("S", "N"):
            break
        else:
            print("Resposta errada, digite S, ou N\n")
        
    if(resposta == "S"):
        b3 = 3
        print(f"Você encheu o balde de 3L, o valor ficou {b3}\n")
    
    while True:
        resposta = input("Deseja despejar a agua do balde de 3l no chão?\n").strip().upper()
        if resposta in("S", "N"):
            break
        else:
            print("Resposta errada, digite S ou N\n")
        
    if(resposta == "S"):
        desperdicio += b3
        b3 = 0
        print(f"Você despejou o balde de 3L no chão, o valor final é {b3}\n")
        
    
    while True:
        resposta = input("Deseja transferir a agua do balde de 3l para o de 5L?\n").strip().upper()
        if resposta in("S", "N"):
            break
        else:
            print("Resposta errada, digite S ou N\n")
        
    if(resposta == "S"):
        despejar_para_5()
        print(f"a agua do balde de 3l, {b3} foi para balde de 5l, ficou {b5}")
    
    while True:
        resposta = input("Deseja encher o balde de 5 litros? S/N\n").strip().upper()
        if resposta in ("S", "N"):
            break
        else:
            print("Resposta errada, digite S, ou N\n")
        
    if(resposta == "S"):
        b5 = 5
        print(f"Você encheu o balde de 5L, o valor final é: {b5}")
        
    while True:
        resposta = input("Deseja despejar a agua do balde de 5l no chão?\n").strip().upper()
        if resposta in("S", "N"):
            break
        else:
            print("Resposta errada, digite S ou N\n")
        
    if(resposta == "S"):
        desperdicio += b5
        b5 = 0
        print(print(f"Você despejou o balde de 5L no chão, o valor final é {b5}\n"))
        
    
    while True:
        resposta = input("Deseja transferir a agua do balde de 5l para o de 3L?\n").strip().upper()
        if resposta in("S", "N"):
            break
        else:
            print("Resposta errada, digite S ou N\n")
        
    if(resposta == "S"):
        despejar_para_3()
        print(f"a agua do balde de 5l, {b3} foi para balde de 3l, ficou {b5}")
    
    print(f"\nESTADO ATUAL → 3L: {b3} | 5L: {b5} | Desperdício: {desperdicio}\n")

    
    
    
    
