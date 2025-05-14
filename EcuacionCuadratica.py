
a = int(input("cuanto vale a? "))
b = int(input("cuanto vale b? "))
c = int(input("cuanto vale c? "))

casoP = (-b + (b*b - 4*a*c)**0.5) / (2*a)
casoN = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(casoP)
print(casoN)