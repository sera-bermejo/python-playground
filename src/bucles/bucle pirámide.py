def impares(numero):
    print(2*numero-1,end="")
    
num= 5

for i, fila in enumerate (range(1,num+1)):
    for columna in range(fila,0, -1):
        impares(columna)
       
        
    print()
