# Desenvolva uma função que receba uma frase como parâmetro e 
# retorne uma nova frase onde todos os espaços originalmente presentes sejam substituídos por “#”. 
# As entradas e saídas de dados devem ser realizadas no código principal.

def substituir_espaços(frase):
    nova_frase = ""
    for i in frase:
        if i == " ":
            nova_frase += "#"
        else:
            nova_frase += i
    return nova_frase

print(substituir_espaços("ola amigos "))            

