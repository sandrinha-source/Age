nome = input("Digite o seu nome: ")
nascimento = int(input("Digite o ano em que você nasceu: "))
mes = int(input("Digite o mês que você nasceu (número): "))

ano_atual = 2026
mes_atual = 3

idade = ano_atual - nascimento

if mes > mes_atual:
    idade = idade - 1

print("Olá,", nome, "você tem", idade, "anos")
