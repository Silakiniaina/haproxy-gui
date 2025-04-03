from models.backend import Backend
from models.frontend import Frontend
from services.storage_service import StorageService

class HAProxyConfigGenerator:
    def __init__(self, storage_service: StorageService):
        self.storage = storage_service

    def generate_config(self) -> str:
        config_lines = []
        
        config_lines.extend(self._generate_global_section())
        config_lines.extend(self._generate_defaults_section())
        
        for frontend in self.storage.frontends.values():
            config_lines.extend(self._generate_frontend_config(frontend))
        
        for backend in self.storage.backends.values():
            config_lines.extend(self._generate_backend_config(backend))
        
        return "\n".join(config_lines)

    def _generate_global_section(self) -> list:
        return [
            "global",
            "    daemon",
            "    maxconn 256",
            "    log /dev/log local0",
            "    log /dev/log local1 notice",
            ""
        ]

    def _generate_defaults_section(self) -> list:
        return [
            "defaults",
            "    mode http",
            "    timeout connect 5000ms",
            "    timeout client 50000ms",
            "    timeout server 50000ms",
            "    option httplog",
            "    log global",
            ""
        ]

    def _generate_frontend_config(self, frontend: Frontend) -> list:
        config_lines = [
            f"frontend {frontend.name}",
            f"    mode {frontend.mode}",
            f"    bind {frontend.bind}"
        ]
        if frontend.maxconn:
            config_lines.append(f"    maxconn {frontend.maxconn}")
        if frontend.timeout_client:
            config_lines.append(f"    timeout client {frontend.timeout_client}")
        if frontend.client_fin_timeout:
            config_lines.append(f"    timeout client-fin {frontend.client_fin_timeout}")
        if frontend.ssl:
            config_lines.append("    bind {frontend.bind} ssl")
            if frontend.ssl_certificate:
                config_lines.append(f"    ssl crt {frontend.ssl_certificate}")
            if frontend.ssl_ciphers:
                config_lines.append(f"    ssl-default-bind-ciphers {frontend.ssl_ciphers}")
        for backend in frontend.backends:
            config_lines.append(f"    default_backend {backend}")
        config_lines.append("")
        return config_lines