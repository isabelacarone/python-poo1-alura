'''6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
Utilize um bloco try-except para lidar com possíveis exceções.'''


#start: O primeiro número na sequência. 
# stop: O número onde a sequência irá parar. Note que este valor não é incluído na sequência. sempre conta o 0
# step: O incremento entre cada número na sequência.

try:
    soma = 0 
    lista = ['4', '18', '22', '0', '7']

    for numero in lista:
        soma += int(numero)  # Converta o elemento para inteiro antes de adicionar à soma

    print(f'Soma dos números da lista: {soma}')
except Exception as erro:
    print(f'Erro: {erro}')


'''7 - Um modo de solucionar essa questão com uma validação de 
lista vazia é do seguinte modo:'''

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
