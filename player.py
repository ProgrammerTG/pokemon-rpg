import random, pokemon, os, pickle
from time import sleep
jogador = {"Nome": "Nicolly", "Nivel": 0, "Dinheiro": 0, "Pokemons": []}
inimigos = ["Alfredo", "Ricardo", "Larissa"]
direc = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
def pokemonupdate(nome, valor):
    if nome == "Nome":
        jogador[nome] = valor
    elif nome == "Pokemons":
         jogador[nome].append(valor)
    else:
        jogador[nome] = jogador[nome] + valor
        if jogador["Dinheiro"] < 0:
            jogador["Dinheiro"] = 0

def playerstatus():
    pokemoni = pokemons()
    return f"Nome:{jogador['Nome']}\nNivel:{jogador['Nivel']}\nDinheiro:{jogador['Dinheiro']}\nPokemons:\n{pokemoni}"

def load(algo):
    global jogador
    if algo:
        arquivo = open(f"{direc}\\database.db", "rb")
        try:
            jogador = pickle.load(arquivo)
            print("Dados carregados com sucesso!")
        except Exception:
            print("Não há nada para carregar!")
        arquivo.close()
    else:
        arquivo = open(f"{direc}\\database.db", "wb")
        pickle.dump(jogador, arquivo)
        print("Dados salvos com sucesso!")
        arquivo.close()
def luta(oponente, pokemono, nivelo):
    pokemonp, nivelp = None, None
    print("Iniciando luta!, lista de ")
    print("-"*20)
    print("Pokemons disponíveis")
    print("-"*20)
    print(pokemons())
    print("-"*20)
    while True:
        escolher = str(input("Escolha um(Nome:Nivel):"))
        if not escolher or len(escolher.split(":")) != 2:
            print("Algo errado, tente novamente!")
        else:
            escolher = escolher.split(":")
            nachado = True
            for e in jogador["Pokemons"]:
                for pokemonn, nivel in e.items():
                    if pokemonn.lower() == escolher[0].lower() and nivel == int(escolher[1]):
                        print("Pokemon encontrado!")
                        pokemonp = pokemonn
                        nivelp = nivel
                        nachado = False
                if not nachado:
                    break
            if nachado:
                print("Pokemon não encontrado!")
            else:
                break
    vidap, vidao = (nivelp * 10) + 70, (nivelo * 10) + 70
    danop, danoo = (nivelp * 5), (nivelo * 5)
    _, ataquep = pokemon.elemento(pokemonp)
    _, ataqueo = pokemon.elemento(pokemono)
    ganhou = False
    while True:
        print(f"O {pokemonp} de {jogador['Nome']} tenta utilizar {ataquep} contra o {pokemono} de {oponente}!")
        sleep(random.randint(2, 4))
        if random.randint(0, 100) <= (45 + (nivelp * 0.50)):
            dano = random.randint(1, danop)
            vidao -= dano
            print(f"Acertando!! Causando {dano} de dano! Agora o {pokemono} de {oponente} tem {vidao} de vida!")
            if vidao <= 0:
                print(f"Parabéns {jogador['Nome']} você ganhou a partida!")
                ganhou = True
                break
        else:
            print(f"O {pokemono} de {oponente} se esquivou rapidamente do golpe!")
        sleep(2)
        print(f"Agora o {pokemono} tenta utilizar {ataqueo} contra o {pokemonp} de {jogador['Nome']}!")
        sleep(random.randint(2, 4))
        if random.randint(0, 100) <= (45 + (nivelo * 0.50)):
            dano = random.randint(1, danoo)
            vidap -= dano
            print(f"Acertando!! Causando {dano} de dano! Agora o {pokemonp} de {jogador['Nome']} tem {vidap} de vida!")
            if vidap <= 0:
                print(f"Infelizmente o {oponente} ganhou a partida!")
                ganhou = False
                break
        else:
            print(f"O {pokemonp} de {jogador['Nome']} se esquivou rapidamente do golpe!")
        sleep(2)
    moedas = random.randint(1, nivelo * 2)
    if ganhou:
        nivel = (nivelo * 0.05)
        print(f"Você ganhou como espólio {nivel} de xp, e {moedas} moedas!")
        pokemonupdate("Nivel", nivel)
        pokemonupdate("Dinheiro", moedas)
    else:
        print(f"Você perdeu {moedas} moedas!")
        pokemonupdate("Dinheiro", (moedas - (moedas * 2)))

def batalhar():
    global inimigos
    verificar = pokemons()
    if not verificar:
        print("Você não tem pokemons para lutar, volte quando tiver um!")
        return
    print("Procurando inimigos!")
    if random.choice((True, False)):
        oponente = random.choice(inimigos)
        pokemonn, nivel = pokemon.aleatoriopokemon()
        print("Oponente encontrado!")
        print(f"Oponente:{oponente}, Pokemon:{pokemonn}({nivel}) F:{(nivel * 5)}, H:{(70 + (nivel * 10))}")
        while True:
            escolher = str(input("Deseja lutar?(S/N)"))
            if escolher.lower() == "s":
                luta(oponente, pokemonn, nivel)
                break
            elif escolher.lower() == "n":
                print("Tentando fugir")
                if random.choice((True, False)):
                    print("Não foi possível escapar, forçado a lutar.")
                    luta(oponente, pokemonn, nivel)
                else:
                    print("Fuga feita com sucesso!")
                break
            else:
                print("Opção inválida!")
    else:
        print("Não foi encontrado inimigos próximos!")

def pokemons():
    todos = ""
    contar = 0
    for e in jogador["Pokemons"]:
        contar += 1
        for pokemon, nivel in e.items():
            todos += f"{contar} - {pokemon}({nivel}) F:{(nivel * 5)}, H:{70 + (nivel * 10)}\n"
    return todos