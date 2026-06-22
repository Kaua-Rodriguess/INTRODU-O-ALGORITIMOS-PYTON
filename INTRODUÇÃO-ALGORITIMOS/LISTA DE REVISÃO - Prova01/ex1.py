n = int(input("Digite um número inteiro: "))

if n <= 1:
    print(f"{n} não é primo")
else:
    cont = 2
    eh_primo = True

    while cont < n:
        if n % cont == 0:
            eh_primo = False

        print(f"contador:{cont}")    
        cont += 1

    if eh_primo:
        print(f"{n} é primo")
    else:
        print(f"{n} não é primo")