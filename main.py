import pokemon, player
def __main__():
    rodar = True
    while rodar:
        print("-"*20)
        print("1 - Explorar pelo mundão a fora")
        print("2 - Lutar com um inimigo")
        print("3 - Ver Pokeagenda")
        print("4 - Player status")
        print("0 - Sair do jogo")
        print("-"*20)
        escolher = str(input("Escolha uma opção:"))
        if escolher == "1":
            pokemon.explorar()
        elif escolher == "2":
            player.batalhar()
        elif escolher == "3":
            print("-"*20)
            print("Lista de pokemons")
            print("-"*20)
            print(player.pokemons())
            print("-"*20)
        elif escolher == "0":
            player.load(False)
            print("-"*20)
            print("Obrigado por jogar! volte sempre!")
            print("-"*20)
            rodar = False
        elif escolher == "4":
            print("-"*20)
            print("Player status")
            print("-"*20)
            print(player.playerstatus())
            print("-"*20)


if __name__ == "__main__":
    print("-"*20)
    print("Bem-vindo a o RPG de Pokemon!")
    print("-"*20)
    print("Iniciando")
    print("Carregando dados!")
    player.load(True)
    __main__()