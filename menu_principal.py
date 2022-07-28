'''Menu principal com submenus '''



opcaop = input('Digite o numero do menu que deseja acessar. \n 1 - Cadastros \n 2 - Financeiro')

if opcaop =="1":
    import menu_cadastro


elif opcaop == "2":
    import menu_financeiro


else:
    print('Opção inválida! \nDigite uma opção válida.\n')
