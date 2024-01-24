import random


def gerar_senha_complexa():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=[]{}|;:'<>,.?/"
    senha_complexa = ''.join(random.sample(caracteres, 12))
    return senha_complexa


tentativas_maximas = 3
tentativas = 0

senha_zero_esq = f'{random.randint(0, 9999):04}'
senha_complexa = gerar_senha_complexa()

while tentativas < tentativas_maximas:
    print("Escolha uma opção:")
    print("1. Gerar senha de acesso")
    print("2. Tentar entrar")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        senha_zero_esq = f'{random.randint(0, 9999):04}'
        print("Sua nova senha de acesso é:")
        print(senha_zero_esq)
    elif opcao == "2":
        senha_correta = input("Qual é a sua senha?")  # Input como string

        if senha_zero_esq == senha_correta:
            print("Senha de acesso correta, parabéns!")
            break
        elif senha_correta == senha_complexa:
            print("Senha complexa correta, parabéns!")
            break
        else:
            if tentativas < tentativas_maximas - 1:
                print("Senha incorreta. Tente novamente.")
            else:
                print("Senha incorreta. Última tentativa.")

            tentativas += 1
    else:
        print("Opção inválida. Tente novamente.")

if tentativas == tentativas_maximas:
    print("Número máximo de tentativas atingido. Acesso bloqueado.")
