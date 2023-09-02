def ler(x, y):
    while True:
        z = int(input(f"Digite um numero de {x}-{y}: "))
        if x <= z <= y:
            break

    return z