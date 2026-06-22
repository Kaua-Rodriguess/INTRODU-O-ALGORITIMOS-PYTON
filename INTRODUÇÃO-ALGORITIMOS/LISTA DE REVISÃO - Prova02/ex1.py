def validar_senha(senha):
    senha_valida = True
    numero = 0
    letra = 0
    porcent = 0

    if (len(senha) < 8):
       senha_valida = False
 
    for c in senha:
       if((c >= '0') and (c <= '9')):
           numero += 1
    
       if c >= 'A' and c <= 'z':
           letra +=1
    
       if( c == " "):
           senha_valida = False

    if (numero < 1):
     senha_valida = False
    if (letra < 1):
     senha_valida = False
      
    return senha_valida

def porcentagem(validas,total): 
    if total == 0:
       return 0
    
    return (validas/total) * 100
    
#==================PROGRAMA PRINCIPAL======================
print("VALIDADOR DE SENHA:\n")

total_senhas = 0
total_validas = 0

senha = input("Digite uma senha: ") 

while senha != "sair":
    total_senhas += 1

    resultado = validar_senha(senha)

    if resultado:
     print("Senha válida!")
     total_validas += 1
    else:
       print("Senha inválida!")

    senha = input("\nDigite outra senha (ou 'sair' para encerrar): ")

#Resultado final
print("\nRESULTADO FINAL")
print(f"Porcentagem de senhas válidas: {porcentagem(total_validas, total_senhas):.2f}%")

  





