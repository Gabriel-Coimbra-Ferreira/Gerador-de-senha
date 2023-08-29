#biblioteca que permite a geração dos numeros aleatorios
import random
#aqui eu estou puxando a biblioteca e declarando a variavel "senha de acesso" que pegara o numero que essa biblioteca gerar
Senha_de_acesso = random.randint(0, 9999)
#aqui estou declarando que pelo menos tenham 3 zeros a esquerda ou ao menos 4 numeros
senha_zero_esq = f'{Senha_de_acesso:04}'

print("Sua senha é")
print(senha_zero_esq)
senha_correta = input("Qual é a sua senha?")  # Input como string

# Converte a senha_correta para inteiro antes da comparação
if int(senha_zero_esq) == int(senha_correta):
    print("Senha correta, parabéns!")
else:
    print("Senha incorreta, tente novamente.")