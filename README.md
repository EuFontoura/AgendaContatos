# Gerenciador de Lista de Contatos

Este projeto foi desenvolvido como parte de um desafio da Rocketseat. Ele implementa um gerenciador de contatos simples que permite adicionar, visualizar, atualizar, marcar como favorito e excluir contatos. Além disso, os contatos favoritos podem ser visualizados separadamente.

## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Funcionalidades](#funcionalidades)
- [Exemplos](#exemplos)
- [Contribuidores](#contribuidores)
- [Licença](#licença)

## Instalação

Não há requisitos externos para rodar este projeto. Ele é escrito em Python puro e pode ser executado em qualquer ambiente com Python 3.x instalado.

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd nome-do-repositorio
    ```

3. Execute o script:

    ```bash
    python3 gerenciador_contatos.py
    ```

## Uso

Ao executar o script, o usuário será apresentado a um menu interativo com as seguintes opções:

1. **Adicionar Contato**: Adiciona um novo contato com nome e telefone à lista.
2. **Ver Agenda**: Exibe todos os contatos com seus respectivos nomes e telefones.
3. **Atualizar Contato**: Permite atualizar o nome, telefone ou ambos de um contato existente.
4. **Marcar/Desmarcar como Favorito**: Define ou remove um contato da lista de favoritos.
5. **Ver Lista de Favoritos**: Exibe todos os contatos marcados como favoritos.
6. **Deletar Contato**: Remove um contato da lista.
7. **Sair**: Encerra o programa.

## Funcionalidades

- **Adicionar Contato**: Insere um novo contato com nome e telefone.
- **Visualizar Contatos**: Lista todos os contatos com opção de ver quais são favoritos.
- **Atualizar Contatos**: Atualiza o nome ou telefone de um contato.
- **Marcar/Desmarcar Favorito**: Marca ou desmarca contatos como favoritos.
- **Ver Favoritos**: Lista apenas os contatos favoritos.
- **Deletar Contato**: Remove contatos da lista.

## Exemplos

### 1. Adicionar Contato
```bash
Digite o nome do contato que deseja adicionar: João
Digite o telefone do contato que deseja adicionar: 123456789
Telefone de João foi adicionado com sucesso!
```
### 2. Ver Contato
```bash
Lista de contatos:
1. João - Telefone: 123456789
```
### 3. Atualizar Contato
```bash
Digite o número do contato que deseja atualizar: 1
Deseja atualizar o nome ou o telefone?
1. O nome
2. O telefone
3. Ambos
Digite sua escolha: 1
Digite o novo nome do contato: João Silva
Contato 1 atualizado para João Silva
```
### 4. Marcar Contato como Favorito
```bash
Digite o número do contato que deseja marcar como favorito: 1
Contato 1 marcado como favorito.
```
### 5. Ver Lista de Favoritos
Se houver contatos marcados como favoritos, a lista será exibida com os respectivos nomes e telefones. Caso contrário, será informado que nenhum contato favorito foi encontrado.
```bash
Contatos Favoritos:
Nome: João Silva - Telefone: 123456789
```
Se não houver contatos favoritos, o programa exibirá:

```bash
Nenhum contato favorito encontrado.
```

### 6. Deletar Contato
Para deletar um contato, o usuário primeiro vê a lista de contatos e depois escolhe o número correspondente ao contato que deseja remover.
```bash
Lista de contatos:
1. João Silva - Telefone: 123456789

Digite o número do contato que deseja deletar: 1
Contato João Silva foi removido com sucesso!
```

Se a lista de contatos estiver vazia, o programa exibirá a seguinte mensagem:

```bash
A lista de contatos está vazia!
```
### 7. Sair do Programa
Para encerrar o programa, basta selecionar a opção "Sair" no menu:

```bash
Menu do Gerenciador de Lista de Contatos:
1. Adicionar Contato
2. Ver Agenda
3. Atualizar Contato
4. Marcar ou desmarcar como Favorito
5. Ver lista de Favoritos
6. Deletar Contato
7. Sair

Digite a sua escolha: 7
```

O programa será encerrado sem exibir mensagens adicionais.

## Contribuidores

Este projeto foi desenvolvido por Gabriel Fontoura.

## Licença

Este projeto não possui uma licença específica.