from tabulate import tabulate

def exchange_money(monto, tasa_origen, tasa_destino):
    return monto * (tasa_destino / tasa_origen)

def mostrar_paises():
    paises = [
        ["Número", "País", "Tasa de cambio (1 unidad local = USD)"],
        ["1", "Japón", 0.0075],
        ["2", "México", 0.0509],
        ["3", "Alemania", 1.13],
        ["4", "Colombia", 0.00026],
        ["5", "Estados Unidos", 1.00],
        ["6", "República Dominicana", 0.017],
        ["7", "Brasil", 0.19]
    ]
    print(tabulate(paises, headers="firstrow", tablefmt="grid"))

def obtener_tasa(pais):
    tasas = {
        "1": 0.0075,
        "2": 0.0509,
        "3": 1.13,
        "4": 0.00026,
        "5": 1.00,
        "6": 0.017,
        "7": 0.19
    }
    return tasas.get(pais)

while True:
    print("\n=== Calculadora de Divisas ===")
    monto = float(input("¿Cuánto dinero deseas convertir? "))

    print("¿En qué país tienes ese dinero?")
    mostrar_paises()
    pais_origen = input("Escribe el número del país origen: ")

    print("¿A qué país vas a viajar?")
    mostrar_paises()
    pais_destino = input("Escribe el número del país destino: ")

    tasa_origen = obtener_tasa(pais_origen)
    tasa_destino = obtener_tasa(pais_destino)

    if tasa_origen is not None and tasa_destino is not None:
        resultado = exchange_money(monto, tasa_origen, tasa_destino)
        print(tabulate([
            ["Monto original", monto],
            ["Tasa país origen (1 unidad local = USD)", tasa_origen],
            ["Tasa país destino (1 unidad local = USD)", tasa_destino],
            ["Monto recibido", round(resultado, 2)]
        ], headers=["Descripción", "Valor"], tablefmt="fancy_grid"))
    else:
        print("Opción inválida.")

    seguir = input("¿Quieres hacer otra conversión? (s/n): ")
    if seguir.lower() != "s":
        print("Gracias por usar la calculadora. ¡Buen viaje!")
        break
