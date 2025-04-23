from tabulate import tabulate

def exchangeMoney(dinero, tasaOrigen, tasaDestino):
    resultado = dinero * (tasaDestino / tasaOrigen)
    return resultado

def mostrarPaises():
    paises = [
        ["Número", "País", "Tasa de Cambio"],
        ["1", "Japón", 142.96],
        ["2", "México", 19.626],
        ["3", "Alemania", 0.8685],
        ["4", "Colombia", 4346.48],
        ["5", "Estados Unidos", 1.00],
        ["6", "República Dominicana", 60.20],
        ["7", "Brasil", 5.7225]
    ]
    print(tabulate(paises, headers="firstrow", tablefmt="grid"))

def obtenerTasa(pais):
    tasas = {
        "1": 142.96,
        "2": 19.626,
        "3": 0.8685,
        "4": 4346.48,
        "5": 1.00,
        "6": 60.20,
        "7": 5.7225
    }
    return tasas.get(pais)

while True:
    print("\n=== Calculadora de Divisas ===")
    dinero = float(input("¿Cuánto dinero tienes? "))

    print("¿En qué país tienes ese dinero?")
    mostrarPaises()
    paisOrigen = input("Escribe el número del país origen: ")

    print("¿A qué país vas a viajar?")
    mostrarPaises()
    paisDestino = input("Escribe el número del país destino: ")

    tasaOrigen = obtenerTasa(paisOrigen)
    tasaDestino = obtenerTasa(paisDestino)

    if tasaOrigen is not None and tasaDestino is not None:
        resultado = exchangeMoney(dinero, tasaOrigen, tasaDestino)
        print(tabulate([
            ["Moneda origen", dinero],
            ["Tasa origen", tasaOrigen],
            ["Tasa destino", tasaDestino],
            ["Total recibido", round(resultado, 2)]
        ], tablefmt="fancy_grid"))
    else:
        print("Opción inválida.")

    seguir = input("¿Quieres hacer otra conversión? (s/n): ")
    if seguir.lower() != "s":
        print("Gracias por usar la calculadora. ¡Buen viaje!")
        break
