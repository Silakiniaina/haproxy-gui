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