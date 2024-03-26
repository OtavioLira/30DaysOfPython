# Criando Strings

letra = "p" # Uma string pode ser uma letra ou um monte de textos
print(letra) #P
print(len(letra)) #1
saudacao = 'Hello, World!' # A string pode ser feita usando aspas simples ou duplas, "Hello, World!"
print(saudacao) # Hello, World!
print(len(saudacao)) # 13
frase = "Eu espero que você esteja aproveitando o desafio de 30 dias de python"
print(frase)

string_multilinha = '''Sou professor e 
gosto de ensinar. Não achei nada tão gratificante quanto capacitar asa pessoas. É por isso que criei 30 dias de python'''
print(string_multilinha)

# Outra forma de fazer a mesma coisa
string_multilinha = """Sou professor e 
gosto de ensinar. Não achei nada tão gratificante quanto capacitar asa pessoas. É por isso que criei 30 dias de python"""
print(string_multilinha)

# Concatenação de Strings
primeiro_nome = "Otavio"
sobrenome = "Lira Neves"
espaco = " "
nome_completo = primeiro_nome + espaco + sobrenome
print(nome_completo) # Otávio Lira Neves

# Verificando o comprimento de uma string usando a função interna len()
print(len(primeiro_nome)) # 6 
print(len(sobrenome)) # 10
print(len(primeiro_nome) > len(sobrenome)) # True 
print(len(nome_completo)) # 17

# Sequência de escape em strings
print("Espero que todos estejam gostando do Desafio Python. \nE você?") # Pulando linha
print("Dias\tTópicos\tExercícios") # addicionando espaço de tabulação(tab) ou 4 espaços
print("Dia 1 \t5\t5")
print("Dia 2 \t6\t20")
print("Dia 3 \t5\t23")
print("Dia 4 \t1\t35")
print("Este é um símbolo de barra invertida (\\)") # para escrever a barra invertida -> \
print('Em toda linguagem de programação começa com \"Hello, World!\"') # Para escrever aspas dupla dentro de uma aspas simples

# Formatação de Strings (Antigo)
# Apenas Strings
primeiro_nome = "Otavio"
sobrenome = "Lira Neves"
linguagem = "Python"
string_formatada = "Eu sou %s %s. Eu ensino %s" %(primeiro_nome, sobrenome, linguagem)
print(string_formatada)

# Strings e numeros
raio = 10
pi = 3.14
area = pi * raio ** 2
string_formatada = "A area do circulo com o raio %d é %.2f" %(raio, area) # 2 refere-se aos 2 dígitos significativos após o ponto
print(string_formatada)

python_libraries = ["Django", "Flask", "NumPy", "Matplotlib", "Pandas"]
string_formatada = "A seguir são bibliotecas python:%s" % (python_libraries)
print(string_formatada)

# Formatação de Strings (Nova)
primeiro_nome = "Otavio"
sobrenome = "Lira Neves"
linguagem = "Python"
string_formatada = 'Eu sou {} {}. Eu ensino {}'.format(primeiro_nome, sobrenome, linguagem)
print(string_formatada)
a = 4
b = 3

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b)) # limita a dois digitos após o decimal
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))

# Strings e numeros
raio = 10
pi = 3.14
area = pi * raio ** 2
string_formatada = "A area do circulo com o raio {} é {:.2f}".format(raio, area)
print(string_formatada)

# Strings Python como sequências de caracteres
linguagem = "Python"
a,b,c,d,e,f = linguagem
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Acessando caracteres em strings por índice
linguagem = "Python"
primeira_letra = linguagem[0]
print(primeira_letra) # P
segunda_letra = linguagem[1]
print(segunda_letra) # y
ultimo_index = len(linguagem) - 1
ultima_letra = linguagem[ultimo_index]
print(ultima_letra) # n 

linguagem = "Python"
ultima_letra = linguagem[-1]
print(ultima_letra) # n
penultima_letra = linguagem[-2]
print(penultima_letra) # o

# Fatiando Strings em Python
linguagem = "Python"
primeiro_terceiro = linguagem[0:3] # começa nm indice zero e vai até o terceiro, mas não inclui o terceiro
print(primeiro_terceiro) # Pyt
ultimo_terceiro = linguagem[3:6]
print(ultimo_terceiro) # hon
# Outra forma
ultimo_terceiro = linguagem[-3:]
print(ultimo_terceiro) # hon
ultimo_terceiro = linguagem[3:]
print(ultimo_terceiro) # hon

# invertendo uma string
saudacao = "Hello, World!"
print(saudacao[::-1]) # !dlroW ,olleH

# Pulando caracteres ao fatiar
linguagem = "Python"
pto = linguagem[0:6:2]
print(pto) # Pto

#Métodos Strings
desafio = "trinta dias de python"

# Converte o primeiro caracter da string para letra maiúscula
print(desafio.capitalize()) # Trinta dias de python

# Converte o primeiro caracter da string para letra maiúscula
desafio = "thirty days of python"
print(desafio.count("y")) # 3
print(desafio.count("y", 7, 14)) # 1
print(desafio.count("th")) # 2

# Verifica se uma string termina com um final especificado
print(desafio.endswith("on")) # True
print(desafio.endswith("tion")) # False

