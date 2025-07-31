import requests

numero = int(input("Ingrese un número entero: "))
data = {"number": numero}

try:
    response = requests.post("http://localhost:8000/predict", json=data)
    if response.ok:
        resultado = response.json()
        print(f"Resultado: {resultado['numero']} es {resultado['clasificacion']}")
    else:
        print("Error al consultar el servicio:", response.text)
except Exception as e:
    print("Error de conexión:", e)
