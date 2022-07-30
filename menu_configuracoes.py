opcao = (int(input("Digite a opção desejada\n"
              "1 - Criar as tabelas padrão do sistema.\n"
              "2 - Para testar conexão com o banco de dados. ")))


if opcao == 1:
    print()
    import cria_tabelas
    print()

elif opcao == 2:
    print()
    import teste_conexao
    print()

else:
    print('\nVocê digitou uma opção incorreta !\n ')

import menu_principal