from dataclasses import dataclass, field


@dataclass
class Frontend:
    name: str
    bind: str = "*:80"
    mode: str = "http"
    backends: list = field(default_factory=list)
    maxconn: int = 10000
    timeout_client: str = "50s"
    client_fin_timeout: str = "1s"
    tcp_request: list = field(default_factory=list)
    tcp_response: list = field(default_factory=list)
    http_request: list = field(default_factory=list)
    http_response: list = field(default_factory=list)
    acls: dict = field(default_factory=dict)
    use_backend_rules: list = field(default_factory=list)
    ssl: bool = False
    ssl_certificate: str = None
    ssl_options: list = field(default_factory=list)
    ssl_ciphers: str = None