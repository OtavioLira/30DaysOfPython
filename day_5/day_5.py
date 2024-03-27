# Como criar Listas
# Sintaxe
lista = list()

lista_vazia = list() # Isso é uma lista vazia, não tem item na lista
print(len(lista)) # 0

# Sintaxe - usando []
lst = []

lista_vazia = []
print(len(lista_vazia)) # 0

frutas = ["banana","laranja","manga","limão"]
vegetais = ["tomate","batata","repolho","cebola","cenoura"]
produtos_animais = ["leite","carne","manteiga","iorgute"]
web_techs = ["HTML","CSS","JS","React","Redux","Node","MongDB"]
paises = ["Finlandia","Estonia", "Denmark", "Sweden", "Norway"]

# Imprima as listas e seu comprimento
print("Frutas:", frutas)
print("quantidade de frutas: ", len(frutas))
print("Vegetais: ", vegetais)
print("quantidade de vegetais: ", len(vegetais))
print("Produtos animais: ", produtos_animais)
print("quantidade de produtos animais: ", len(produtos_animais))
print("Tecnologias web: ", web_techs)
print("Quantidade de tecnologias web: ", len(web_techs))
print("Paises: ", paises)
print("Quantidade de paises: ", len(paises))

lista = ["Otavio", 250, True, {"paises":"Brasil", "cidade":"São paulo"}] # lista contendo diferentes tipos de dados

# Acessando itens de lista usando indexação positiva
frutas = ["banana","laranja","manga","limao"]
primeira_fruta = frutas[0] # Estamos acessando o primeiro item usando o indice
print(primeira_fruta) # banana
segunda_fruta = frutas[1]
print(segunda_fruta) # laranja
ultima_fruta = frutas[3]
print(ultima_fruta) # limao
# Ultimo indice
ultimo_indice = len(frutas) - 1
ultima_fruta = frutas[ultimo_indice]

# Acessando itens de lista usando indexação negativa
frutas = ["banana","laranja","manga","limao"]
primeira_fruta = frutas[-4]
ultima_fruta = frutas[-1]
segunda_fruta = frutas[-2]
print(primeira_fruta) # banana
print(segunda_fruta) # limao
print(ultima_fruta) # manga

# Descompactando itens da lista
lista = ["item1", "item2", "item3", "item4", "item5"]
primeiro_item, segundo_item, terceiro_item, *resto = lista
print(primeiro_item) # item1
print(segundo_item) # item2
print(terceiro_item) # item3
print(resto) # ['item4','item5']

# Primeiro Exemplo
frutas = ["banana","laranja","manga","limao","lima","maça"]
primeira_fruta, segunda_fruta, terceira_fruta, *resto = frutas
print(primeira_fruta) # banana
print(segunda_fruta) # laranja
print(terceira_fruta) # manga
print(resto) # ['limão','lima','maça']

# Segundo Exemplo
primeiro, segundo, terceiro, *resto, decimo = [1,2,3,4,5,6,7,8,9,10]
print(primeiro)
print(segundo)
print(terceiro)
print(resto)
print(decimo)

# Terceiro exemplo
paises = ["Alemanha","França","Bélgica","Suécia","Dinamarca","Finlândia","Noruega","Islândia","Estônia"]
alemanha, franca, suecia, *resto, estonia = paises
print(alemanha)
print(franca)
print(suecia)
print(resto)
print(estonia)

# Fatiando itens de uma lista
frutas = ["banana","laranja","manga","limao"]
todas_frutas = frutas[0:4]

todas_frutas = frutas[0:]
laranja_manga = frutas[1:3]
laranja_manga_limao = frutas[1:]
laranja_limao = frutas[::2]

frutas = ["banana","laranja","manga","limao"]
todas_frutas = frutas[-4:]
laranja_manga = frutas[-3:-1]
laranja_manga_limao = frutas[-3:]
frutas_reversas = frutas[::-1]

# Modificando listas
frutas = ["banana","laranja","manga","limao"]
frutas[0] = "abacate"
print(frutas)
frutas[1] = "maca"
print(frutas)
ultimo_indice = len(frutas) - 1
frutas[ultimo_indice] = "lima"
print(frutas)

# Verificando itens na lista
frutas = ["banana","laranja","manga","limao"]
existe = "banana" in frutas
print(existe) # True
existe = "lima" in frutas
print(existe) # False

# Adicionando itens na lista
# Syntaxe

#lista = list()
#lista.append(item)

frutas = ["banana","laranja","manga","limao"]
frutas.append("maca")
print(frutas)
frutas.append("lima")
print(frutas)

# inserindo itens na lista

frutas = ["banana","laranja","manga","limao"]
frutas.insert(2, "maca")
print(frutas)
frutas.insert(3,"lima")
print(frutas)

# Removendo itens da lista
frutas = ["banana","laranja","manga","limao"]
frutas.remove("banana")
print(frutas)
frutas.remove("limao")
print(frutas)

# Removendo itens usando o POP
frutas = ["banana","laranja","manga","limao"]
frutas.pop()
print(frutas)

frutas.pop(0)
print(frutas)

# Removendo itens usando o DEL
frutas = ["banana","laranja","manga","limao"]
del frutas[0]
print(frutas)
del frutas[1]
print(frutas)
del frutas[1:3]
print(frutas)
#del frutas
#print(frutas)

# Limpando listas
frutas = ["banana","laranja","manga","limao"]
frutas.clear()
print(frutas)

# Copiando uma lista
frutas = ["banana","laranja","manga","limao"]
copia_frutas = frutas.copy()
print(copia_frutas)

# Juntando listas
numeros_positivos = [1, 2, 3, 4, 5]
zero =[0]
numeros_negativos = [-5, -4, -3, -2, -1]
inteiros = numeros_negativos + zero + numeros_positivos
print(inteiros)
frutas = ["banana","laranja","manga","limao"]
vegetais = ["tomate","batata","repolho","cebola","cenoura"]
frutas_vegetais = frutas + vegetais
print(frutas_vegetais)

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print("Numeros: ", num1)
numeros_negativos = [-5, -4, -3, -2, -1]
numeros_positivos = [1, 2, 3, 4, 5]
zero = [0]

numeros_negativos.extend(zero)
numeros_positivos.extend(numeros_positivos)
print("Inteiros: ", numeros_negativos)
frutas = ["banana","laranja","manga","limao"]
vegetais = ["tomate","batata","repolho","cebola","cenoura"]
frutas.extend(vegetais)
print("Frutas e vegetais: ", frutas)

# Contando itens da lista
frutas = ["banana","laranja","manga","limao"]
print(frutas.count("laranja"))
anos = [22, 19, 24, 25, 26, 24, 25, 24]
print(anos.count(24))

# Achando o index de um item na lista
frutas = ["banana","laranja","manga","limao"]
print(frutas.index("laranja"))
anos = [22, 19, 24, 25, 26, 24, 25, 24]
print(anos.index(24))

# invertendo a lista
frutas = ["banana","laranja","manga","limao"]
frutas.reverse()
print(frutas)
anos = [22, 19, 24, 25, 26, 24, 25, 24]
anos.reverse()
print(anos)

# Ordenando tens na lista
