import datetime
import pandas as pd
import numpy as np
import mysql.connector
from mysql.connector import Error
from datetime import datetime


con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')


criar_membros = """CREATE TABLE `templarios`.`membros` (
  `idmembro` INT NOT NULL AUTO_INCREMENT,
  `nomemembro` VARCHAR(45) NOT NULL,
  `telmembro` VARCHAR(45) NULL DEFAULT NULL,
  `enderecomembro` VARCHAR(45) NULL DEFAULT NULL,
  `nascimentomembro` VARCHAR(45) NULL DEFAULT NULL,
  `candidaturamembro` VARCHAR(45) NULL DEFAULT NULL,
  `emergenciamembro` VARCHAR(45) NULL DEFAULT NULL,
  `sanguemembro` VARCHAR(45) NULL DEFAULT NULL,
  `ativomembro` VARCHAR(45) NULL DEFAULT '1',
  `data_cadastro` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idmembro`));

		"""

criar_pagar = """CREATE TABLE `templarios`.`pagar` (
  `idpagar` INT NOT NULL AUTO_INCREMENT,
  `data_movimento` VARCHAR(45) NOT NULL,
  `historico` VARCHAR(45) NOT NULL,
  `data_lancamento` VARCHAR(45) NULL DEFAULT NULL,
  `valor` DECIMAL(10,2) NOT NULL,
  `saldo` DECIMAL(10,2) NULL DEFAULT '0.00',
  `debito_credito` VARCHAR(45) NULL DEFAULT 'D',
  PRIMARY KEY (`idpagar`));
"""

criar_receber ="""CREATE TABLE `templarios`.`receber` (
  `idreceber` INT NOT NULL AUTO_INCREMENT,
  `data_movimento` VARCHAR(45) NOT NULL,
  `historico` VARCHAR(45) NOT NULL,
  `data_lancamento` VARCHAR(45) NULL DEFAULT NULL,
  `valor` DECIMAL(10,2) NOT NULL,
  `saldo` DECIMAL(10,2) NULL DEFAULT '0.00',
  `debito_credito` VARCHAR(45) NULL DEFAULT 'C',
  PRIMARY KEY (`idreceber`));
"""
criar_saldos = """CREATE TABLE `templarios`.`saldos` (
  `idsaldos` INT NOT NULL AUTO_INCREMENT,
  `valor_saldo_receber` DECIMAL(10,2) NULL DEFAULT NULL,
  `valor_saldo_pagar` DECIMAL(10,2) NULL DEFAULT NULL,
  `valor_saldo_total` DECIMAL(10,2) NULL DEFAULT NULL,
  PRIMARY KEY (`idsaldos`));
"""

cursor = con.cursor()
cursor.execute(criar_membros)
print ("Tabela Membros criada com sucesso!")
cursor.execute(criar_pagar)
print ("Tabela Pagar criada com sucesso!")
cursor.execute(criar_receber)
print ("Tabela Receber criada com sucesso!")
cursor.execute(criar_saldos)
print ("Tabela Saldos criada com sucesso!")
con.commit()

print('Tabelas criadas com sucesso !')
cursor.close()
import menu_principal