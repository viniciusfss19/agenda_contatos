def menu():
    opcao=input('''
    ===============================================================
                            AGENDA DE CONTATO 
    ===============================================================        
                                    MENU:
    [1] CADASTRAR CONTATOS
    [2] LISTAR CONTATOS
    [3] DELETAR CONTATO
    [4] BUSCAR CONTATO PELO INOME
    [5] SAIR
    ===============================================================    
    ESCOLHA UMA DAS OPÇÕES A CIMA:
    ''')


    if opcao == "1":
        cadastrarcontato()
    elif opcao=="2":
        listarcontato()
    elif opcao == "3":
        deletarcontato()
    elif opcao == "4":
        buscarcontato()
    else:
        sair()


def cadastrarcontato():
     nome_contato = str(input('Nome do contato'))
     idcontato = int(input('Adicione um codigo ID para o contato'))
     telefone =input('Número de Telefone')
     endereco =input('Endereço')
     numeroresidencia=input("Digite o número da residência")
     email=input('E-mail')
     try:
        agenda = open("agenda.txt","a") #'a' é para disponibilizar a agenda para edição#
        dados = f'{nome_contato};{idcontato};{telefone};{endereco};{numeroresidencia};{email}\n'
        agenda.write(dados)
        agenda.close()
        print('Contato Salvo com Sucesso :)')
     except:
         print('Erro na Gravação do contato')

def listarcontato():
    agenda = open('agenda.txt','r') #'r' é para disponibilizar a agenda para leitura#
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarcontato():
    print(f'DELETAR O CONTATO')

def buscarcontato():
    nome = input('Digite o nome do contato: ')
    nome = nome.upper().strip()
    agenda = open('agenda.txt', 'r')  # 'r' é para disponibilizar a agenda para leitura#

    for contato in agenda:
        if nome in contato.split(":")[0]:
          print(contato)
        else:
            print('contato inexistente')


    agenda.close()

def sair():
    print(f'ATÉ MAIS')
    exit()


def main():
    menu()
main()