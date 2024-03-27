''' 5 - Solicite ao usuário um número e, em seguida, 
utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.'''
3

tabuada = int(input('insira aqui um numero p/ descobria tabuada dele:'))

for i in range (1, 11,1 ):
    final = tabuada * i
    print(f'{tabuada} * {i} = {final}')