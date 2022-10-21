print('Digite C para converter de Fahrenheit para Celsius.\nDigite F para converter de Celsius para Fahrenheit.')
operacao = str(input('Sua escolha: '))

if operacao == 'C':
    tempF = input('Por favor, insira a temperatura em Fahrenheit:')
    if tempF.isnumeric():
        tempC = (int(tempF) - 32) * 5 / 9
        print(f'A temperatura em Celcius é: {tempC}')
    else:
        print('Digite apenas números')
elif operacao == 'F':
    tempC = input('Por favor, insira a temperatura em Celcius:')
    if tempC.isnumeric():
        tempF = (int(tempC) * 9 / 5) + 32
        print(f'A temperatura em Fahrenheit é: {tempF}')
    else:
        print('Digite apenas números')