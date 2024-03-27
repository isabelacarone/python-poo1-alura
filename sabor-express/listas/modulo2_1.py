'''1 - Solicite ao usuário que insira um número e, em seguida, 
use uma estrutura if else para determinar se o número é par ou ímpar.'''


try: 
    numero = float(input("insira aqui um número: "))

    if numero % 2 != 0:
        print(f" seu número {numero} é ímpar ")
    else:
        print(f"seu número {numero} é par")
        

except Exception as erro:
    print(f"erro: {erro}")