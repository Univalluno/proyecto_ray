# Microservicio de Clasificación de Números

Este proyecto implementa un microservicio en Python usando Ray Serve y FastAPI, que clasifica si un número es par o impar. El servicio se ejecuta en un contenedor Docker y puede ser consumido por un cliente HTTP o script en Python.

## 🧰 Tecnologías usadas

- Python 3.10  
- Ray 2.25+ (usando `@ray.remote` y `@serve.deployment`)  
- FastAPI y Uvicorn  
- Docker  
- WSL2 en Windows 11

## 🚀 Cómo ejecutar

### 1. Construir la imagen Docker

```bash
sudo docker build -t ray-fastapi-app .
```

### 2. Ejecutar el contenedor

```bash
sudo docker run -p 8000:8000 ray-fastapi-app
```

### 3. Consumir el microservicio

#### Desde cURL:

```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"number": 9}'
```

#### Desde el cliente Python:

```bash
python3 cliente.py
```

## 📦 Estructura del proyecto

```
proyecto_ray/
├── main.py          # Microservicio con paralelismo @ray.remote
├── Dockerfile       # Imagen Docker
├── cliente.py       # Cliente de prueba
├── README.md        # Documentación final con paralelismo
└── evidencia.txt    # Evidencia técnica actualizada
```

## 🧪 Respuesta esperada

Input:
```json
{"number": 9}
```

Output:
```json
{"numero": 9, "clasificacion": "impar"}
```

## 👤 Autor

Estudiante: [Jerson David Otero Cruz]  
Curso: Infraestructuras Paralelas y Distribuidas  
Universidad del Valle  
Julio 2025
