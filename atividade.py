import random
import time

print('Bem vindo ao jogo de Porto RPG Digital!')
time.sleep(1)
input('Pressione qualquer tecla para continuar... ').strip()
fase = 0

jogador = {
    'nome': input('Digite o seu nome jogador(a)!: ').lower(),
    'vida': 50,
    'ataque': 10,
    'defesa': 5,
    'energia': 3,
    'inventário': ['poção de vida', 
                   'poção de energia', 
                   'poção de defesa', 
                   'poção de ataque'],
}

status = {
    'vida': 50,
    'energia': 3
}

inimigos = [
    {'nome': "Slime",
     'vida': 30, 
     'ataque': 7, 
     'defesa': 0, 
     'drop': [
         'poção de vida', 
         'poção de vida',
         'poção de energia',
         'poção de energia',
         'nada']},

    {'nome': "Goblin",
     'vida': 50,
     'ataque': 15,
     'defesa': 5,
     'drop': [
         'poção de vida', 
         'poção de vida',
         'poção de vida',
         'poção de vida',
         'poção de energia',
         'poção de energia',
         'poção de ataque',
         'poção de ataque',
         'nada']},

    {'nome': "Orc",
     'vida': 80,
     'ataque': 25,
     'defesa': 10,
     'drop': [
         'poção de vida',
         'poção de vida',
         'poção de vida',
         'poção de energia',
         'poção de energia',
         'poção de ataque',
         'poção de ataque',
         'poção de defesa',
         'poção de defesa',
         'nada',
         'nada']},

    {'nome': "Dragão",
     'vida': 150,
     'ataque': 40,
     'defesa': 20,
     'drop': [
         'poção de vida',
         'poção de vida',
         'poção de vida',
         'poção de energia',
         'poção de energia',
         'poção de ataque',
         'poção de ataque',
         'poção de defesa',
         'poção de defesa']},

    {'nome': "😨Deus😨 (Desista, nem tente...)",
     'vida': 300,
     'ataque': 60,
     'defesa': 30,
     'drop': [
         'poção de vida',
         'poção de vida',
         'poção de vida',
         'poção de energia',
         'poção de energia',
         'poção de ataque',
         'poção de ataque',
         'poção de defesa',
         'poção de defesa']},
]

inimigo = inimigos[fase]

def mostrar_status(jogador):
    print(f'==========JOGADOR========== \nNome: {jogador["nome"]} \nVida: {jogador["vida"]} \nAtaque: {jogador["ataque"]} \nDefesa: {jogador["defesa"]} \nEnergia: {jogador["energia"]} \nInventário: \n-{"\n-".join(jogador["inventário"])}')
    time.sleep(1)

def mostrar_batalha(jogador, inimigo):
    print(f'==========BATALHA========== \n Jogador: \nNome: {jogador["nome"]} \nVida: {jogador["vida"]} \nAtaque: {jogador["ataque"]} \nDefesa: {jogador["defesa"]} \nEnergia: {jogador["energia"]} \n---------------\n Inimigo: \nNome: {inimigo["nome"]} \nVida: {inimigo["vida"]} \nDefesa: {inimigo['defesa']} \n==================')

def mostrar_inimigo(inimigo):
    print(f'Você encontrou um {inimigo["nome"]}!')
    time.sleep(1)

def escolher_acao():
    acao = input('O que você deseja fazer? \n1 - Atacar \n2 - Usar item \n3 - Descansar \n4 - Fugir \nDigite aqui: ').lower()
    while acao not in ['1', '2', '3', '4', 'atacar', 'usar item', 'descansar', 'fugir']:
        acao = input('Opção inválida! \nO que você deseja fazer? \n1 - Atacar \n2 - Usar item \n3 - Descansar \n4 - Fugir \nDigite aqui: ').lower()
    return acao

def verificar_vida(jogador, inimigo):
    if jogador['vida'] <= 0:
        print('Você morreu! Game Over!')
        time.sleep(1)
        return False
    elif inimigo['vida'] <= 0:
        print(f'Você derrotou {inimigo["nome"]}!')
        return False
    return True

def calcular_dano(jogador, inimigo):
    dano_inimigo = inimigo['ataque'] - jogador['defesa']
    if dano_inimigo <= 0:
        dano_inimigo = inimigo['ataque'] // 2
    dano_jogador = jogador['ataque'] - inimigo['defesa']
    if dano_jogador <= 0:
        dano_jogador = jogador['ataque'] // 2
    return dano_inimigo, dano_jogador

dano_inimigo, dano_jogador = calcular_dano(jogador, inimigo)

def atacar(jogador, inimigo, dano_jogador):
    print('Você descide atacar!')
    time.sleep(1)
    inimigo['vida'] -= dano_jogador
    print(f'Você causou {dano_jogador} ao {inimigo["nome"]}!')
    time.sleep(1)
    jogador['energia'] -= 1

def ataque_inimigo(jogador, inimigo, dano_inimigo):
    print(f'O {inimigo["nome"]} descide atacar!')
    time.sleep(1)
    jogador['vida'] -= dano_inimigo
    print(f'Você recebeu {dano_inimigo} do {inimigo["nome"]}!')
    time.sleep(1)

