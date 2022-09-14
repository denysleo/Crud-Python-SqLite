#Dupla:
#Denys Leonardo Oliveira de Sales /email: dlos@etepd.com
#Luana Vitória Ribeiro Bernatrdo /email.: lvrb@etepd.com
class oportunidade_emprego:
  def __init__(self, titulo, salario, data_criacao, nome_empresa, cargo, descricao, status):
    self.titulo = titulo
    self.salario = salario
    self.data_criacao = data_criacao
    self.nome_empresa = nome_empresa
    self.cargo= cargo
    self.descricao=descricao
    self.status=status

if __name__ == '__main__':
  oportunidade1 = oportunidade_emprego("desenvolvedor", 2000, 13,"control","empregado","front-end","aberta")

import sqlite3

conn = sqlite3.connect("banco.db")

def criarTabela():
  cursor = conn.cursor()
  conn.execute("""
  create table if not exists vaga
    cd_vaga integer primary key autoincrement,
    vaga text
    atualizado integer
  """)

def adicionarvaga(vaga):
  conn.execute("insert into vaga(vaga, atualizado) values (?, 0)", (vaga))
  conn.commit()

def removervaga(cd_vaga):
  conn.execute("delete from vaga where cd_vaga = ?", (cd_vaga))
  conn.commit()

def atualizarvaga(cd_vaga):
  conn.execute("uptade vaga set atualizado = 1 where cd+vaga = ?", (cd_vaga))
  conn.commit()

def getvaga():
  return conn.execute("select cd_vaga, vaga, atualizado from vaga")

