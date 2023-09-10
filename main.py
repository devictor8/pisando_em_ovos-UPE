espaços = [1, 2, 3, 4, 5]
config = {'armador_pont': 0, 'andarilho_pont': 0}
matriz = []

print('=-' * 20)
print('{:^40}'.format('PISANDO EM OVOS'))
print('=-' * 20)


def fazer_matriz():
    global matriz
    matriz.clear()
    for linha in range(5):
        matriz.append([])
        for coluna in range(5):
            matriz[linha].append('A')


def placar():
    global config
    print('Placar atual: ')
    print(f'A pontuação do jogador {config["armador"]}: {config["armador_pont"]}')
    print(f'A pontuação do jogador {config["andarilho"]}: {config["andarilho_pont"]}')


def valor_espaco(col_res):
    global espaços
    espaços.clear()
    if col_res > 1:
        espaços.append(col_res - 1)
    espaços.append(col_res)
    if col_res < 5:
        espaços.append(col_res + 1)
    

def caminhar_mapa():
    global matriz
    global config
    global espaços
    linha = 0
    espaços = [1, 2, 3, 4, 5]
    while True:
        print(espaços)
        coluna_mapa = validacao('Escolha sabiamente um dos espaços válidos: ', espaços)
        if matriz[linha][coluna_mapa-1] == 'A' and linha < 4:
            print(f'Você deu sorte, agora escolha um dos espaços validos da linha {linha+2} a seguir')
            valor_espaco(coluna_mapa)
        elif matriz[linha][coluna_mapa-1] == 'O':
            print('Eca! Você pisou em um ovo podre e perdeu')
            config['armador_pont'] += 1
            break
        linha += 1
        if linha == 5:
            print('Você atravessou o terreno sem cair em nenhuma armadilha! Parabéns!!!!')
            config['andarilho_pont'] += 1
            break


def carregamento():
    for c in range(100):
        if c == 0:
            print()
        else:
            print('='*c)


def validacao(txt, valores_permitidos):
    res = input(f'{txt}')
    while res not in valores_permitidos or res in '':
        res = input(f'Tente novamente. {txt}')

    return int(res)


def armador():
    global config
    while True:
        jogador_armador = validacao('Qual jogador plantará as armadilhas? [1 ou 2] ', ['1', '2'])
        if jogador_armador == 1:
            config['armador'] = 1
            config['andarilho'] = 2
            break
        elif jogador_armador == 2:
            config['armador'] = 2
            config['andarilho'] = 1
            break


def print_matriz():
    print(f'''
            0 1 2 3 4 5
            1 {matriz[0][0]} {matriz[0][1]} {matriz[0][2]} {matriz[0][3]} {matriz[0][4]} 
            2 {matriz[1][0]} {matriz[1][1]} {matriz[1][2]} {matriz[1][3]} {matriz[1][4]}
            3 {matriz[2][0]} {matriz[2][1]} {matriz[2][2]} {matriz[2][3]} {matriz[2][4]}
            4 {matriz[3][0]} {matriz[3][1]} {matriz[3][2]} {matriz[3][3]} {matriz[3][4]}
            5 {matriz[4][0]} {matriz[4][1]} {matriz[4][2]} {matriz[4][3]} {matriz[4][4]}
                        ''')


def plantar_armadilha(arm):
    global matriz
    global jogo_mapa
    fazer_matriz()
    print_matriz()

    print(f'Jogador {arm}, você pode esconder até 3 ovos podres por linha do terreno.')
    for linha in range(1, 6):
        for c in range(1, 4):
            coluna = validacao(f'Em qual coluna da linha {linha} você quer esconder ovos podres? [1 a 5] ',['1', '2', '3', '4', '5'])
            matriz[linha-1][coluna-1] = 'O'
            if c != 3:
                per = validacao('Quer continuar nessa linha? \n[1] - Sim \n[2] - Não\nresposta: ', ['1', '2'])
                if per == 2:
                    break
    print_matriz()
    redefinir = validacao('Você redefinir o campo? \n[1] - Sim \n[2] - Não\nresposta: ', ['1', '2'])
    if redefinir == 1:
        fazer_matriz()
        plantar_armadilha(arm)


while True:
    print('''
Opções:
    1 - Definir Armador
    2 - Plantar Armadilhas
    3 - Iniciar com Andarilho
    4 - Mostrar o placar
    0 - Finalizar o Jogo
    ''')
    opc = validacao('Qual opção você deseja escolher? ', ['1', '2', '3', '4', '0'])
    match opc:
        case 1:
            armador()
            print(f'O armador é o jogador: {config["armador"]}')
            print(f'O andarilho é o jogador: {config["andarilho"]}')
        case 2:
            if 'armador' and 'andarilho' in config:
                plantar_armadilha(config['armador'])
            else:
                print('Escolha quem será o armador na opção 1 do menu!')
        case 3:
            carregamento()
            caminhar_mapa()
        case 4:
            placar()
        case 0:
            print('Encerrando programa...')
            break
