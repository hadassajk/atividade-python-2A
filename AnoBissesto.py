# Venha saber se o ano é bissexto 


ano = int(input("Digite um ano por favor:"))

if ano % 4 == 0  and ano % 100 != 0 or ano % 400 == 0:
    print(f("O ano {ano} é bissexto"))
else:
    print(f"O ano {ano} não é bissexto")