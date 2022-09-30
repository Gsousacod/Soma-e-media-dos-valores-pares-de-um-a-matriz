matriz =  [ [0,0,0], [0,0,0], [0,0,0]]
soma = 0
c = 0
m = 0
for i in range (0,3):
    for j in range(0,3):
        matriz[i][j] = int(input("Digite um elemento:"))
        if(matriz[i][j]%2==0):
            soma+=matriz[i][j]
            c+=1
me = soma/c
print('<<>>'*5)
print(matriz)
print('<<>>'*5)
for i in range (0,3):
        for j in range(0,3):
                print(f'[{matriz[i] [j] :^5}]', end = "")
        print()
print('<<>>'*5)
print(soma)
print('<<>>'*5)
print(me)