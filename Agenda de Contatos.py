def menu():
    opcao=input('''
    ===============================================================
                            AGENDA DE CONTATO 
    ===============================================================        
            MENU:
    [1] CADASTRAR CONTATOS
    [2] LISTAR CONTATOS
    [3] DELETAR CONTATO
    [4] BUSCAR CONTATO PELO ID
    ===============================================================    
    ESCOLHA UMA DAS OPÇÕES A CIMA:
    ''')


    if opcao == "1":
        cadastrarcontato()
    elif opcao=="2":
        listarcontato()
    elif opcao == "3":
        deletarcontato()
    else:
        buscarcontato() 


def cadastrarcontato():
     nome= str(input('Nome do contato'))
     idcontato= int(input('Adicione um codigo ID para o contato'))
     telefone=input('Número de Telefone')
     endereco=input('Endereço')
     numeroresidencia=input("Digite o número da residência")
     email=input('E-mail')
     try:
        agenda = open("agenda.txt","a")
        dados = f'{nome};{idcontato};{telefone};{endereco};{numeroresidencia};{email}\n'
        agenda.write(dados)
        agenda.close()
        print('Contato Salvo com Sucesso :)')
     except:
         print('Erro na Gravação do contato')

def listarcontato():
    print(f'LISTAR CONTATO')

def deletarcontato():
    print(f'DELETAR O CONTATO')

def buscarcontato():
    print(f'BUSCAR CONTATO')

def main():
    menu()
main()