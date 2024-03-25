#  Aqui temos um fatorial, nesse caso a condição base é n igual a 1 ou 0 e função é chamada até se chegue neste valor.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        # começa sendo 5 * 5*4*3*2*1
        # Então, se n for 5, a função calculará 5 * factorial(4). E factorial(4) será 4 * factorial(3), 
        # e assim por diante. Portanto, o resultado final será 5 * 4 * 3 * 2 * 1, que é o fatorial de 5.
        return n * factorial(n)

print(factorial(5))