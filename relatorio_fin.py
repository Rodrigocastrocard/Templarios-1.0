import mysql.connector
from mysql.connector import Error





con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')

tipo_relatorio = int(input('Qual relatorio você deseja ver ? \n 1-Recebimentos\n 2-Pagamento\n 3-Saldo\n'))

if tipo_relatorio == 1:
	consulta_sql = "select * from receber "
	cursor = con.cursor()
	cursor.execute(consulta_sql)
	linhas = cursor.fetchall()
	print('Numero total de registros', cursor.rowcount)
	print('\nMostrando os lançamentos realizados')
	print()
	for linha in linhas:
		print('Codigo do Movimento:', linha[0])
		print('Data do Movimento:', linha[1])
		print('Historico:', linha[2])
		print('Data do Lancamento:', linha[3])
		print('Valor:', linha[4])
		print('Saldo:', linha[5])
		print('Debito ou Credito:', linha[6])
		print()

elif tipo_relatorio == 2:
	consulta_sql = "select * from pagar "
	cursor = con.cursor()
	cursor.execute(consulta_sql)
	linhas = cursor.fetchall()
	print('Numero total de registros', cursor.rowcount)
	print('\nMostrando os lançamentos realizados')
	print()
	for linha in linhas:
		print('Codigo do Movimento:', linha[0])
		print('Data do Movimento:', linha[1])
		print('Historico:', linha[2])
		print('Data do Lancamento:', linha[3])
		print('Valor:', linha[4])
		print('Saldo:', linha[5])
		print('Debito ou Credito:', linha[6])
		print()

elif tipo_relatorio == 3:
	consulta_sql = "select * from saldos "
	cursor = con.cursor()
	cursor.execute(consulta_sql)
	linhas = cursor.fetchall()
	print()
	for linha in linhas:
		print('Total de recebimentos:', linha[1])
		print('Data de pagamentos:', linha[2])
		print('Saldo total:', linha[3])
		print()

else:
	print('Opção incorreta"')

