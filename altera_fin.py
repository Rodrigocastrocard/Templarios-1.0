import mysql.connector
from mysql.connector import Error


#conexão
con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')
qual_tabela = int(input('Digite qual tabela você deseja alterar \n 1-Recebimento \n 2-Pagamento\n'))

#se recebimento
	#incluir
if qual_tabela == 1:
	id_alterar = int(input('Digite o codigo do movimento a ser alterado.'))
	data_movimento = input('Digite a data do movimento. ')
	historico = input('Digite o histórico do movimento')
	valor = float(input('Digite o valor da movimentação. '))

	alterar = """ update receber set  data_movimento = (%s), historico = (%s), valor = (%s) 
			where idreceber = (%s)"""
	sql_data = data_movimento, historico, valor, id_alterar

	cursor = con.cursor()
	cursor.execute(alterar,sql_data)
	con.commit()
	print(cursor.rowcount, 'Registro inserido com sucesso.')
	cursor.close()

	#Somar e atualizar na tabela saldo de recebimento
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

	#Atualiza saldo total
	consulta_sql = "SELECT * FROM saldos "
	cursor = con.cursor()
	cursor.execute(consulta_sql)
	linhas = cursor.fetchall()
	for valor_saldo in linhas:
		saldo_receber = (valor_saldo[1])
		saldo_receber2 = float(saldo_receber)
		saldo_pagar = (valor_saldo[2])
		saldo_pagar2 = float(saldo_pagar)
	saldo_total = [saldo_receber2 - saldo_pagar2]

	print(saldo_total)

	atualizar_saldo = """ UPDATE `templarios`.`saldos` SET `valor_saldo_total` = (%s); """
	sql_data = (saldo_total)
	cursor.execute(atualizar_saldo, sql_data)
	con.commit()

#se pagamento
	#incluir
elif qual_tabela == 2:
	id_alterar = int(input('Digite o codigo do movimento a ser alterado.'))
	data_movimento = input('Digite a data do movimento. ')
	historico = input('Digite o histórico do movimento')
	valor = float(input('Digite o valor da movimentação. '))

	alterar = """ update pagar set  data_movimento = (%s), historico = (%s), valor = (%s) 
			where idpagar = (%s)"""
	sql_data = data_movimento, historico, valor, id_alterar

	cursor = con.cursor()
	cursor.execute(alterar,sql_data)
	con.commit()
	print(cursor.rowcount, 'Registro inserido com sucesso.')
	cursor.close()

	#somar e atualizar saldo parcial de pagamentos
	consulta_sql = "SELECT SUM(valor) FROM pagar "
	cursor = con.cursor()
	cursor.execute(consulta_sql)
	linhas = cursor.fetchall()
	valor = (linhas[0])
	for valor in linhas:
		saldo = valor[0]
		valor2 = float(saldo)
	valor3 = [valor2]
	alterar = """ UPDATE `templarios`.`saldos` SET `valor_saldo_pagar` = (%s); """
	sql_data = (valor3)
	cursor.execute(alterar, sql_data)
	con.commit()

	#Atualizar saldo total
	consulta_sql = "SELECT * FROM saldos "
	cursor = con.cursor()
	cursor.execute(consulta_sql)
	linhas = cursor.fetchall()
	for valor_saldo in linhas:
		saldo_receber = (valor_saldo[1])
		saldo_receber2 = float(saldo_receber)
		saldo_pagar = (valor_saldo[2])
		saldo_pagar2 = float(saldo_pagar)
	saldo_total = [saldo_receber2 - saldo_pagar2]

	print(saldo_total)

	atualizar_saldo = """ UPDATE `templarios`.`saldos` SET `valor_saldo_total` = (%s); """
	sql_data = (saldo_total)
	cursor.execute(atualizar_saldo, sql_data)
	con.commit()



else:
	print('Opção incorreta.\n')


import menu_financeiro