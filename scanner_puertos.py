"""Escáner básico de puertos TCP para equipos autorizados.

Uso:
    python scanner_puertos.py

El programa realiza conexiones TCP sin enviar datos al servicio remoto.
Utilícelo únicamente sobre equipos propios, máquinas virtuales o redes
para las que tenga autorización explícita.
"""

from __future__ import annotations

import ipaddress
import socket
from dataclasses import dataclass


PUERTO_MINIMO = 1
PUERTO_MAXIMO = 65535
TIEMPO_ESPERA_SEGUNDOS = 0.5


@dataclass(frozen=True)
class ResultadoEscaneo:
    """Resultados del escaneo de un rango de puertos."""

    ip: str
    puerto_inicial: int
    puerto_final: int
    puertos_abiertos: list[int]

    @property
    def puertos_analizados(self) -> int:
        """Cantidad de puertos incluidos en el rango solicitado."""
        return self.puerto_final - self.puerto_inicial + 1


def validar_ip(valor: str) -> str:
    """Valida una dirección IPv4 o IPv6 y devuelve su representación normalizada."""
    try:
        return str(ipaddress.ip_address(valor.strip()))
    except ValueError as error:
        raise ValueError("La IP no es válida. Ejemplo: 127.0.0.1") from error


def validar_puerto(valor: str, nombre: str = "puerto") -> int:
    """Convierte y valida un número de puerto TCP."""
    try:
        puerto = int(valor.strip())
    except ValueError as error:
        raise ValueError(f"El {nombre} debe ser un número entero.") from error

    if not PUERTO_MINIMO <= puerto <= PUERTO_MAXIMO:
        raise ValueError(
            f"El {nombre} debe estar entre {PUERTO_MINIMO} y {PUERTO_MAXIMO}."
        )
    return puerto


def puerto_abierto(ip: str, puerto: int, timeout: float = TIEMPO_ESPERA_SEGUNDOS) -> bool:
    """Comprueba si se puede establecer una conexión TCP con un puerto."""
    familia = socket.AF_INET6 if ":" in ip else socket.AF_INET
    direccion = (ip, puerto, 0, 0) if familia == socket.AF_INET6 else (ip, puerto)

    with socket.socket(familia, socket.SOCK_STREAM) as conexion:
        conexion.settimeout(timeout)
        return conexion.connect_ex(direccion) == 0


def escanear_puertos(
    ip: str,
    puerto_inicial: int,
    puerto_final: int,
    timeout: float = TIEMPO_ESPERA_SEGUNDOS,
) -> ResultadoEscaneo:
    """Escanea secuencialmente un rango de puertos TCP."""
    if puerto_inicial > puerto_final:
        raise ValueError("El puerto inicial no puede ser mayor que el puerto final.")
    if timeout <= 0:
        raise ValueError("El tiempo de espera debe ser mayor que cero.")

    puertos_abiertos: list[int] = []
    total = puerto_final - puerto_inicial + 1

    print("Escaneando...")
    for numero, puerto in enumerate(range(puerto_inicial, puerto_final + 1), start=1):
        try:
            abierto = puerto_abierto(ip, puerto, timeout)
        except OSError as error:
            raise ConnectionError(
                f"No fue posible crear la conexión para el puerto {puerto}: {error}"
            ) from error

        if abierto:
            puertos_abiertos.append(puerto)
            print(f"Puerto {puerto} - ABIERTO")

        print(f"\rProgreso: {numero}/{total}", end="", flush=True)

    print()
    return ResultadoEscaneo(ip, puerto_inicial, puerto_final, puertos_abiertos)


def solicitar_datos() -> tuple[str, int, int]:
    """Solicita y valida los datos introducidos por el usuario."""
    while True:
        try:
            ip = validar_ip(input("IP: "))
            puerto_inicial = validar_puerto(input("Desde: "), "puerto inicial")
            puerto_final = validar_puerto(input("Hasta: "), "puerto final")

            if puerto_inicial > puerto_final:
                raise ValueError(
                    "El puerto inicial no puede ser mayor que el puerto final."
                )
            return ip, puerto_inicial, puerto_final
        except ValueError as error:
            print(f"Entrada inválida: {error}")
            print("Vuelva a ingresar los datos.\n")


def mostrar_resumen(resultado: ResultadoEscaneo) -> None:
    """Muestra el resumen final del escaneo."""
    print("\n--- RESUMEN ---")
    print(f"IP analizada: {resultado.ip}")
    print(
        f"Rango: {resultado.puerto_inicial}-{resultado.puerto_final}"
    )
    print(f"Puertos analizados: {resultado.puertos_analizados}")
    print(f"Puertos abiertos: {len(resultado.puertos_abiertos)}")
    if resultado.puertos_abiertos:
        print("Lista de puertos abiertos:", ", ".join(map(str, resultado.puertos_abiertos)))
    else:
        print("No se encontraron puertos abiertos en el rango indicado.")


def main() -> None:
    """Punto de entrada de la aplicación."""
    print("=" * 42)
    print("          ESCÁNER DE PUERTOS TCP")
    print("=" * 42)
    print("Use esta herramienta únicamente con autorización.\n")

    ip, puerto_inicial, puerto_final = solicitar_datos()
    try:
        resultado = escanear_puertos(ip, puerto_inicial, puerto_final)
    except KeyboardInterrupt:
        print("\nEscaneo cancelado por el usuario.")
        return
    except ConnectionError as error:
        print(f"\nError durante el escaneo: {error}")
        return

    mostrar_resumen(resultado)


if __name__ == "__main__":
    main()

