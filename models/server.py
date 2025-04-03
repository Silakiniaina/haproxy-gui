from dataclasses import dataclass
import socket
import time

@dataclass
class Server:
    name: str
    host: str
    port: int
    weight: int = 1
    check: bool = False
    check_port: int = None
    check_inter: str = "2s"
    check_fall: int = 3
    check_rise: int = 2
    maxconn: int = 1000
    backup: bool = False
    disabled: bool = False
    maintenance: bool = False
    # Add status field to track server state
    status: str = "unknown"