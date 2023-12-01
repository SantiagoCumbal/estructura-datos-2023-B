#Santiago Cumbal
sueldoBase=float(input("Ingrese su sueldo:"))
venta01= float(input("Ingrese el dinero de la venta 1 que realizo en el mes:"))
venta02= float(input("Ingrese el dinero de la venta 2 que realizo en el mes:"))
venta03= float(input("Ingrese el dinero de la venta 3 que realizo en el mes:"))
totalDeVenta = venta01 + venta02 + venta03
comision = totalDeVenta * 0.10 
print("El pago por las ventas realizadas en el mes:", comision)
total = sueldoBase + comision 
print("El pago al mes es:", total)