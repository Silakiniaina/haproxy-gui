from models.backend import Backend
from models.frontend import Frontend
from services.storage_service import StorageService

class HAProxyConfigGenerator:
    def __init__(self, storage_service: StorageService):
        self.storage = storage_service