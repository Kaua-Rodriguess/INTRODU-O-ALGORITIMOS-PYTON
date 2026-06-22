
def print_recursivo(x):
    print(x)

    if x > 0:
        print_recursivo(x-1)
    print(x)
    


#PROGRAMA PRICIPAL

print_recursivo(3)