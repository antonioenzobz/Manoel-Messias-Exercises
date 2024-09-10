# Dicionários globais para armazenar clientes e pacotes
Clientes = {}
PacotesDisponiveis = {}
PacotesVendidos = {}

def print_pacotes(pacotes):
    print("========================= Pacotes ==========================")
    for pacote, detalhes in pacotes.items():
        print(f"Pacote: {pacote}")
        for chave, valor in detalhes.items():
            print(f"{chave}: {valor}")
        print()
    print("====================================================================")

def menu_cliente():
    global Clientes
    try:
        print("Antes de comprar nossos pacotes, vamos precisar de algumas informações suas.")
        nome = input("Nome Completo: ")
        cpf = input("CPF (sem pontos e hífen): ")

        if not validar_cpf(cpf):
            raise ValueError("CPF inválido.")

        email = input("Email: ")
        idade = int(input("Idade: "))
        endereco = input("Endereço: ")
        telefone = int(input("Telefone: "))

        Clientes[nome] = {
            "Idade": idade,
            "CPF": cpf,
            "Email": email,
            "Endereço": endereco,
            "Telefone": telefone
        }
        print("Pronto, você já pode usar nossos serviços!")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Erro inesperado: {e}")
    else:
        while True:
            try:
                print("======================== Agencia de Turismo ========================")
                print("1 - Pacotes à Venda")
                print("2 - Minhas Compras")
                print("3 - Informação do usuário")
                print("====================================================================")
                
                opçãoCliente = input("Digite a opção desejada: ")

                if opçãoCliente == "1":
                    print_pacotes(PacotesDisponiveis)
                    print("1 - Comprar pacote")
                    print("2 - Voltar")
                    ComprarP = input("Digite a opção desejada: ")
                    if ComprarP == "1":
                        pacote_escolhido = input("Digite o nome do pacote que deseja comprar: ")
                        if pacote_escolhido in PacotesDisponiveis:
                            if int(PacotesDisponiveis[pacote_escolhido]["Quantidades disponíveis"]) > 0:
                                PacotesDisponiveis[pacote_escolhido]["Quantidades disponíveis"] = str(int(PacotesDisponiveis[pacote_escolhido]["Quantidades disponíveis"]) - 1)
                                if nome not in PacotesVendidos:
                                    PacotesVendidos[nome] = []
                                PacotesVendidos[nome].append({
                                    "Pacote": pacote_escolhido,
                                    "Local": PacotesDisponiveis[pacote_escolhido]["Local"],
                                    "Preço": PacotesDisponiveis[pacote_escolhido]["Preço"],
                                    "Descrição": PacotesDisponiveis[pacote_escolhido]["Descrição"]
                                })
                                print(f"Você comprou o {pacote_escolhido} com sucesso!")
                            else:
                                print("Desculpe, este pacote não está mais disponível.")
                        else:
                            print("Pacote inválido.")
                    elif ComprarP == "2":
                        continue
                    else:
                        print("Opção inválida!")
                        
                elif opçãoCliente == "2":
                    if nome in PacotesVendidos:
                        print(f"Pacotes comprados por {nome}:")
                        for pacote in PacotesVendidos[nome]:
                            print(f"  {pacote['Pacote']} em {pacote['Local']} por {pacote['Preço']}")
                            print(f"  Descrição: {pacote['Descrição']}")
                        print()
                    else:
                        print(f"{nome} não comprou nenhum pacote ainda.")

                
                elif opçãoCliente == "3":
                    print("========================= Suas Informações =========================")
                    print(f"Nome: {nome}")
                    print(f"CPF: {cpf}")
                    print(f"Idade: {idade}")
                    print(f"Email: {email}")
                    print(f"Endereço: {endereco}")
                    print("====================================================================")
                    
                else:
                    print("Opção inválida!")
            except Exception as e:
                print(f"Erro ao processar a opção: {e}")
            finally:
                print("Fim da operação do cliente.")

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    digito1 = digito1 if digito1 < 10 else 0
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11)
    digito2 = digito2 if digito2 < 10 else 0
    return cpf[-2:] == f"{digito1}{digito2}"

def menu_agencia():
    global Clientes, PacotesDisponiveis, PacotesVendidos
    try:
        while True:
            print("===================== Menu da Agência =====================")
            print("1 - Consultar Clientes")
            print("2 - Consultar Pacotes Disponíveis")
            print("3 - Consultar Pacotes Vendidos")
            print("===========================================================")

            opcaoAgencia = input("Digite a opção desejada: ")

            if opcaoAgencia == "1":
                print("============ Clientes ============")
                for cliente, detalhes in Clientes.items():
                    print(f"Cliente: {cliente}")
                    for chave, valor in detalhes.items():
                        print(f"{chave}: {valor}")
                    print()
                print("==================================")

            elif opcaoAgencia == "2":
                print_pacotes(PacotesDisponiveis)

            elif opcaoAgencia == "3":
                print("======================== Pacotes Vendidos ========================")
                for cliente, pacotes in PacotesVendidos.items():
                    print(f"Cliente: {cliente}")
                    for pacote in pacotes:
                        print(f"  Pacote: {pacote['Pacote']} em {pacote['Local']} por {pacote['Preço']}")
                        print(f"  Descrição: {pacote['Descrição']}")
                    print()
                print("====================================================================")

            else:
                print("Opção inválida!")
    except Exception as e:
        print(f"Erro inesperado no menu da agência: {e}")
    finally:
        print("Operação da agência finalizada.")
