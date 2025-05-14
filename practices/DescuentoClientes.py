
precio = float(input("Ingrese el precio del producto: "))
cliente = input("Ingrese el tipo de cliente (regular o VIP): ").lower()

if cliente == "regular":
    descuento = 0.05  
    tipo_descuento = "regular"

elif cliente == "vip":
    descuento = 0.10
    tipo_descuento = "VIP"
    
else:
    descuento = 0 
    tipo_descuento = "ninguno"


precio_final = precio * (1 - descuento)

print(f"El descuento aplicado es del {descuento * 100}%. El precio final es: {precio_final}")