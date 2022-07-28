import mysql.connector
from mysql.connector import Error




try:
	con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')

	consulta_sql = "select * from membros "


	cursor = con.cursor()
	cursor.execute(consulta_sql)
	linhas = cursor.fetchall()
	print ('Numero total de membros cadastrados', cursor.rowcount)
	print ('\nMostrando os membros cadastrados')
	for linha in linhas:
		print ( 'Código:' ,linha[0])
		print ('Nome:' , linha[1])
		print ('Telefone:' , linha[2])
		print ('Endereço:' , linha[3])
		print ('Data de nascimento:' , linha[4])
		print ('Data da candidatura:' , linha[5])
		print ('Telefone para emergencias' , linha[6])
		print ('Tipo sanguineo:' , linha[7])
		print ('Ativo:' , linha[8])
		print ()
except Error as e:
	print ('Erro ao acessar a tabela' ,e)

finally:
	if (con.is_connected()):
		cursor.close()
		con.close()
		print('conexão finalizada')

import menu_cadastro