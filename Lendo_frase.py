
frase = "flamengo é o melhor"
print(frase)
palavra = 'campeao'

frase_lista = frase.split()

print(frase_lista)

ultima_palavra_antes = frase_lista[-1]
ultima_palavra_depois = palavra

print("antes",ultima_palavra_antes)
print("depois",ultima_palavra_depois)

frase_lista[-1] = ultima_palavra_depois
print(frase_lista)

frase_final = " ".join(frase_lista)
print(frase_final)

def ultima_palavra(frase,palavra):
    print(frase)
    frase_lista = frase.split()
    ultima_palavra_antes = frase_lista[-1]
    ultima_palavra_depois = palavra
    frase_lista[-1] = ultima_palavra_depois
    frase_final = " ".join(frase_lista)

    return frase_final

print(ultima_palavra("flamengo é o melhor", "pior"))
