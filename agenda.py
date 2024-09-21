def adicionar_contato(contatos, nome_contato, telefone_contato):

    contato = {"contato": nome_contato, "telefone": telefone_contato, "favorito": False}
    contatos.append(contato)
    print(f"\nTelefone de {nome_contato} foi adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "☆" if contato["favorito"] else " "
        nome_contato = contato["contato"]
        telefone_contato = contato["telefone"]
        print(f"{indice}. {nome_contato} - Telefone: {telefone_contato} {status}")
    return

def atualizar_nome_contato(contatos, indice_contato, novo_nome_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["contato"] = novo_nome_contato
        print(f"\nContato {indice_contato} atualizado para {novo_nome_contato}")
    else:
        print("\nÍndice de tarefa inválido.")
    return
def atualizar_telefone_contato(contatos, indice_contato, novo_telefone_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone_contato
        print(f"\nContato {indice_contato} atualizado para {novo_telefone_contato}")
    else:
        print("\nÍndice de tarefa inválido.")
    return

def marcar_favorito(contatos, indice_contato):
    try:
        indice_contato_ajustado = int(indice_contato) - 1  # Ajuste para índice começar em 0
        if indice_contato_ajustado < 0 or indice_contato_ajustado >= len(contatos):
            print("Índice fora do intervalo. Por favor, escolha um índice válido.")
            return
        
        if contatos[indice_contato_ajustado]["favorito"] == False:
            contatos[indice_contato_ajustado]["favorito"] = True
            print(f"Contato {contatos[indice_contato_ajustado]['contato']} foi marcado como favorito.")
        else:
            contatos[indice_contato_ajustado]["favorito"] = False
            print(f"Contato {contatos[indice_contato_ajustado]['contato']} foi desmarcado como favorito.")
    
    except (ValueError, IndexError):
        print("Erro: O índice informado é inválido.")


def ver_lista_favoritos(contatos):
    print("\nContatos Favoritos:")
    favoritos = [contato for contato in contatos if contato["favorito"]]  # Filtra os favoritos
    if not favoritos:
        print("\nNenhum contato favorito encontrado.")
        return

    for contato in favoritos:
        nome_contato = contato["contato"]
        telefone_contato = contato["telefone"]
        print(f"Nome: {nome_contato} - Telefone: {telefone_contato}")
    return

def deletar_contato(contatos):
    if not contatos:
        print("\nA lista de contatos está vazia!")
        return
    try:
        escolha = int(input("\nDigite o número do contato que deseja deletar: "))
        if escolha < 1 or escolha > len(contatos):
            print("\nEscolha inválida. Tente novamente.")
        else:
            contato_removido = contatos.pop(escolha - 1)  # Remove o contato com base no índice
            print(f"\nContato {contato_removido['contato']} foi removido com sucesso!")
    except ValueError:
        print("\nEntrada inválida. Digite um número válido.")
    return

contatos = []
while True:
    print("\nMenu do Gerenciador de Lista de Contatos:")
    print("1. Adicionar Contato")
    print("2. Ver Agenda")
    print("3. Atualizar Contato")
    print("4. Marcar ou desmarcar como Favorito")
    print("5. Ver lista de Favoritos")
    print("6. Deletar Contato")
    print("7. Sair")

    escolha = input("\nDigite a sua escolha:")

    if escolha == "1":
        nome_contato = input("\nDigite o nome do contato que deseja adicionar: ")
        telefone_contato = input("\nDigite o telefone do contato que deseja adicionar: ")
        adicionar_contato(contatos, nome_contato, telefone_contato)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("\nDigite o número do contato que deseja atualizar: ")
        escolha_alteracao = input("Deseja atualizar o nome ou o telefone?\n1. O nome\n2. O telefone\n3. Ambos\nDigite sua escolha: ")
        if escolha_alteracao == "1":
            novo_nome = input("\nDigite o novo nome do contato: ")
            atualizar_nome_contato(contatos, indice_contato, novo_nome)
        if escolha_alteracao == "2":
            novo_telefone = input("\nDigite o novo telefone do contato: ")
            atualizar_telefone_contato(contatos, indice_contato, novo_telefone)
        if escolha_alteracao == "3":
            novo_nome = input("\nDigite o novo nome do contato: ")
            atualizar_nome_contato(contatos, indice_contato, novo_nome)
            novo_telefone = input("\nDigite o novo telefone do contato: ")
            atualizar_telefone_contato(contatos, indice_contato, novo_telefone)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("\nDigite o número do contato que deseja marcar ou desmarcar como favorito: ")
        marcar_favorito(contatos, indice_contato)

    elif escolha == "5":
        ver_lista_favoritos(contatos)

    elif escolha == "6":
        ver_contatos(contatos)
        deletar_contato(contatos)

    elif escolha == "7":
        break