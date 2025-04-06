# Interfaz de Métodos Numéricos

Esta aplicación proporciona una interfaz gráfica para resolver ecuaciones utilizando diferentes métodos numéricos:
- Newton-Raphson
- Falsa Posición
- Bisección

## Requisitos
- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación

1. Crear un entorno virtual:
```bash
python -m venv venv
```

2. Activar el entorno virtual:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Ejecutar la aplicación:
```bash
python interfaz.py
```

2. Ingresar la función matemática en el campo "f(x)"
3. Seleccionar el método numérico deseado
4. Configurar los parámetros específicos del método
5. Hacer clic en "Calcular Raíz"

## Notas
- La función debe ser ingresada usando la sintaxis de Python (ejemplo: x**2 - 4)
- Se recomienda usar una tolerancia entre 0.0001 y 0.000001
- El número máximo de iteraciones por defecto es 50 