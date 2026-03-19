#ALAN OLEA EXPONENCIACION BINARIA
def exponenciacion_binaria(base, exponente, mod):
    resultado = 1
    base = base % mod

    while exponente > 0:
        # Si el bit actual es 1
        if exponente % 2 == 1:
            resultado = (resultado * base) % mod

        # Cuadrar la base
        base = (base * base) % mod

        # Pasar al siguiente bit
        exponente //= 2

    return resultado

print(exponenciacion_binaria(2, 1234, 789))