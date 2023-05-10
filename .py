# Lista com as perguntas sobre o crime
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?",
             "Devia para a vítima?", "Já trabalhou com a vítima?"]

# Variável para contar o número de respostas positivas
num_respostas_positivas = 0

# Loop para fazer as perguntas e obter as respostas
for pergunta in perguntas:
    resposta = input(pergunta + " (sim ou não): ")
    if resposta.lower() == "sim":
        num_respostas_positivas += 1

# Emitir a classificação com base no número de respostas positivas
if num_respostas_positivas == 2:
    print("Suspeita")
elif 3 <= num_respostas_positivas <= 4:
    print("Cúmplice")
elif num_respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")
