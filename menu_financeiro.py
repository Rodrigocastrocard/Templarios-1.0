

opcaocad = input('Digite o numero do modulo que deseja utilizar. \n 1 - Recebimentos \n 2 - Pagamentos \n 3 - Ajuste de saldo \n 4 - Relatorio \n 5 - Alterar lançamento \n 0 - Inicio')
if opcaocad == '1':
    import recebimento

elif opcaocad == '2':
    import pagamentos

elif opcaocad == '3':
    import ajusta_saldo

elif opcaocad == '4':
    import relatorio_fin

elif opcaocad == '5':
    import altera_fin

elif opcaocad == '0':
    import menu_principal


else:
    print('Digite uma opção válida!\n')
