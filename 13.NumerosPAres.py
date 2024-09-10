# Solicitar ao usuraio o numero
numero = int(input("Digite um numero: "))

# Inicializando variaveis
soma_pares = 0
contador = 2 # O primeiro numero par

# Calculando a soma dos numeros pares usando o loop while
while contador <= numero:
    #print(f"{soma_pares} + {contador} = {soma_pares + contador}")
    soma_pares += contador # soma_pares = soma_pares + contador 
    contador += 2 # Avançando para o proximo numero par 
    
# Exibindo o resultado
print(f" A soma dos numeros pares ate {numero} e {soma_pares}")
