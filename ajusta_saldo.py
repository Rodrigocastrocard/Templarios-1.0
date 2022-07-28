import datetime
import mysql.connector
from mysql.connector import Error

print('Menu em desenvolvimento, faça o ajuste no menu RECEBIMENTO ou PAGAMENTO')
'''
try:
	con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')
	novo_saldo = input('Digite o novo valor de saldo. ')
	data_movimento = input('Digite a data do movimento. ')
	creddeb = '***'
	valor = '0'
	historico = 'Ajuste de saldo'

	inserir = """INSERT INTO movim_financeiro
							( data_movimento, creddeb_fin, historico_fin, valor_fin, saldo_fin) 
							values (%s, %s, %s, %s, %s);						
							"""
	sql_data = (data_movimento, creddeb, historico, valor, novo_saldo)


	cursor = con.cursor()
	cursor.execute(inserir,sql_data)
	con.commit()
	print(cursor.rowcount, 'Saldo Ajustado com sucesso ! .\n')
	cursor.close()


except Error as erro:
	print('Erro {}'.format(erro))
finally:
	if (con.is_connected()):
		cursor.close()
		con.close()
		print('conexão finalizada')
	else:
		print('Error ao fechar conexão')
'''