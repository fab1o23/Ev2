fondo_cambio=40000
registro_descuentos_acumulados=0
registro_dinero_ingresado=0
auto=2000
camioneta=3000
camion=4000
motocicleta=890
total=0
precio_actual=total
print("VEHICULOS DISPONIBLES PARA ESTACIONAR")
print("-------------------------------------")
print(" Auto: $2.000\n Camioneta: $3.000\n Camión: $4.000\n Motocicleta: $890")
while True:
    correo=str(input("Ingrese su correo electronico: "))
    if len(correo)<8 or len(correo)>30:
        print("El correo debe tener como minimo 8 caracteres y como maximo 30.")
        continue
    while True:
        try:
            ingreso_dinero=int(input("Ingrese un monto para pagar: $"))
            if ingreso_dinero<1 or ingreso_dinero>10000:
                print("El monto ingresado no puede ser menor a $1 ni mayor a $10.000")
                continue
        except ValueError:
            print("El monto debe ser un número")
            continue
        print("Menu")
        print("--------------\n")
        print("Los vehiculos disponibles son\n [1]Auto: $2.000\n [2]Camioneta: $3.000\n [3]Camión: $4.000\n [4] Motocicleta: $890")
        opc=""
        while True:
            try:
                opc=int(input("Seleccione el numero de el vehiculo deseado: "))
                if opc==1:
                    print("Has seleccionado Auto con un valor de $2.000")
                    total=2000
                if opc==2:
                    print("Has seleccionado Auto con un valor de $3.000")
                    total=3000
                if opc==3:
                    print("Has seleccionado Auto con un valor de $4.000")
                    total=4000
                if opc==4:
                    print("Has seleccionado Auto con un valor de $890")
                    total=890
            except ValueError:
                print("Caracteres invalidos, ingrese un numero de 1 a 4")
                continue
            break
        break
    for letra in correo:
        if letra=="@":
            break
        if letra.lower()=="A":
            descuento=1
        elif letra.lower()=="Z":
            descuento=0.3
        elif letra.lower()=="L":
            descuento=-0.2
        elif letra.lower()=="Z":
            descuento=0.3
        elif letra.lower()=="B":
            descuento=0.7
        elif letra.lower()=="M":
            descuento=1.3
        elif letra.lower()=="O":
            descuento=-0.2
        elif letra.lower()=="E":
            descuento=-1
        elif letra.lower()=="U":
            descuento=0.5
        elif letra.lower()==".":
            descuento=-1
        elif letra.lower()=="X":
            descuento=2
        elif letra.lower()=="Y":
            descuento=2.1
        elif letra.lower()=="I":
            descuento=6
        else: descuento=0
        registro_descuentos_acumulados+=descuento
        monto_descuento=total*(descuento/100)
        precio_actual-=monto_descuento
        if registro_descuentos_acumulados>=90:
            print(f"\n descuento total acumulado: {registro_descuentos_acumulados}, el estacionamiento es gratuito")
            precio_actual=0
        elif registro_descuentos_acumulados > 0:
            print(f"\n Descuento total acumulado: {registro_descuentos_acumulados}%, descuento aplicado")
        else:
            print(f"\nNo hay descuento acumulado, precio final sin cambios: {total}")
        
        print(f"El precio final despues de aplicar los descuento es de: {precio_actual:.0f}")
        continuar=str(input("Desea continuar su compra? (si/no): "))
        if continuar =="si":
            continue
        else:
            print("Has finalizado tu compra!")
        break
    
        