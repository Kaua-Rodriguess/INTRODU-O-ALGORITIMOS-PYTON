#função recurssiva que retorna a quantidade de digitos de um numero. Exemplo:
#ENTRADA: 6857
#SAÍDA: 4

def contar_digitos(n):
    #caso base
    if n < 10:
        return 1
    
    #A cada interação eu faço uma divisão inteira e somo +1
    #
    
    return 1 + contar_digitos(n // 10)