print(True)
print(False)

#Operações Aritméticas em python
# Inteiros
print("Adição: ", 1 + 2) # 3
print("Subtração: ", 2 - 1) # 1
print("Multiplicação: ", 2 * 3) # 6
print("divisão: ", 4 / 2) # 2.0 # divisão no python retorna numero flutuante
print("divisão: ", 6 / 2)
print("divisão: ", 7 / 2)
print("Divisão sem o restante: ", 7 // 2) # 3.
print("Divisão sem o restante: ", 7 // 3) # 2
print("Resto da divisão: ", 3 % 2) #1
print("Exponencial: ", 2 ** 3) #9 isso significa 2 * 2 * 2

# Floating numbers
print("Numeros flutuante, PI", 3.14)
print("Numero flutuante, gravidade", 9.81)

# Numeros complexos
print("Numero complexo: ", 1 + 1j)
print("Multiplicação de numeros complexos: ", (1+1j) * (1-1j))

# Declarações de variavies no topo
a = 3
b = 2

# Operações aritméticas e associando os valores nas variaveis
total = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
div_piso = a // b
expo = a ** b

print(total)
print("a + b = ", total)
print("a - b =", subtracao)
print("a * b = ", multiplicacao)
print("a / b = ", divisao)
print("a % b = ",resto)
print("a // b =", div_piso)
print("a ** b", expo)

print('== adição, subtração, multiplicação, divisão, resto ==')

# Declarando os resultados e organizando
num1 = 3
num2 = 4

# Operaçõesa aritmeticas
total = num1 + num2
sub = num2 - num1
mult = num1 * num2
div = num2 / num1
resto = num2 % num1

# Imprimindo os valores e os rotulos
print('total: ', total)
print('subtração: ', subtracao)
print('multiplicação: ', mult)
print('divisão: ', divisao)
print('resto: ', resto)

# Calculando a area do circulo
raio = 10
area_circulo = 3.14 * raio ** 2
print("Area do circulo: ", area_circulo)

# Calculando a area do retangulo
altura = 10
largura = 20
area_retangulo = altura * largura
print("Area do retangulo: ", area_retangulo)

# Calculando a largura de um objeto
massa = 75
gravidade = 9.81
peso = massa * gravidade
print(peso, "N")

# Calculando a densidade do liquido
massa = 75 # em quilos
volume = 0.075 # em metros cubicos
densidade = massa / volume # 1000 Kg/m^3

# Operadores de comparação
print(3 > 2) # True
print(3 >= 2) # true
print(3 < 2) # False
print(2 <= 3) # True
print(3 == 2) # False
print(3 != 2) # True
print(len("mango") == len("avocado")) # False
print(len("mango") != len("avocado")) # True
print(len("mango") < len("avocado")) # True
print(len("milk") != len("meat")) # False
print(len("milk") == len("meat")) # True
print(len("tomato") == len("potato")) # True
print(len("python") > len("dragon")) # False

# Comparar algo da verdadeiro ou falso
print("True == True: ", True == True)
print("True == False:", True == False)
print("False == False: ", False == False)
 
print("1 == 1", 1 == 1) # True - os valores são iguais
print("1 is not 2", 1 is not 2) # True - 1 não é 2
print("A in Otavio", "a" in "Otavio") # True - A foi encontrado na string
print("T in Otavio", "T" in "Otavio") # False - naõ tem T maiúscula na string
print("codar in codar é para todos", "codar" in "codar é para todos") # True - 'codar' está na string 'codar é para todos'
print("O in Ola: ", "O" in "Ola") # True
print("4 is 2 ** 2: ", 4 is 2 ** 2) # True

print(3 > 2 and 4 > 3) # True - ambas as condições são verdadeiras
print(3 > 2 and 4 < 3) # False - a segunda condição é falsa
print(3 < 2 and 4 < 3) # False - ambas as condições são falsas
print("True and True", True and True)
print(3 > 2 or 4 > 3) # True - ambas as condições são verdadeiras
print(3 > 2 or 4 < 3) # True - uma das condições é verdadeira
print(3 < 2 or 4 < 3) # False - ambas as condições são falsas
print("True or False", True or False)
print(not 3 > 2) # False - 3 > 2 é verdadeiro, então not True retornar False
print(not True) # False - Negação, o operador not torna true em false
print(not False) # True
print(not not True) # True
print(not not False) # False

# Desafios (incompleto)
age = 10
peso = 76.6
complex_number = 4 + 4j

print("area do triângulo")
base = int(input("Digite a base: "))
altura = int(input("Digite a altura: "))
print("A area do triangulo é ", 0.5 * base * altura)

print("Perímetro do triângulo")
ladoA = int(input("Digite o lado A: "))
ladoB = int(input("Digite o lado B: "))
ladoC = int(input("Digite o lado C: "))
print("O perímetro do triângulo é ", ladoA + ladoB + ladoC)

print("Area do triângulo")
altura = int(input("Digite a altura do triângulo: "))
largura = int(input("Digite a largura do triângulo: "))
print("A area do triângulo é ", altura * largura, " é o perímetro é ", 2 * (altura * largura))

print("Raio Circulo")
raio = int(input("Digite o raio do circulo: "))
print("Área do circulo: ", 3.14 * raio * raio, "\nCircunferência: ", 2 * 3.14 * raio)

inclinacao = 2
y_intersecao = 2*0 - 2
x_intersecao = -(-2) / inclinacao

print("Inclinação: ", inclinacao)
print("Interseção do eixo Y: ", y_intersecao)
print("Interseção do eixo X: ", x_intersecao)

import math

x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Inclinação (slope):", slope)
print("Distância euclidiana:", distance)

