import mysql.connector
from mysql.connector import Error

try:
	con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')


	id_alterar = int(input('Digite o codigo do membro a ser alterado.'))

	seleciona = "SELECT idmembro FROM membros WHERE idmembro ='{}'".format(id_alterar)

	cursor = con.cursor()
	cursor.execute(seleciona)
	linhas = cursor.fetchall()

	if len(linhas) != 0:  # Verifica se o retorno contém alguma linha

		nomemembro = input('Digite o nome. ')
		telmembro = input('Digite o número do Telefone Celular: ')
		try:
			if len(telmembro) != 11:
				raise ValueError
			else:
				telmembro = int(telmembro)  # se contiver letras causa um ValueError
				telmembro = str(telmembro)
				celular = telmembro
				telFormatado = '({}) {}-{}-{}'.format(celular[0:2],
												  celular[2], celular[3:7], celular[7:])
				print(telFormatado)

		except ValueError:
			if len(telmembro) == 0:
				print('Você não digitou o número')
			else:
				print('Número inválido, o número precisa ter 11 números inteiros')

		enderecomembro = input('Digite o endereço. ')
		nascimentomembro = input('Digite a data de nascimento. ')
		try:
			if len(nascimentomembro) != 8:
				raise ValueError
			else:
				nascimentomembro = str(nascimentomembro)
				datanascimento = nascimentomembro
				data_formatada = '{}/{}/{}'.format(datanascimento[0:2],
											   datanascimento[2:4], datanascimento[4:])
				print(data_formatada)

		except ValueError:
			if len(nascimentomembro) == 0:
				print('Você não digitou a data')
			else:
				print('A data está incorreta, ela deve ter 8 digitos')

		candidaturamembro = input('Digite a data de candidatura. ')
		try:
			if len(candidaturamembro) != 8:
				raise ValueError
			else:
				candidaturamembro = str(candidaturamembro)
				datacandidatura = candidaturamembro
				data_formatadacand = '{}/{}/{}'.format(datacandidatura[0:2],
												   datacandidatura[2:4], datacandidatura[4:])
				print(data_formatadacand)

		except ValueError:
			if len(datacandidatura) == 0:
				print('Você não digitou a data')
			else:
				print('A data está incorreta, ela deve ter 8 digitos')

		emergenciamembro = input('Digite o telefone para emergencias. ')
		try:
			if len(emergenciamembro) != 11:
				raise ValueError
			else:
				emergenciamembro = int(emergenciamembro)  # se contiver letras causa um ValueError
				emergenciamembro = str(emergenciamembro)
				celularemer = emergenciamembro
				telemerFormatado = '({}) {}-{}-{}'.format(celularemer[0:2],
													  celularemer[2], celularemer[3:7], celularemer[7:])
				print(telemerFormatado)

		except ValueError:
			if len(emergenciamembro) == 0:
				print('Você não digitou o número')
			else:
				print('Número inválido, o número precisa ter 11 números inteiros')

		sanguemembro = input('Digite o tipo sanguineo. ')

		alterar = """ update membros set  nomemembro = (%s), telmembro = (%s), enderecomembro = (%s), nascimentomembro = (%s), candidaturamembro = (%s), emergenciamembro = (%s), sanguemembro = (%s)
			where idmembro = (%s)"""
		sql_data = nomemembro, telemerFormatado, enderecomembro, data_formatada, data_formatadacand, telemerFormatado, sanguemembro, id_alterar



		cursor = con.cursor()
		cursor.execute(alterar,sql_data)
		con.commit()
		print(cursor.rowcount, 'Registro inserido com sucesso.')
		cursor.close()
	else:
		print('Id não existe ! ')



except Error as erro:
	print('Erro {}'.format(erro))
finally:
	if (con.is_connected()):
		cursor.close()
		con.close()
		print('conexão finalizada')



import menu_cadastro
