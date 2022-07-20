while True:
    try:
        nome = input('Digite seu nome: ')
        print(f'Olá {nome}! =)')
        
        bad_div = input('Dividir por zero? [s, n] ')
        if bad_div == 's':
            0/0
    except KeyboardInterrupt: # Exceção causada por um Ctrl + c
        print('\nAté mais.')
        exit()
    except ZeroDivisionError:
        print('Não é possível dividir por zero.')
    else: # Só é execultado se não houver nenhuma exceção
        print('Tudo funcionou sem erros.')
    finally: # Sempre execulta
        print('Fim do loop.')
