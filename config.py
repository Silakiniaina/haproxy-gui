from dataclasses import dataclass

@dataclass
class Config:
    DEBUG = True
    SECRET_KEY = 'votre_clé_secrète_ici'
    # Autres configurations...