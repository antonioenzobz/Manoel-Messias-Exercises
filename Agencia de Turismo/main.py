from functions import menu_cliente, menu_agencia, Clientes, PacotesDisponiveis, PacotesVendidos

try:
    # Inicializa pacotes disponíveis com dados predefinidos
    Clientes.update({
        "Carlinhos Almeida Pinto": {
            "Idade": "43",
            "CPF": "05675486311",
            "Email": "carlinhos63041@gmail.com",
            "Endereço": "Rio de Janeiro-RJ, bairro Corinthiano, Rua Cavalos Doceis 64",
            "Telefone": "89981765412"
        },
        "Dalva Ribeiro Dias": {
            "Idade": "32",
            "CPF": "93510361166",
            "Email": "dalvadias@gmail.com",
            "Endereço": "São Paulo-SP, bairro Jardins, Rua das Flores 123",
            "Telefone": "11987654321"
        },
        "Cleide Oliveira dos Santos": {
            "Idade": "37",
            "CPF": "93519615952",
            "Email": "cleiders789@gmail.com",
            "Endereço": "Belo Horizonte-MG, bairro Savassi, Avenida Getúlio Vargas 456",
            "Telefone": "31987654321"
        }
    })

    PacotesDisponiveis.update({
        "Pacote Básico": {
            "Local": "Rio de Janeiro",
            "Preço": "R$ 1.200",
            "Quantidades disponíveis": "20",
            "Descrição": "Inclui 3 dias e 2 noites em um hotel 3 estrelas, com café da manhã incluso e passeios pelo Cristo Redentor e Pão de Açúcar."
        },
        "Pacote Aventura": {
            "Local": "Foz do Iguaçu",
            "Preço": "R$ 1.800",
            "Quantidades disponíveis": "15",
            "Descrição": "5 dias e 4 noites com hospedagem em um hotel 4 estrelas, incluindo passeios às Cataratas do Iguaçu, passeio de barco e trilhas pela mata atlântica."
        },
        "Pacote Cultural": {
            "Local": "Salvador",
            "Preço": "R$ 1.500",
            "Quantidades disponíveis": "25",
            "Descrição": "4 dias e 3 noites em um hotel boutique com café da manhã, incluindo visitas ao Pelourinho, Mercado Modelo e um tour gastronômico pela cidade."
        },
        "Pacote Relaxamento": {
            "Local": "Campos do Jordão",
            "Preço": "R$ 2.000",
            "Quantidades disponíveis": "10",
            "Descrição": "6 dias e 5 noites em um resort spa, com acesso a tratamentos de bem-estar, massagens e atividades de relaxamento em meio à natureza."
        },
        "Pacote Família": {
            "Local": "Fortaleza",
            "Preço": "R$ 2.500",
            "Quantidades disponíveis": "18",
            "Descrição": "7 dias e 6 noites em um resort all-inclusive com atividades para crianças e adultos, incluindo passeios à Praia do Futuro e ao Parque do Cocó."
        }
    })

    PacotesVendidos.update({
        "Itadori Yuji": [{
            "Pacote": "Pacote Relaxamento",
            "Local": "Campos do Jordão",
            "Preço": "R$ 2.000",
            "Descrição": "6 dias e 5 noites em um resort spa, com acesso a tratamentos de bem-estar, massagens e atividades de relaxamento em meio à natureza."
        }],
        "Geto Suguro": [{
            "Pacote": "Pacote Família",
            "Local": "Fortaleza",
            "Preço": "R$ 2.500",
            "Descrição": "7 dias e 6 noites em um resort all-inclusive com atividades para crianças e adultos, incluindo passeios à Praia do Futuro e ao Parque do Cocó."
        }]
    })

    # Inicializa o sistema perguntando o perfil do usuário
    print("Bem-vindo ao menu da agência! Selecione seu perfil:")
    print("1 - Cliente")
    print("2 - Agência")
    usuario = input("Digite o número correspondente: ")

    # Chama a função apropriada com base na escolha do usuário
    if usuario == "1":
        menu_cliente()
    elif usuario == "2":
        menu_agencia()
    else:
        print("Entrada inválida!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    print("Execução finalizada.")
