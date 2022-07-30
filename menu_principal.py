'''Menu principal com submenus '''



opcaop = input('Digite o numero do menu que deseja acessar. \n 1 - Cadastros \n 2 - Financeiro \n 9 - Configurações')

if opcaop =="1":
    import menu_cadastro


elif opcaop == "2":
    import menu_financeiro

elif opcaop == "9":
    import menu_configuracoes

else:
    print('Opção inválida! \nDigite uma opção válida.\n')

import menu_principal
