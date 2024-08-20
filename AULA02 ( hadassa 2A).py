# Comentario de uma linha 
# Tipagem dinamica :

teste = "Olá"
print(type(teste))
teste = 30
print(type(teste))
teste = 2.4
print(type(teste))

nome = input("Digite o seu nome :")
print("Olá " , nome )
idade = input("Digite a sua idade")
print(idade)
print(type(idade))


#Tipos de Dados :
#Int : numeros inteiros 
#Float : numeros reais , decimais 
#Str : string , cadeia de caracteres
#Boolean : tipo logico true ou falso 

valorA = int(input("Digite o valor A : "))
valorB = int(input("Digite o valor de B :"))
print(valorA + valorB)
print(type(valorA))


# Operadores Aritimáticos:

x = 3 

print(x + 1) #Adição
print(x - 1) #Subtraçaõ
print(x * 2) #Multipliçaõ
print(x / 2) #Divisão
print(x // 2) #Divisão inteiro 
print(x ** 2) #Exponenciação
print(x % 2) #Resto da divisão / Modulo


# Algoritimo Media
#CRIAR UM ALGORITMO QUE LEIA 4 NOTAS E APRESENTE A MEDIA FINAL

nota1 =float(input("Digite sua primeira nota "))
nota2 = float(input("Digite sua segunda nota "))
nota3 = float(input("Digite sua terceira nota "))
nota4 = float(input("Digite sua quarta nota "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print("A media final obtida :" , media)
