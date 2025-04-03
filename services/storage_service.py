from typing import Dict
from models.backend import Backend
from models.frontend import Frontend

class StorageService:
    def __init__(self):
        self.backends: Dict[str, Backend] = {}
        self.frontends: Dict[str, Frontend] = {}

    def add_backend(self, backend: Backend) -> None:
        self.backends[backend.name] = backend

    def get_backend(self, name: str) -> Backend:
        return self.backends.get(name)

    def delete_backend(self, name: str) -> None:
        self.backends.pop(name, None)

    def add_frontend(self, frontend: Frontend) -> None:
        self.frontends[frontend.name] = frontend

    def get_frontend(self, name: str) -> Frontend:
        return self.frontends.get(name)

    def delete_frontend(self, name: str) -> None:
        self.frontends.pop(name, None)