'''3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.'''

soma_impares = 0
for i in range(1, 11, 2):  
#start: O primeiro número na sequência. 
# stop: O número onde a sequência irá parar. Note que este valor não é incluído na sequência. sempre conta o 0
# step: O incremento entre cada número na sequência.
    soma_impares += i #melhor escrever assim do que soma_impares = soma_impares + 1
print(soma_impares)
