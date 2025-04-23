# Calculadora de Divisas

Este es un programa en Python que permite convertir dinero entre distintos países utilizando tasas de cambio reales. Es una herramienta útil para viajeros que necesitan saber cuánto dinero recibirán al cambiar su moneda de origen por otra extranjera.

## Versión de Python

- Python 3.12.10

## Requisitos

- Librería externa: tabulate

## ¿Qué hace este programa?

Camila y Diego viajan frecuentemente por motivos laborales. Este programa les permite:

- Ingresar el monto de dinero que poseen.
- Seleccionar el país de origen y el país al que van a viajar.
- Ver una tabla con las tasas de cambio y el total que recibirán.

El sistema calcula automáticamente el equivalente en la moneda extranjera según las tasas reales predefinidas. Toda la información se muestra de forma clara y ordenada usando tablas.

## Instalación y Ejecución (paso a paso desde la terminal)

# 1. Clona el repositorio desde GitHub:

git clone https://github.com/YandellCM/CalculadoraDivisas.git

# 2. Entra a la carpeta del proyecto:

cd CalculadoraDivisas

# 3. Crea el entorno virtual dentro del proyecto:

python -m venv venv

# 4. Activa el entorno virtual:

source venv/Scripts/activate

# 5. Instala las dependencias necesarias:

pip install -r requirements.txt

# 6. Ejecuta el programa:

python Calculadora.py
