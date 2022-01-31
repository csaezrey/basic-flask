## Descripción
El objetivo del código es mostrar un proyecto simple de Python con las siguientes caracterísitcas en un nivel básico:
- Uso de contenedor para su implementación
- Uso de Framework Flask
- Pruebas unitarias
- Ejemplo de excepción
- Ejemplo de logs


## Docker
Para la creación de la imagen, desde la carpeta del archivo dockerfile, docker utilizar el comando:
```
docker build -t wallet .
```

Para la ejecución usar el comando:
```
docker run -i wallet
```

## Python
Para la ejecución de la APP, desde la carpeta CPEX\Wallet, utilizar el comando:
```
python app.py
```

## Pruebas
Desde la carpeta CPEX\Wallet, ejecutar el comando:
```
python -m pytest
```

Considerar que solo incluye 3 pruebas de ejemplo y no hay una [covertura de todo el código](https://pypi.org/project/pytest-cov/).
