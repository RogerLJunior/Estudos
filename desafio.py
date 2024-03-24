print ( "Esse Programa tem como desafio testar e demonstrar meus conhecimentos em Pyhton.")

print (" Para acessar o desafio utilize o Link: https://wiki.python.org.br/EstruturaSequencial")

print( " Os desafios propostos serão: ")

print( "DESAFIO 01 ")

print ("Ola Mundo ")

print( "DESAFIO 02 ")

numero = input("Digite um número: ")
print(f"O número informado foi {numero}")

print( "DESAFIO 03 ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma dos dois números é {soma}")

print( "DESAFIO 04 ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média das notas é {media}")

print( "DESAFIO 05 ")

metros = float(input("Digite a quantidade de metros: "))
centimetros = metros * 100
print(f"{metros} metros equivalem a {centimetros} centímetros")

print( "DESAFIO 06 ")

import math

raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio ** 2

print(f"A área do círculo é {area:.2f}")

print( "DESAFIO 07 ")

lado = float(input("Digite o tamanho do lado do quadrado: "))
area = lado ** 2
dobro_area = area * 2
print(f"O dobro da área do quadrado é {dobro_area}")

print( "DESAFIO 08 ")

valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario = valor_hora * horas_trabalhadas
print(f"O total do seu salário no referido mês é R${salario:.2f}")
 
print( "DESAFIO 09 ")

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)
print(f"A temperatura em Celsius é {celsius:.2f}")

print("Desafio 10")
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Fórmula de conversão de Celsius para Fahrenheit: F = C * 9/5 + 32
fahrenheit = celsius * 9/5 + 32

print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")

print("Desafio 11")

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite um número real: "))

produto = (2 * num1) * (num2 / 2)

soma = (3 * num1) + num_real

cubo = num_real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {produto}")
print(f"A soma do triplo do primeiro com o terceiro é: {soma}")
print(f"O terceiro elevado ao cubo é: {cubo}")

print("Desafio 12")

altura = float(input("Digite a altura da pessoa em metros: "))

peso_ideal = (72.7 * altura) - 58

print(f"O peso ideal para a altura de {altura}m é de aproximadamente {peso_ideal:.2f}kg")

print("Desafio 13")

altura = float(input("Digite a altura da pessoa em metros: "))
sexo = input("Digite o sexo da pessoa (M para masculino ou F para feminino): ")

if sexo.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem com altura de {altura}m é de aproximadamente {peso_ideal:.2f}kg")
elif sexo.upper() == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher com altura de {altura}m é de aproximadamente {peso_ideal:.2f}kg")
else:
    print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")


print("Desafio 14")

limite_peso = 50  
valor_multa_por_quilo = 4.00  

peso = float(input("Digite o peso de peixes em quilos: "))

if peso > limite_peso:
    excesso = peso - limite_peso
    multa = excesso * valor_multa_por_quilo
    print(f"O peso de peixes excedeu o limite em {excesso:.2f} quilos.")
    print(f"O valor da multa a ser pago é de R$ {multa:.2f}.")
else:
    print("O peso de peixes está dentro do limite permitido.")

print("Desafio 15")


valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))


salario_bruto = valor_hora * horas_trabalhadas


ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
total_descontos = ir + inss + sindicato


salario_liquido = salario_bruto - total_descontos


print(f"+ Salário Bruto : R$ {salario_bruto:.2f}")
print(f"- IR (11%) : R$ {ir:.2f}")
print(f"- INSS (8%) : R$ {inss:.2f}")
print(f"- Sindicato (5%) : R$ {sindicato:.2f}")
print(f"= Salário Liquido : R$ {salario_liquido:.2f}")

print("Desafio 16")
import math


cobertura_por_litro = 3  
litros_por_lata = 18     
preco_por_lata = 80.00   


area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))


litros_necessarios = area / cobertura_por_litro


latas_necessarias = math.ceil(litros_necessarios / litros_por_lata)


preco_total = latas_necessarias * preco_por_lata


print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}")


print("Desafio 17")

import math


cobertura_por_litro = 6  
litros_por_lata = 18     
preco_por_lata = 80.00   
litros_por_galao = 3.6   
preco_por_galao = 25.00  
folga = 1.1              


area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))


litros_necessarios = area / cobertura_por_litro * folga


latas_necessarias = math.ceil(litros_necessarios / litros_por_lata)


preco_total_latas = latas_necessarias * preco_por_lata


galoes_necessarios = math.ceil(litros_necessarios / litros_por_galao)


preco_total_galoes = galoes_necessarios * preco_por_galao


latas_misturadas = math.floor(litros_necessarios / litros_por_lata)
litros_resto = litros_necessarios % litros_por_lata
galoes_misturados = math.ceil(litros_resto / litros_por_galao)


preco_total_mistura = latas_misturadas * preco_por_lata + galoes_misturados * preco_por_galao


print(f"Quantidade de tinta a ser comprada:")
print(f"- Apenas latas de 18 litros: {latas_necessarias} latas")
print(f"- Preço total: R$ {preco_total_latas:.2f}")

print(f"\n- Apenas galões de 3.6 litros: {galoes_necessarios} galões")
print(f"- Preço total: R$ {preco_total_galoes:.2f}")

print(f"\n- Mistura de latas e galões:")
print(f"  - Latas: {latas_misturadas} latas")
print(f"  - Galões: {galoes_misturados} galões")
print(f"  - Preço total: R$ {preco_total_mistura:.2f}")

print("Desafio 18")

tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_link_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))


velocidade_link_mbps = velocidade_link_mbps / 8  

tempo_download_segundos = tamanho_arquivo_mb / velocidade_link_mbps


tempo_download_minutos = tempo_download_segundos / 60


print(f"O tempo aproximado de download do arquivo é de {tempo_download_minutos:.2f} minutos")

