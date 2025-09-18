# #Questão 1 – Saudação personalizada (Função simples)
# def saudacao(nome):
#     return f"Olá,{nome}! Seja bem-vindo ao curso de lógica de programação."
# print(saudacao("ana"))

#Questão 2 – Par ou Ímpar (Condicional + Função)
# def par_ou_impar(numero):
#     if numero % 2 == 0:
#         return "par"
#     else: return "impar"
# print(f"O número 1 é {par_ou_impar(1)}")

#Questão 3 – Maior de dois números (Condicional)
# n1 = float(input("Digite meu primeiro valor:"))
# n2 = float(input("Digite meu segundo valor:"))
# if n1 > n2:
#     print(f"{n1} é maior que {n2}")
# if n2 > n1:
#     print(f"{n2} é maior que {n1}")
# if  n1 == n2:
#     print(f"{n1} e {n2} são iguais")     

#Questão 4 – Tabuada (Repetição)
# numero= int(input("Digite um valor:"))
# for i in range(1, 11):

#Questão 5 – Contagem regressiva (Laço)
# for contagem in range(1,11):
#     print(contagem)
# print("EXPLOSÃO!!!!!!!!!!!!!!!!!")

#Questão 6 – Média de notas (Função + Repetição)
# def calcular_media():
#     quntidade_notas = int(input("Quantas notas você quer calcular a média?: "))
#     total = 0
#     for i in range(quntidade_notas):
#         nota = float(input(f"Digite a {i+1}ª nota: "))
#         total += nota
#     media = total / quntidade_notas
#     return media
# media = calcular_media()
# print(f"A média das notas é: {media}")

# #Questão 7 – Fatorial (Repetição + Função)
# numero = int(input("Digite um número para que seja exibido seu fatorial:"))
# fatorial = 1
# for i in range(1, numero + 1):
#     fatorial *= i
# print(f"O fatorial de {numero} é {fatorial}")

# #Questão 8 – Verificar vogais (Função + String)
# ContarVogais = input("Digite uma palavra:")
# vogais = "aeiou"
# contador = 0
# for letra in ContarVogais : 
#     if letra in vogais:
#         contador += 1
# print(f"A palavra {ContarVogais} possui {contador} vogais.")

# #Questão 9 – Jogo de adivinhação (Laço + Condicional)
# def jogo_adivinhacao():
#     numero_secreto = 7
#     chute = 0
#     tentativas = 0
#     print("Jogo de Adivinhação")
#     while chute != numero_secreto:
#         chute = int(input("Digite um número entre 1 e 10: "))
#         tentativas += 1
#         if chute == numero_secreto:
#             print(f"Parabéns! Você acertou em {tentativas} tentativas!")
#         elif chute < numero_secreto:
#             print("O número é MAIOR. Tente novamente.")
#         else:
#             print("O número é MENOR. Tente novamente.")
# jogo_adivinhacao()