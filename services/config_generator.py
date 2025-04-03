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

    def _generate_backend_config(self, backend: Backend) -> list:
        config_lines = [
            f"backend {backend.name}",
            f"    mode {backend.mode}",
            f"    balance {backend.balance}"
        ]
        if backend.timeout_connect:
            config_lines.append(f"    timeout connect {backend.timeout_connect}")
        if backend.timeout_server:
            config_lines.append(f"    timeout server {backend.timeout_server}")
        if backend.timeout_check:
            config_lines.append(f"    timeout check {backend.timeout_check}")
        if backend.check_enabled:
            config_lines.append("    option httpchk")
            if backend.option_httpchk:
                config_lines.append(f"    http-check {backend.option_httpchk}")
        if backend.maxconn:
            config_lines.append(f"    maxconn {backend.maxconn}")
        if backend.retries:
            config_lines.append(f"    retries {backend.retries}")
        if backend.cookie:
            config_lines.append(f"    cookie {backend.cookie} {backend.cookie_type}")
        if backend.forwardfor:
            config_lines.append("    option forwardfor")
        if backend.option_redispatch:
            config_lines.append("    option redispatch")
        
        for server in backend.servers.values():
            server_line = f"    server {server.name} {server.host}:{server.port}"
            if server.weight != 1:
                server_line += f" weight {server.weight}"
            if server.check:
                server_line += " check"
                if server.check_port:
                    server_line += f" port {server.check_port}"
                if server.check_inter:
                    server_line += f" inter {server.check_inter}"
                if server.check_fall:
                    server_line += f" fall {server.check_fall}"
                if server.check_rise:
                    server_line += f" rise {server.check_rise}"
            if server.maxconn:
                server_line += f" maxconn {server.maxconn}"
            if server.backup:
                server_line += " backup"
            if server.disabled:
                server_line += " disabled"
            if server.maintenance:
                server_line += " maintenance"
            if backend.cookie:
                server_line += f" cookie {server.name}"
            config_lines.append(server_line)
        
        config_lines.append("")
        return config_lines