binaire = input("Quel est le binaire que vous voulez convertir ?") 

decimal = 0 
decimal = int()
b = 0 


for i in reversed(binaire) : 
    decimal += int(i)*2**b      
    b+=1 
 
print("Le nombre (", binaire, ") en binaire est égal à (",decimal,") en décimal.")
