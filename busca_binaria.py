# É um algoritmo de busca em vetores que segue o paradigma de divisão e conquista. 
# Ela parte do pressuposto de que o vetor está ordenado e realiza sucessivas divisões do espaço de busca comparando 
# o elemento buscado (chave) com o elemento no meio do vetor. Se o elemento do meio do vetor for a chave, 
# a busca termina com sucesso. Caso contrário, se o elemento do meio vier antes do elemento buscado, então a busca continua na metade posterior do vetor. 
# E finalmente, se o elemento do meio vier depois da chave, a busca continua na metade anterior do vetor.



def busca_binaria(array, alvo):
    limite_inferior = 0
    limite_superior = len(array) - 1
    meio = 0
    while (limite_inferior <= limite_superior):
        meio = limite_inferior + limite_superior/2
        if array[meio] == alvo:
            return meio
        elif array[meio] < alvo:
            limite_inferior = meio + 1 
        else:
            limite_superior = meio - 1
        return - 1        