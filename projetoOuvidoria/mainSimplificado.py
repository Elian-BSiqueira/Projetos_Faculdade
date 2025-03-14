"""
Grupo: Elian Barros
       Lucas Vicent
       Luiz Matheus Farias
       Rafael Barbosa de Melo
"""


# Etapa 1
# Codigo simplificado sem usar bloco try except ou verificacoes complexas

# Inicializa a variável de controle do loop e a lista de manifestações
opcao = -1
listaDeManifestacoes = []

# Loop principal do sistema
while opcao != 5:
    # Exibe o menu de opções para o usuário
    print("1) Listagem das Manifestações\n"
          "2) Criar uma nova Manifestação\n"
          "3) Exibir quantidade de manifestações\n"
          "4) Pesquisar uma manifestação por código\n"
          "5) Sair do Sistema")

    # Captura a opção do usuário e converte para inteiro
    opcao = int(input("Digite sua opcao: "))

    # Valida a entrada para garantir que esteja no intervalo correto (1 a 5)
    while opcao <= 0 or opcao > 5:
        print(f"ERRO. opcao invalida")  # Mensagem de erro
        opcao = int(input("Digite sua opcao: "))

    # Opção 1: Listar manifestações
    if opcao == 1:
        if not listaDeManifestacoes:
            print("Nao ha manifestacoes")  # Caso não haja manifestações cadastradas
        else:
            contador = 1  # Inicia contador para numerar as manifestações
            for manif in listaDeManifestacoes:
                print(f"{contador}) {manif}")  # Exibe cada manifestação numerada
                contador += 1

    # Opção 2: Criar uma nova manifestação
    elif opcao == 2:
        manifestacao = input("Descreva sua manifestacao: ")  # Captura a descrição
        listaDeManifestacoes.append(manifestacao)  # Adiciona à lista
        print(f"Manifestacao cadastrada com sucesso. Seu codigo e {len(listaDeManifestacoes)}")

    # Opção 3: Exibir a quantidade de manifestações cadastradas
    elif opcao == 3:
        print(f"Existem {len(listaDeManifestacoes)} manifestacoes cadastradas")

    # Opção 4: Pesquisar manifestação por código
    elif opcao == 4:
        codigo = int(input("Digite o codigo da manisfetacao: "))  # Captura código
        print(f"{codigo}) {listaDeManifestacoes[codigo - 1]}")  # Exibe manifestação

    # Opção 5: Sair do sistema
    elif opcao == 5:
        print("Saindo do programa. Obrigado por usar")
