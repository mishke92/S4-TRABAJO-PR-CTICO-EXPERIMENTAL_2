
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

