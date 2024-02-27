

print("LISTADO A ORDENAR")  
    
producto=input("digite el nombre del  producto")
precio=input(int("digite el precio"))
cantidad=input(int("digite la cantidad"))




subtotal =(precio*cantidad)
descuento=subtotal-20%subtotal
neto=subtotal-descuento
    
print(f"el subtotal es{subtotal}")
print(f"el descuento es{descuento}")
print(f"el valor neto es {neto}")