# Substitui o caractere de tabulação por espaços, o tamanho da tabulação padrão é 8. É necessário o argumento do tamanho da tabulação
desafio = "thirty\tdays\tof\tpython"
print(desafio.expandtabs()) # 'thirty  days    of      python'
print(desafio.expandtabs(10)) # 'thirty    days      of        python'

# Retorna o índice da primeira ocorrência de uma substring, se não for encontrado retorna -1
desafio = "thirty days of python"
print(desafio.find("y")) # 5
print(desafio.find("th")) # 0

# Retorna o índice da última ocorrência de uma substring, se não for encontrado retorna -1
print(desafio.rfind("y")) # 16
print(desafio.rfind("th")) # 17

# Retorna o índice mais baixo de uma substring, argumentos adicionais indicam o índice inicial e final (padrão 0 e comprimento da string - 1). Se a substring não for encontrada, gera um valueError.
sub_string = "da"
print(desafio.index(sub_string)) # 7
print(desafio.index(sub_string, 9)) # error

# Retorna o índice mais alto de uma substring, argumentos adicionais indicam o índice inicial e final (padrão 0 e comprimento da string - 1)
print(desafio.rindex(sub_string)) # 8
print(desafio.rindex(sub_string, 9)) # error

# Verifica caracteres alfanuméricos
desafio = "ThirtyDaysPython"
print(desafio.isalnum()) # True

desafio = "30DaysPython"
print(desafio.isalnum()) # True

desafio = "thirty days of python"
print(desafio.isalnum()) # Falso, espaço não é um caractere alfanumérico

desafio = 'thirty days of python 2019'
print(desafio.isalnum()) # False

# Verifica se todos os elementos da string são caracteres alfabéticos (a-z e A-Z)
desafio = "thirty days of python"
print(desafio.isalnum()) # False, o espaço mais uma vez é excluido

desafio = "ThirtyDaysPython"
print(desafio.isalpha()) # True

num = "123"
print(desafio.isalpha()) # False

# Verifica se todos os caracteres de uma string são decimais (0-9)
desafio = "thirty days of python"
print(desafio.isdecimal()) # False
desafio = "123"
print(desafio.isdecimal()) # True
desafio = "\u00B2"
print(desafio.isdecimal()) # False
desafio = "12 3"
print(desafio.isdecimal()) # False, espaço não é permitido

# Verifica se todos os caracteres em uma string são números (0-9 e alguns outros caracteres Unicode para números)
desafio = "Thirty"
print(desafio.isdigit()) # False
desafio = "30"
print(desafio.isdigit()) # True
desafio = "\u00B2"
print(desafio.isdecimal()) # True

# Verifica se todos os caracteres em uma string são números ou estão relacionados a números (assim como isdigit(), apenas aceita mais símbolos, como ½)
num = "10"
print(num.isnumeric()) # True
num = "\u00bD" # ½
print(num.isnumeric()) # True
num = "10.5"
print(num.isnumeric()) # False

# Verifica se há um identificador válido - verifica se uma string é um nome de variável válido
desafio = "30DaysOfPython"
print(desafio.isidentifier()) # False, começa com um numero
desafio = "thirty_days_of_python"
print(desafio.isidentifier()) # True

# Verifica se todos os caracteres do alfabeto na string estão minúsculos
desafio = "thirty days of python"
print(desafio.islower()) # True
desafio = "Thirty days of python"
print(desafio.islower()) # False

# Verifica se todos os caracteres do alfabeto na string estão maiúsculos
desafio = "thirty days of python"
print(desafio.isupper()) # False
desafio = "THIRTY DAYS OF PYTHON"
print(desafio.isupper()) # True

# Retorna uma string concatenada
web_tech = ["HTML","CSS","JavaScript","React"]
resultado = " ".join(web_tech)
print(resultado) # HTML CSS JavaScript React

web_tech = ["HTML","CSS","JavaScript","React"]
resultado = "# ".join(web_tech)
print(resultado) # 'HTML# CSS# JavaScript# React'

# Remove todos os caracteres fornecidos, começando do início e do final da string
desafio = "thirty days of pythoonnn"
print(desafio.strip("noth")) # 'irty days of py'

# Substitui substring por uma determinada string
desafio = "thirty days of python"
print(desafio.replace("python","coding")) # thirty days of coding

# Divide a string, usando determinada string ou espaço como separador
desafio = "thirty days of python"
print(desafio.split()) # ['thirty', 'days', 'of', 'python']
desafio = "thirty, days, of, python"
print(desafio.split(",")) # ['thirty', 'days', 'of', 'python']

# Retorna uma string com título
desafio = "thirty days of python"
print(desafio.title())

# Converte todos os caracteres maiúsculos em minúsculos e todos os caracteres minúsculos em maiúsculos
desafio = "thirty days of python"
print(desafio.swapcase()) # THIRTY DAYS OF PYTHON
desafio = "Thirty Days Of Python"
print(desafio.swapcase()) # tHIRTY dAYS oF pYTHON

# Verifica se a string começa com a string especificada
desafio = "thirty days of python"
print(desafio.startswith("thirty")) # True

desafio = "30 days of python"
print(desafio.startswith("thirty")) # False