
import db

MENU_INICIAL = 99

def exibir_cabecalho():
    """ imprimi o cabeçalho no terminal utilizando o tamanho maximo de 60 caracteres """
    QTD_COLUNAS = 60
    print ("-" * QTD_COLUNAS)
    print ("{:^60}".format("VAGAS"))
    print ("-" * QTD_COLUNAS)
    print ("{:^60}".format("tecle 99 volta para o menu inicial, [CTRL+C] sai"))
    print ("-" * QTD_COLUNAS)

def exibir_vagas():    
    """ exibe a lista de tarefas cadastradas, com algumas formatações básicas """
    for tarefa in db.getvaga():
        # check = \u2713 é o caracter unicode que representa o concluido
        check = u'\u2713' if vaga[2] == 1 else ""
        """
            os parametros passados para esse format() são o seguinte
            {:>4}  = 4 posições, alinhado a direita
            {:<47} = 47 posições, alinhado a esquerda
            {:^3}  = 3 posições, centralizado
        """
        t = "- [{:>4}] {:<47} {:^3}".format(tarefa[0], tarefa[1], check)
        print (t)
    print ("-" * 60)

def mostrar_opcao_nova_vaga():
    texto_nova_vaga = input("Descreva a vaga => ")
    print ("adicionando tarefa -> " + str(texto_nova_vaga))
    if texto_nova_vaga != str(MENU_INICIAL):
        db.adicionarvaga(texto_nova_vaga)    

def mostrar_opcao_concluir_vaga():
    cd_vaga = int(input("Qual vaga quer concluir? digite o código => "))
    print ("Concluindo vaga vaga -> " + str(cd_vaga))
    if cd_vaga != MENU_INICIAL:
        db.atualizarvaga(cd_vaga)
