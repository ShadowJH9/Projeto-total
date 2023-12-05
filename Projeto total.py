nome = input("Digite seu nome")
idade = int( input("Digite sua idade") )
peso = float( input ("Digite seu peso") )

print (nome)
print(type(idade))
print (type(peso))


soma = 10 + 9
multiplicacao = 19 * 7
divisao = 133 / 7
potencia = 7 ** 2

print("soma", soma)
print("multiplicao", multiplicacao)
print("divisao", divisao)
print("potencia", potencia)

idade = int( input ("informe sua idade") )

if idade >= 18:
    print ("PERMITIDO")
else:
    print ("NÃO PERMITIDO!")


salario = float(input("Informe salario: "))

if salario <= 3000:
    print("Programador Junior")
elif salario > 3000 and salario <= 6000:
    print("Programador Pleno")
elif salario > 6000 and salario <= 15000:
    print("programador Senior")
else:
    print(" Gerente de projetos")

lista_numeros = [1, 2, 3]

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

numeros = [1, 2, 3]
strings = [ "jose", "henrique", "shadow"]
decimais = [8.9, 17.6, 20.0]

