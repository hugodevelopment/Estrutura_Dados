# Desenvolva uma função que receba uma frase como parâmetro e 
# retorne uma nova frase onde todos os espaços originalmente presentes sejam substituídos por “#”. 
# As entradas e saídas de dados devem ser realizadas no código principal.

def substituir_espacos(frase):
    nova_frase = ""
    for caractere in frase:
        if caractere == " ":
            nova_frase += "#"
        else:
            nova_frase += caractere
    return nova_frase

# Código principal
frase = "ola coco hugo lucas"
nova_frase = substituir_espacos(frase)
print(nova_frase)
