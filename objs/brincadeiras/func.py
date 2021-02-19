def faz_matriz(matriz):
    col = len(matriz[0])
    lin = len(matriz)

    s = ''

    for i in range(lin):
        for j in range(col):
            s += matriz[i][j]

    return s