from dataclasses import dataclass, field
from typing import Dict
from .server import Server

@dataclass
class Backend:
    name: str
    mode: str = "http"
    balance: str = "roundrobin"
    servers: Dict[str, Server] = field(default_factory=dict)
    timeout_connect: str = "5s"
    timeout_server: str = "50s"
    timeout_check: str = "5s"
    check_enabled: bool = False
    check_interval: str = "2s"
    check_fall: int = 3
    check_rise: int = 2
    maxconn: int = 2000
    retries: int = 3
    cookie: str = None
    cookie_type: str = "insert"
    http_reuse: str = "safe"
    http_check: str = None
    forwardfor: bool = True
    ssl: bool = False
    ssl_verify: bool = True
    ssl_ca_file: str = None
    option_httpchk: str = None
    option_redispatch: bool = True
    option_persist: bool = True
    compression: bool = False
    compression_types: str = "text/html text/plain text/css"
