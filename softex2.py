c = str(input("Digite c para continuar: "))
while c == "c":
    num_1 = float(input("Digite o primeiro numero: "))
    num_2 = float(input("Digite o segundo numero: "))
    soma = num_1 + num_2
    subtracao= num_1 - num_2
    multiplicacao= num_1 * num_2
    divisao= num_1 / num_2
    operacao = str(input("Qual operação voce deseja \n1 para soma\n2 para subtração\n3 para multiplicação\n4 para divisão\n0 para sair\n"))
    if operacao == "1":
        print(soma)
        c = str(input("Digite c para continuar: "))
    elif operacao == "2":
        print(subtracao)
        c = str(input("Digite c para continuar: "))
    elif operacao == "3":
        print(multiplicacao)
        c = str(input("Digite c para continuar: "))
    elif operacao == "4":
        print(divisao)
        c = str(input("Digite c para continuar: "))
    elif operacao == "0":
        break
    else:
        print(0)
        