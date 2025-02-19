def registrar(usuarios_registrados):

    usuario = input("Digite um nome de usuário: ")

    senha = input("Digite uma senha: ")

    usuarios_registrados[usuario] = senha

    print("Usuário registrado com sucesso!")

def login(usuarios_registrados):

    usuario = input("Digite seu nome de usuário: ")

    senha = input("Digite sua senha: ")

    if usuario in usuarios_registrados and usuarios_registrados[usuario] == senha:
        print("Login bem-sucedido!")
        return True
    else:
        print("Usuário ou senha incorretos.")
        return False


def menu():
    print("Menu do Usuário")
    print("1 - Visualizar saldo")
    print("2 - Fazer investimento")
    print("3 - Visualizar carteira")
    print("4 - Sair")

def saldo():
    print("Saldo")

def investimento():
    print("Investimento")

def carteira():
    print("Visualizar a carteira de investimentos")

def main():
    usuarios_registrados = {}

    while True:
        print("Bem-vindo!")
        opcao = input("Escolha uma opção:\n1. Registrar\n2. Login\n3. Sair\nOpção: ")
        
        if opcao == "1":
            registrar(usuarios_registrados)
        elif opcao == "2":
            if login(usuarios_registrados):
                while True:
                    menu()
                    opcao = input("Escolha uma opção: ")
                    if opcao == "1":
                        saldo()
                    elif opcao == "2":
                        investimento()
                    elif opcao == "3":
                        carteira()
                    elif opcao == "4":
                        print("Saindo do menu do usuário...")
                        break
                    else:
                        print("Opção incorreta. Por favor, escolha uma das opções acima.")
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção incorreta. Por favor, escolha uma das opções acima.")

if __name__ == "__main__":
    main()
