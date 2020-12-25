# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!
op = ''
res = 0

print("\n******************* Python Calculator *******************")

operacao = int(input('''Selecione o número da operação desejada:\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\nDigite sua opção(1/2/3/4): '''))

if(operacao >= 5 or operacao <= 0):
    print("Operação Inválida!")
else:
    try:
        n1 = float(input("\nDigite o primeiro número: "))
        n2 = float(input("\nDigite o segundo número: "))
        
        if(operacao == 1):
            op = '+'
            res = (lambda x, y: x + y)(n1, n2)
        elif(operacao == 2):
            op = '-'
            res = (lambda x, y: x - y)(n1, n2)
        elif(operacao == 3):
            op = '*'
            res = (lambda x, y: x * y)(n1, n2)
        elif(operacao == 4):
            op = '/'
            res = (lambda x, y: x / y)(n1, n2)
        print(f"{n1} {op} {n2} = {res}")
    except:
        print("erro ao fazer os calculos...")