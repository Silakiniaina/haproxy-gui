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

    def check_status(self) -> str:
            """Check if the server is up or down by attempting a TCP connection."""
            check_port = self.check_port if self.check_port else self.port
            try:
                # Create a socket connection
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)  # 2-second timeout for quick response
                result = sock.connect_ex((self.host, check_port))
                sock.close()
                
                # If connection succeeds (result == 0), server is up
                if result == 0:
                    self.status = "up"
                else:
                    self.status = "down"
            except Exception as e:
                self.status = "down"  # If any error occurs, assume server is down
            return self.status