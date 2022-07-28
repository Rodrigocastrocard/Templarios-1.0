'''Menu com opções e importação de modulos para cadastro, alteração ou desativação'''


opcaocad = input('Digite o numero do modulo que deseja utilizar. \n 1 - Cadastrar \n 2 - Alteração \n 3 - Desativação \n 4 - Relatorio \n 0 - Inicio')
if opcaocad == '1':
        import cadastra_membro

elif opcaocad == '2':
       import altera_membro

elif opcaocad == '3':
       import desativa_membro

elif opcaocad == '4':
        import relmembro

elif opcaocad == '0':
        import menu_principal


else:
        print('Digite uma opção válida!\n')


