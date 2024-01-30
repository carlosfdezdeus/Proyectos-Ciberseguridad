import random
import math


def es_primo(numero):
    if numero < 2:
        # Número menor de 2 NO es PRIMO
        return False

    elif numero > 2:
        for i in range (2, numero // 2 + 1):
            if (numero % i == 0):     
                # numero = divisible entre i --> NO es PRIMO
                return False
    
    else:
        # Si no cumple las anteriores condiciones -> No divisible por ningun número => ES PRIMO
        return True


def generador_primos(valor_min, valor_max):
    primo = 2
    while es_primo(primo):
        primo = random.randint(valor_min, valor_max)
    
    return primo


def inverso_modular(e, phi):
    # Calcula el inverso modular de 'e' módulo 'phi'.
    # Devuelve x tal que (e * x) % phi == 1.
    # Lanza un error si el inverso modular no existe.
    try:
        d = pow(e, -1, phi)
        return d
    except ValueError:
        raise ValueError(f"El inverso modular no existe para {e} y {phi}.")


