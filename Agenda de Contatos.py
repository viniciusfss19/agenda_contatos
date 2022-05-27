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
    elif opcao== "3":
        deletarcontato()
    else:
        buscarcontato() 


def cadastrarcontato():
    return print(f'CADASTRE O CONTATO')

def listarcontato():
    print(f'LISTAR CONTATO')

def deletarcontato():
    prit(f'DELETAR O CONTATO')

def buscarcontato():
    print(f'BUSCAR CONTATO')

def main():
    menu()
main()