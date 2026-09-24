# MANUAL DE USUARIO DEL SOFTWARE

## Escáner básico de puertos TCP



---

## 1. Descripción general

El programa `scanner_puertos.py` es una herramienta básica desarrollada en Python para verificar puertos TCP abiertos dentro de un rango definido por el usuario.

El sistema solicita una dirección IP, un puerto inicial y un puerto final. Luego realiza conexiones TCP secuenciales sobre el rango indicado y muestra los puertos que responden como abiertos.

> **Importante:** La herramienta debe utilizarse únicamente sobre equipos propios, máquinas virtuales o redes para las que se disponga de autorización explícita.

---

## 2. Objetivo

Permitir al usuario comprobar de manera sencilla qué puertos TCP se encuentran abiertos en un equipo autorizado, mostrando el progreso del análisis y un resumen final de los resultados.

---

## 3. Requisitos

Para ejecutar el programa se requiere:

- Python 3 instalado.
- Sistema operativo Windows, Linux o macOS.
- Acceso a una terminal o consola.
- El archivo `scanner_puertos.py`.
- Conectividad con el equipo que se desea analizar.

No es necesario instalar librerías externas, ya que el programa utiliza módulos incluidos en Python:

- `ipaddress`
- `socket`
- `dataclasses`

---

## 4. Ejecución del programa

### 4.1 Abrir la terminal

Ubicarse en la carpeta donde se encuentra el archivo `scanner_puertos.py`.

### 4.2 Ejecutar el programa

```bash
python scanner_puertos.py
```

Si el sistema utiliza el comando `python3`, ejecutar:

```bash
python3 scanner_puertos.py
```

---

## 5. Uso paso a paso

Al iniciar, el programa muestra el encabezado:

```text
==========================================
          ESCÁNER DE PUERTOS TCP
==========================================
Use esta herramienta únicamente con autorización.
```

### Paso 1. Ingresar la dirección IP

El sistema solicitará:

```text
IP:
```

Ejemplo:

```text
127.0.0.1
```

El programa valida que la dirección ingresada corresponda a una dirección IPv4 o IPv6 válida.

### Paso 2. Ingresar el puerto inicial

El sistema solicitará:

```text
Desde:
```

Ejemplo:

```text
20
```

### Paso 3. Ingresar el puerto final

El sistema solicitará:

```text
Hasta:
```

Ejemplo:

```text
100
```

El rango permitido es de **1 a 65535**.

El puerto inicial no puede ser mayor que el puerto final.

### Paso 4. Esperar el análisis

El programa mostrará:

```text
Escaneando...
```

Durante el proceso se presenta el avance:

```text
Progreso: 25/81
```

Cuando se detecta un puerto abierto se muestra, por ejemplo:

```text
Puerto 80 - ABIERTO
```

### Paso 5. Revisar el resumen final

Al finalizar se muestra un resumen como el siguiente:

```text
--- RESUMEN ---
IP analizada: 127.0.0.1
Rango: 20-100
Puertos analizados: 81
Puertos abiertos: 2
Lista de puertos abiertos: 22, 80
```

Si no se encuentra ningún puerto abierto:

```text
No se encontraron puertos abiertos en el rango indicado.
```

---

## 6. Validaciones del sistema

El programa incluye validaciones para evitar entradas incorrectas.

### Dirección IP inválida

```text
Entrada inválida: La IP no es válida. Ejemplo: 127.0.0.1
```

### Puerto no numérico

```text
Entrada inválida: El puerto inicial debe ser un número entero.
```

### Puerto fuera del rango permitido

```text
Entrada inválida: El puerto debe estar entre 1 y 65535.
```

### Puerto inicial mayor que el final

```text
Entrada inválida: El puerto inicial no puede ser mayor que el puerto final.
```

---

## 7. Cancelación del escaneo

El usuario puede cancelar la ejecución presionando:

```text
Ctrl + C
```

El sistema mostrará:

```text
Escaneo cancelado por el usuario.
```

---

## 8. Funcionamiento técnico

El programa está organizado en funciones independientes para facilitar su comprensión y mantenimiento.

### `validar_ip()`

Valida una dirección IPv4 o IPv6 y devuelve su representación normalizada.

### `validar_puerto()`

Convierte el valor ingresado a número entero y verifica que se encuentre entre los puertos 1 y 65535.

### `puerto_abierto()`

Crea una conexión TCP mediante `socket` y utiliza `connect_ex()` para comprobar si el puerto responde. Si el resultado es `0`, el puerto se considera abierto.

### `escanear_puertos()`

Recorre secuencialmente todos los puertos comprendidos entre el puerto inicial y el puerto final. Los puertos abiertos se almacenan en una lista.

### `solicitar_datos()`

Solicita al usuario la dirección IP, el puerto inicial y el puerto final, y controla los errores de entrada.

### `mostrar_resumen()`

Presenta los resultados obtenidos al finalizar el escaneo.

### `main()`

Controla el flujo principal del programa:

1. Muestra el encabezado.
2. Solicita los datos.
3. Ejecuta el escaneo.
4. Controla errores o cancelaciones.
5. Presenta el resumen.

---

## 9. Estructura de resultados

Los resultados se almacenan temporalmente en la clase `ResultadoEscaneo`, que contiene:

- IP analizada.
- Puerto inicial.
- Puerto final.
- Lista de puertos abiertos.
- Cantidad total de puertos analizados.

---

## 10. Tiempo de espera

El programa utiliza un tiempo de espera predeterminado de **0.5 segundos** para cada intento de conexión.

---

## 11. Ejemplo completo de uso

```text
==========================================
          ESCÁNER DE PUERTOS TCP
==========================================
Use esta herramienta únicamente con autorización.

IP: 127.0.0.1
Desde: 1
Hasta: 100

Escaneando...
Puerto 80 - ABIERTO
Progreso: 100/100

--- RESUMEN ---
IP analizada: 127.0.0.1
Rango: 1-100
Puertos analizados: 100
Puertos abiertos: 1
Lista de puertos abiertos: 80
```

Los resultados dependen de los servicios activos en el equipo autorizado analizado.

---

## 12. Recomendaciones de uso

- Utilizar rangos pequeños durante las pruebas iniciales.
- Verificar que la dirección IP sea correcta.
- Ejecutar pruebas únicamente en entornos autorizados.
- No utilizar la herramienta para analizar equipos o redes de terceros sin permiso.
- Cancelar el proceso con `Ctrl + C` cuando sea necesario.

---

## 13. Conclusión

El escáner de puertos TCP permite identificar puertos abiertos dentro de un rango definido por el usuario mediante conexiones TCP simples. Su estructura modular facilita la validación de datos, el control de errores y la presentación clara de resultados.

El programa fue diseñado con fines educativos y de práctica en entornos controlados y autoriza
