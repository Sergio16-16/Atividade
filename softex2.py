c = str(input("Digite c para continuar: "))
while c == "c":
    num_1 = float(input("Digite o primeiro numero: "))
    num_2 = float(input("Digite o segundo numero: "))
    soma = num_1 + num_2
    subtracao= num_1 - num_2
    multiplicacao= num_1 * num_2
    divisao= num_1 / num_2
    operacao = str(input("Qual operação voce deseja \n+ para soma\n- para subtração\n* para multiplicação\n/ para divisão\n"))
    if operacao == "+":
        print(soma)
    elif operacao == "-":
        print(subtracao)
    elif operacao == "*":
        print(multiplicacao)
    elif operacao == "/":
        print(divisao)
    else:
        print(0)