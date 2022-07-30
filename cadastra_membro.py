import datetime
import mysql.connector
from mysql.connector import Error
from datetime import datetime

con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')



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
		data_formatada = '{}/{}/{}'.format(nascimentomembro[0:2],
												   nascimentomembro[2:4], nascimentomembro[4:])
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
		data_formatadacand = '{}/{}/{}'.format(candidaturamembro[0:2],
												   candidaturamembro[2:4], candidaturamembro[4:])
		print(data_formatadacand)

except ValueError:
	if len(candidaturamembro) == 0:
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
data_cadastro = datetime.today().strftime('%d-%m-%y')

inserir = """INSERT INTO membros
						( nomemembro, telmembro, enderecomembro, nascimentomembro, candidaturamembro, emergenciamembro, sanguemembro, data_cadastro) 
						values (%s, %s, %s, %s, %s, %s, %s,%s);						
						"""
sql_data = (nomemembro, telFormatado, enderecomembro, data_formatada, data_formatadacand, telemerFormatado, sanguemembro, data_cadastro)

cursor = con.cursor()
cursor.execute(inserir,sql_data)
con.commit()
print(cursor.rowcount, 'Registro inserido com sucesso.\n')
cursor.close()


import menu_principal

