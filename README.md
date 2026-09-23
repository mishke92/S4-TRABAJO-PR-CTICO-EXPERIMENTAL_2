# Escáner de Puertos TCP en Python

Aplicación básica desarrollada en Python para realizar un escaneo de puertos TCP e identificar cuáles se encuentran abiertos en un equipo autorizado. El proyecto utiliza la biblioteca estándar `socket`, por lo que no requiere instalar paquetes externos.

> **Uso responsable:** esta herramienta debe utilizarse únicamente sobre equipos propios, máquinas virtuales o redes para las que se tenga autorización explícita. No se debe escanear infraestructura de terceros sin permiso.

## Objetivo

Desarrollar una aplicación sencilla que permita:

1. Ingresar una dirección IP.
2. Definir un puerto inicial.
3. Definir un puerto final.
4. Ejecutar un escaneo TCP.
5. Mostrar los puertos abiertos.
6. Presentar un resumen del análisis.

## Requisitos

- Python 3.10 o superior.
- Visual Studio Code u otro editor de código.
- Acceso a una terminal.
- Un equipo, máquina virtual o red autorizada para realizar la prueba.

El programa utiliza exclusivamente módulos incluidos en Python:

- `ipaddress`: validación de direcciones IP.
- `socket`: creación de conexiones TCP.
- `dataclasses`: representación de los resultados.

## Estructura del proyecto

```text
S4-TRABAJO-PR-CTICO-EXPERIMENTAL_2/
├── scanner_puertos.py
└── README.md
```

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```

2. Entrar en la carpeta del proyecto:

   ```bash
   cd S4-TRABAJO-PR-CTICO-EXPERIMENTAL_2
   ```

3. Verificar que Python esté instalado:

   ```bash
   python --version
   ```

   En algunos sistemas puede ser necesario utilizar:

   ```bash
   python3 --version
   ```

No es necesario ejecutar `pip install`, porque el programa no utiliza dependencias externas.

## Ejecución

Desde la carpeta del proyecto, ejecutar:

```bash
python scanner_puertos.py
```

En sistemas donde el comando `python` no esté disponible:

```bash
python3 scanner_puertos.py
```

El programa solicitará los siguientes datos:

```text
IP: 127.0.0.1
Desde: 1
Hasta: 100
```

### Ejemplo de ejecución

```text
==========================================
          ESCÁNER DE PUERTOS TCP
==========================================
Use esta herramienta únicamente con autorización.

IP: 127.0.0.1
Desde: 1
Hasta: 100
Escaneando...
Puerto 22 - ABIERTO
Puerto 80 - ABIERTO
Progreso: 100/100

--- RESUMEN ---
IP analizada: 127.0.0.1
Rango: 1-100
Puertos analizados: 100
Puertos abiertos: 2
Lista de puertos abiertos: 22, 80
```

Los puertos que no acepten conexiones TCP no se muestran como abiertos. Esto no significa necesariamente que el servicio no exista: un firewall puede bloquear la conexión o el servicio puede utilizar otro protocolo.

## Validaciones incluidas

La aplicación verifica que:

- La dirección ingresada sea una IPv4 o IPv6 válida.
- Los puertos sean números enteros.
- Cada puerto esté entre `1` y `65535`.
- El puerto inicial no sea mayor que el puerto final.
- El rango solicitado tenga al menos un puerto.
- Cada conexión tenga un tiempo máximo de espera de `0.5` segundos.

Si los datos son incorrectos, el programa muestra el motivo y solicita ingresarlos nuevamente.

## Funcionamiento técnico

Para cada puerto del rango seleccionado, el programa:

1. Crea un socket TCP.
2. Establece un tiempo máximo de espera.
3. Intenta conectarse a la IP y al puerto.
4. Registra el puerto como abierto si la conexión es aceptada.
5. Cierra el socket al terminar la comprobación.

El escaneo es secuencial y no envía información al servicio remoto; únicamente intenta establecer una conexión TCP.

## Prueba recomendada

Para una prueba local segura, se puede utilizar:

```text
IP: 127.0.0.1
Desde: 1
Hasta: 100
```

También se puede utilizar una máquina virtual propia o un equipo del laboratorio autorizado. Antes de realizar una prueba en otra dirección, debe confirmarse que existe autorización para analizarla.

## Limitaciones

- El programa realiza únicamente escaneo TCP.
- El escaneo es secuencial, por lo que rangos muy amplios pueden tardar más.
- No identifica automáticamente el nombre o la versión del servicio.
- Un puerto filtrado por un firewall puede aparecer como cerrado.
- El resultado depende del estado de la red y de la configuración del equipo analizado.

## Cancelar el escaneo

Para detener la ejecución, presionar:

```text
Ctrl + C
```

El programa informará que el escaneo fue cancelado.

## Publicación en GitHub

Después de crear el repositorio en GitHub, agregar el archivo y subir los cambios:

```bash
git add scanner_puertos.py README.md
git commit -m "Crear escáner de puertos TCP en Python"
git push origin main
```

El enlace del repositorio debe incorporarse en el informe de la práctica.

## Licencia y uso académico

Este proyecto fue desarrollado con fines académicos para demostrar el funcionamiento básico de las conexiones TCP y la identificación de puertos abiertos. Su uso debe respetar las normas institucionales, la legislación vigente y la autorización del propietario de los equipos analizados.
