#JOGO DA FORCA

secreto = 'paraquedas'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('ahh, só é permitido uma letra por vez!')
        continue

    if letra in digitadas:
        print('Você já digitou essa letra!\n')
        digitadas.pop()
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'ISSO! A letra "{letra}" exista na palavra secreta!')
    else:
        print(f'POXA! A letra " {letra}" não existe na palavra secreta!')
        digitadas.pop()

    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU! Apalavra era {secreto_temporario}.')
        break
    else:
        print(f'A paralvra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()

    print(digitadas)