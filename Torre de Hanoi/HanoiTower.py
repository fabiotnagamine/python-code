def hanoi():
    def mova(n, origem, destino, aux, jogada):
        def mova_disco(de, para, jogada):
            print(f"Jogada {jogada:>3}: Torre {de} Para Torre {para}")
            return jogada + 1 # atualiza para a próxima jogada

        if n == 1:
            jogada = mova_disco(origem, destino, jogada)
        else:
            jogada = mova(n - 1, origem, aux, destino, jogada)
            jogada = mova_disco(origem, destino, jogada)
            jogada = mova(n - 1, aux, destino, origem, jogada)

        return jogada

    n = int(input("Quantos discos deseja considerar? \n -->"))
    print(f"Solução do puzzle ({2 ** n - 1} jogadas): \n")
    mova(n, "1", "3", "2", 1)
hanoi()