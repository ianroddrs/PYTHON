valor = float(input('Qual o valor do pedido? '))
estado = str(input('Qua o Estado?'))

imposto = 0.055 * valor

if estado == 'PA':
    valor_total = valor + imposto
    print(f'O subtotal é de R${valor:.2f}.')
    print(f'O imposto é de R${imposto:.2f}.')
    print(f'O total é de R${valor_total:.2f}.')
else:
    print(f'O total é de R${valor:.2f}.')

