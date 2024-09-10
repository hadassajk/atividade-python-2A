
def soma_pares_ate(numero):
    
 """Calcule a soma dos numeros pares ate um determinado numero

 Args:
 
 numero: o numero limite ate onde a soma sera calculado.
 
 Returns:
 
 A soma dos numeros pares.
 """

 soma = 0 
contador = 2 
while contador <= numero:
    soma += contador 
    contador += 2 
return soma 

# Obtendo o numero do usuario

 numero = int(input("Digite um numero :"))

# Chamando a funçao e imprimindo o resultado
resultado = soma_pares_ate(numero)
print(f" A soma dos numeros pares ate {numero}  e : {resultado}"