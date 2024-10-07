def calculadora_basica() :
    while True:
        print("Selecione a operação:")
        print("1.Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        operação = input( " Digite o número da opeção desejada: ")

        if operação == '5':
            print(" Saindo da calculadora ...")
            break
        
        if operação in [ '1' , '2' , '3' , '4' ]:
            Try:
            num1 = float(input("Digite o primeiro número:"))
            num2 = float(input("Digite o segundo número:"))
        if operação == '1':
                    resultado = num1 + num2 
                    print ( f " O resultado da soma é : {resultado}")
        elif operação == '2':resultado = num1 - num2
        print (f " O resultado da subtração é : {resultado}")
        
        elif operação == '3'resultado = num1 * num2
        print (f " O resultado da multiplicação é : {resultado}")

        elif operação == '4':
        if num2 != 0: resultado = num1 / num2

    print(f " O resultado da divisão é : {resultado}")
    else:
    print("Erro : Divisão por zero não é permitida .")

    except ValueError:
    print("Erro : Por favor , digite um número válido . ")
    print(" Operação inválida . tente novamente . ")
      
       #calculadora_basica()


