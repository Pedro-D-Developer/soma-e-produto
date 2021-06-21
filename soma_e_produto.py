def soma(a, b):
    """Recebemos a letra "A" e a letra "B" do usuário e retornamos a "soma". (Equação segundo grau.)"""
    return -abs(b) / -abs(a)


def produto(a, c):
    """Recebemos a letra "A" e a letra "C" do usuário e retornamos o "produto". (Equação segundo grau.)"""
    return c / a


if __name__ == "__main__":
    try:
        letra_a = int(input("Olá, insira o (A) da questão: "))
        letra_b = int(input("Olá, insira o (B) da questão: "))
        letra_c = int(input("Olá, insira o (C) da questão: "))
    except ValueError:
        print("\nUm dos números inseridos estão incorretos.")
        exit()

    print(f"\nSoma = {soma(letra_a, letra_b)}")
    print(f"Produto = {produto(letra_a, letra_c)}")