def usar_item(jogador):
    if jogador['inventário']:
        for i in jogador['inventário']: 
            print(f'Você possui o item: {i}') 
        item_usado = input('Qual item você deseja usar? ').lower().strip()
        while item_usado not in jogador['inventário'] and item_usado not in ['voltar', 'cancelar', 'sair']: 
            print(f'Item {item_usado} não encontrado')
            item_usado = input('Qual item você deseja usar? ').lower().strip()
        if item_usado == 'poção de vida':
            print('Você usou uma poção de vida!')
            time.sleep(1)
            jogador['vida'] += 15
            print(f'Sua vida agora está em {jogador["vida"]}') 
        elif item_usado == 'poção de energia':
            print('Você usou uma poção de energia!')
            time.sleep(1)
            jogador['energia'] += 5
            print(f'Sua energia agora está em {jogador["energia"]}') 
        elif item_usado == 'poção de defesa':
            print('Você usou uma poção de defesa!')
            time.sleep(1) 
            jogador['defesa'] += 5
            print(f'Sua defesa agora está em {jogador["defesa"]}')
        elif item_usado == 'poção de ataque': 
            print('Você usou uma poção de ataque!')
            time.sleep(1)
            jogador['ataque'] += 5
            print(f'Seu ataque agora está em {jogador["ataque"]}')
        else:
            print(f'Você fechou sua mochila!')
            time.sleep(1)
            print('Mas acabou se distraindo...')
            time.sleep(1)
    else: 
        print('Você não tem nenhum item para usar!')
    time.sleep(1)

def descansar(jogador, dano_inimigo):
    print(f'Você está descansando...')
    jogador['vida'] -= dano_inimigo
    time.sleep(1)
    print(f'Opa! Você levou {dano_inimigo} de dano enquanto descansava... Isso deve ter doído um pouco')
    jogador['energia'] += 2
    time.sleep(1)
    print(f'Você recuperou 2 de energia! Energia atual: {jogador["energia"]}')
    time.sleep(1)

penalidade = dano_inimigo * 2

def fugir_batalha(jogador, penalidade):
    print(f'Você descidiu fugir...? \nQue covarde... 🙄')
    time.sleep(1)
    jogador['vida'] = jogador['vida'] - penalidade
    jogador['ataque'] = jogador['ataque'] - penalidade
    jogador['defesa'] = jogador['defesa'] - penalidade
    if jogador['energia'] > 1:
        jogador['energia'] -= 2
    print('Todos os seus status foram reduzidos, não fuja da próxima! >:(')
    time.sleep(2)
    

def verificar_energia(jogador):
    if jogador['energia'] <= 0:
        print('Você não tem energia suficiente para atacar!')
        return False
    else:
        return True

def escolher_drop(jogador,inimigo):
    drop = random.choice(inimigo['drop'])
    if drop != 'nada':
        jogador['inventário'].append(drop)
        print(f'Você encontrou um(a) {drop}!')
    else:
        print('O inimigo não deixou nada para você.')
    time.sleep(1)

def batalhar(jogador, inimigo, dano_jogador, dano_inimigo):
    while verificar_vida(jogador, inimigo):
        calcular_dano(jogador, inimigo)
        mostrar_batalha(jogador, inimigo)
        time.sleep(1)
        acao = escolher_acao()
        if acao == '1' or acao == 'atacar':
                energia = verificar_energia(jogador)
                if energia:
                    atacar(jogador, inimigo, dano_jogador)
        elif acao == '2' or acao == 'usar item':
            usar_item(jogador)
        elif acao == '3' or acao == 'descansar':
            descansar(jogador, dano_inimigo)
        else:
            fugir_batalha(jogador, dano_inimigo)
            break
        if inimigo['vida'] > 0 and acao not in ['3', 'descansar']:
            ataque_inimigo(jogador, inimigo, dano_inimigo)
    if inimigo['vida'] <= 0:
        return True
    else:
        return False

time.sleep(1)
print('Então vamos começar! Mas antes... Olhe os seus status:')
mostrar_status(jogador)
time.sleep(3)

print(f'{jogador["nome"]} estava andando pela floresta... Seguindo uma trilha de pedras desgastadas, quando algo chama sua atenção...')

while fase < len(inimigos):
    inimigo = inimigos[fase]
    time.sleep(2)
    mostrar_inimigo(inimigo)
    time.sleep(1)
    venceu = batalhar(jogador, inimigo, dano_jogador, dano_inimigo)
    if venceu:
        if fase >= 2:
            escolher_drop(jogador, inimigo)
            escolher_drop(jogador, inimigo)
        else:
            escolher_drop(jogador, inimigo)
        if fase < len(inimigos):
            print(f'Você consegue eliminar o {inimigo["nome"]} que está a sua frente!')
            time.sleep(2)
            jogador['energia'] = status['energia'] + 2
            jogador['vida'] = status['vida'] + 15
            jogador['ataque'] += penalidade
            jogador['defesa'] += penalidade
            print('Você recebeu um buff!')
            time.sleep(1)
            mostrar_status(jogador)
            time.sleep(2)
            print(f'Você continua sua jornada e encontra outro inimigo! \nPrepare-se para a próxima batalha!')
            fase += 1
        else:
            print('Parabéns! Você derrotou todos os inimigos e completou o jogo!')
    else:
        print('Você perdeu a batalha! Tente novamente!')
        break