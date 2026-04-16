def dividir():
    # ENTRADA
    try:
        a = int(input('primero valor: '))
        b = int(input('segundo valor: '))

        # PROCESSAMENTO
        divisao = a / b
    except ZeroDivisionError:
        print('Erro: não é possível dividir pro zero.')
    except TypeError:
        print('Erro: os valores precisam ser números.')
    else:
        # SAÍDA
        print(f'Resultado: {divisao}')

dividir()
