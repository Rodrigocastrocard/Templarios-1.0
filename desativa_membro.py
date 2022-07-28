import mysql.connector
from mysql.connector import Error

try:
	con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')



	id_desativa = int(input('Digite o codigo do membro a ser alterado.'))


	alterar = """update membros set ativomembro = '0' where idmembro = (%s);"""
	sql_data = id_desativa

	cursor = con.cursor()
	cursor.execute(alterar,[sql_data])
	con.commit()
	print(cursor.rowcount, 'Membro desativado com sucesso.')
	cursor.close()



except Error as erro:
	print('Erro {}'.format(erro))
finally:
	if (con.is_connected()):
		cursor.close()
		con.close()
		print('conexão finalizada')

import menu_cadastro