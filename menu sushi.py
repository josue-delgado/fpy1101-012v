import os
import time

# Cantidad de pedidos
pikachu_Roll = 0
otaku_Roll = 0
pulpo_venenoso_Roll = 0
anguila_electrica_Roll = 0



opciones = 0

while True:
    opciones = int(input("Bienvenido a Sushi, que desea pedir \n (1) Pikachu Roll $4500 \n (2) Otaku Roll $5000 \n (3) Pulpo Venenoso Roll $5200 \n (4) Anguila Eléctrica Roll $4800 \n (5) Finalizar Pedido \n (6) salir \n Ingrese una Opcion: "))
    if opciones == 1:
        pikachu_Roll += 1
    elif opciones == 2:
        otaku_Roll += 1
    elif opciones == 3:
        pulpo_venenoso_Roll += 1
    elif opciones == 4:
        anguila_electrica_Roll += 1
    elif opciones == 5:
        totalProductos = (pikachu_Roll + otaku_Roll + pulpo_venenoso_Roll + anguila_electrica_Roll)
        totalPagar = (pikachu_Roll * 4500 + otaku_Roll * 5000 + pulpo_venenoso_Roll * 5200 + anguila_electrica_Roll * 4800)
        while True:
            cuponOpcion = input("¿Tiene algun cupon de descuento? Si - No: ")
            if cuponOpcion == "Si" or cuponOpcion == "si" or cuponOpcion == "sI" or cuponOpcion == "SI": 
                cuponDescuento = input("Ingrese su cupon de descuento: ")
                if cuponDescuento == "soyotaku" or cuponDescuento == "SOYOTAKU":
                  total_Pagar_Descuento = totalPagar * 0.1
            print(f"******* \n Total Productos {totalProductos} \n ******* \n Pikachu Roll: {pikachu_Roll} \n Otaku Roll: {otaku_Roll} \n Pulpo Roll: { pulpo_venenoso_Roll} \n Anguila Venenosa Roll: {anguila_electrica_Roll} \n ******* \n Subtotal por pagar: ${totalPagar} \n Descuento por codigo: ${round(total_Pagar_Descuento)} \n TOTAL: ${round(totalPagar - total_Pagar_Descuento)}                                               ")
            break
    elif opciones == 6:
        print("Gracias por preferirnos")
        os.system("cls")
        break
    else:
        os.system("cls")
        print("Ingrese el numero correcto del 1-5")
        time.sleep(1)
        os.system("cls")        
        continue
 
    print(f"Pikachu: {pikachu_Roll} \n Otaku: {otaku_Roll} \n Pulpo: {pulpo_venenoso_Roll} \n Anguila: {anguila_electrica_Roll}")