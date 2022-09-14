#Dupla:
#Denys Leonardo Oliveira de Sales /email: dlos@etepd.com
#Luana Vitória Ribeiro Bernatrdo /email.: lvrb@etepd.com
import db
import mensagens as msg

def main():
    NOVA_VAGA     = 1
    CONCLUIR_VAGA = 2
    
    while True:
        msg.exibir_cabecalho()
        msg.exibir_vagas()
        try:
            # exibe as opções disponíveis
            opcao = int(input("O que deseja fazer? 1 = Nova vaga, 2 = Atualizar vaga => "))

            # verifica qual opção o usuário escolheu
            if opcao == NOVA_VAGA:
                msg.mostrar_opcao_nova_vaga()
            elif opcao == CONCLUIR_VAGA:
                msg.mostrar_opcao_concluir_vaga()
            else:
                print ("Opção não reconhecida, por favor informar um número")    
        except ValueError as e :
            print ("Opção não reconhecida, por favor informar um número")
        except Exception:
            exit(0)

if __name__ == "__main__":
    db.criarTabela()

    main()
