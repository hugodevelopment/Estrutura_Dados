# Desafio 1: Encontrar o erro Aqui está um código Python que deveria imprimir os números de 1 a 10, 
# mas há um erro. Você pode identificar e corrigir o erro?

# Aqui o erro é que o numero 10 não está sendo incluso, então deve incluir até 11 para imprimir o 10
# for i in range(1,10):
#     print(i)


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(8))

