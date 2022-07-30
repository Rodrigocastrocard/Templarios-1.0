import datetime
import pandas as pd
import numpy as np
import mysql.connector
from mysql.connector import Error
from datetime import datetime


con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')
#cria recebimento
data_movimento = input('Digite a data do movimento. ')
try:
	if len(data_movimento) != 8:
		raise ValueError
	else:
		data_formatada = '{}/{}/{}'.format(data_movimento[0:2],
												   data_movimento[2:4], data_movimento[4:])
		print(data_formatada)

except ValueError:
	if len(data_movimento) == 0:
		print('Você não digitou a data')
	else:
		print('A data está incorreta, ela deve ter 8 digitos')

historico = input('Digite o histórico do movimento')
valor = float(input('Digite o valor da movimentação. '))
data_lancamento = datetime.today().strftime('%d-%m-%y')
inserir = """INSERT INTO receber
					( data_movimento, historico, valor, data_lancamento) 
					values (%s, %s, %s, %s);						
					"""
sql_data = (data_formatada, historico, valor, data_lancamento)
cursor = con.cursor()
cursor.execute(inserir,sql_data)
con.commit()

#soma recebimento e atualiza saldo parcial de recebimentos
consulta_sql = "SELECT SUM(valor) FROM receber "
cursor = con.cursor()
cursor.execute(consulta_sql)
linhas = cursor.fetchall()
valor = (linhas[0])
for valor in linhas:
    saldo = valor[0]
    valor2 = float(saldo)
valor3 = [valor2]
alterar = """ UPDATE `templarios`.`saldos` SET `valor_saldo_receber` = (%s); """
sql_data = (valor3)
cursor.execute(alterar, sql_data)
con.commit()


#atualiza saldo total
consulta_sql = "SELECT * FROM saldos "
cursor = con.cursor()
cursor.execute(consulta_sql)
linhas = cursor.fetchall()
for valor_saldo in linhas:
    saldo_receber = (valor_saldo[1])
    saldo_receber2 = float(saldo_receber)
    saldo_pagar = (valor_saldo[2])
    saldo_pagar2 = float(saldo_pagar)
saldo_total = [saldo_receber2-saldo_pagar2]

print (saldo_total)


atualizar_saldo = """ UPDATE `templarios`.`saldos` SET `valor_saldo_total` = (%s); """
sql_data = (saldo_total)
cursor.execute(atualizar_saldo, sql_data)
con.commit()

print(cursor.rowcount, 'Registro inserido com sucesso.\n')
cursor.close()











