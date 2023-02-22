decimal = int(input("Quel decimal voulez-vous convertir en binaire ?"))

nbr = decimal
binaire1 = ''

while decimal > 0:
    quotient=decimal//2
    reste=decimal%2
    binaire1 += str(reste)
    decimal=quotient

binaire = ''
for i in range(len(binaire1)-1, -1, -1):
    binaire += binaire1[i]
 
print("\nLe nombre entier positif (",nbr,") en base 10 est noté (",binaire,") en binaire.")
