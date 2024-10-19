exemplo = 'A frase que vai ser analisada'
texto = exemplo.lower()
letra = 'a'
cont = 0
inicio = 0

for i in range(len(texto)):
    posicao = texto.find(letra, inicio)
    if posicao != -1:
        inicio = posicao + 1
        cont += 1

if cont > 0:
    print("Foram encontradas {} letras A na frase.".format(cont))
else:
    print("Essa letra não apareceu na frase.")
