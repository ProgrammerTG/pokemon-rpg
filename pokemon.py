#Módulos
import random
import player

#Pokemons Lista
pokemons = {"Raio":["Pikachu"], "Fogo": ["Charmander"], "Água": ["Squirtle"]}
elementos = []
for e, v in pokemons.items():
    elementos.append(e)

def aleatoriopokemon():
    nivel = random.randint(10, 50)
    pokemon = random.choice(pokemons[random.choice(elementos)])
    return pokemon, nivel

def elemento(pokemon):
    ataque = {"Fogo": "bola de fogo", "Raio": "choque", "Água": "jato d'água"}
    for e, v in pokemons.items():
        if pokemon in v:
            return e, ataque[e]
            

def explorar():
    if random.choice((True, False)):
        print("Você encontrou um pokemon!")
        print("Identificando espécie!")
        pokemon, nivel = aleatoriopokemon()
        print(f"Pokemon identificado: {pokemon}({nivel})")
        while True:
            escolher = str(input("Deseja capturar?(S/N) "))
            if escolher.lower() == "s":
                print("Tentando capturar")
                if random.randint(0, 100) < (50 - (nivel * 0.50)):
                    print("Pokemon capturado!")
                    player.pokemonupdate("Pokemons", {pokemon: nivel})
                else:
                    print("Que pena! O pokemon fugio, fica para a próxima!")
                break
            elif escolher.lower() == "n":
                print("Ignorando!")
                break
            else:
                print("Selecione uma opção válida!")
    else:
        print("Não achou nada dessa vez, mais sorte na próxima!")
    