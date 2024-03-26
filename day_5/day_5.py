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
print(resto) # ['lima','maça']


