# Função para registrar um novo usuário
def registrar(usuarios_registrados):
    usuario = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
    usuarios_registrados[usuario] = {'senha': senha, 'saldo': 0.0}
    print("Usuário registrado com sucesso!")

# Função para fazer login
def login(usuarios_registrados):
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if usuario in usuarios_registrados and usuarios_registrados[usuario]['senha'] == senha:
        print("Login bem-sucedido!")
        return usuario
    else:
        print("Usuário ou senha incorretos.")
        return None

# Função para apresentar o menu do usuário
def menu():
    print("\nMenu do Usuário")
    print("1 - Visualizar saldo")
    print("2 - Depositar reais")
    print("3 - Sacar reais")
    print("4 - Sair")

# Função para visualizar o saldo
def saldo(usuario, usuarios_registrados):
    print(f"Seu saldo atual é: R${usuarios_registrados[usuario]['saldo']:.2f}")

# Função para depositar reais
def depositar(usuario, usuarios_registrados):
    valor = float(input("Digite o valor a ser depositado: R$"))
    usuarios_registrados[usuario]['saldo'] += valor
    print(f"Depósito de R${valor:.2f} realizado com sucesso!")

# Função para sacar reais
def sacar(usuario, usuarios_registrados):
    valor = float(input("Digite o valor a ser sacado: R$"))
    if usuarios_registrados[usuario]['saldo'] >= valor:
        usuarios_registrados[usuario]['saldo'] -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque.")

# Programa principal
def main():
    usuarios_registrados = {}
    while True:
        print("\nBem-vindo!")
        opcao = input("Escolha uma opção:\n1. Registrar\n2. Login\n3. Sair\nOpção: ")
        if opcao == "1":
            registrar(usuarios_registrados)
        elif opcao == "2":
            usuario_logado = login(usuarios_registrados)
            if usuario_logado:
                while True:
                    menu()
                    opcao_menu = input("Escolha uma opção: ")
                    if opcao_menu == "1":
                        saldo(usuario_logado, usuarios_registrados)
                    elif opcao_menu == "2":
                        depositar(usuario_logado, usuarios_registrados)
                    elif opcao_menu == "3":
                        sacar(usuario_logado, usuarios_registrados)
                    elif opcao_menu == "4":
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
