def Fibonacci(num):
    termo1 = 0
    termo2 = 1
    proximo = termo1 + termo2
    while proximo < num:
        proximo = termo1 + termo2
        termo1 = termo2
        termo2 = proximo
    if proximo == num:
        print("{} pertence à sequência Fibonacci!".format(num))
    else:
        print("{} não pertence à sequência".format(num))
    
numero = int(input("Informe o número desejado para buscar: "))
Fibonacci(numero)
       
        