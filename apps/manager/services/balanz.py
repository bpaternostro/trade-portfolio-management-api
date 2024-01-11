import os
import requests

from ..constants import BALANZ_INIT_URL, BALANZ_COTIZACIONES_URL, BALANZ_LOGIN_URL
from .exchange import Exchange

class Balanz(Exchange):
    
    def __init__(self) -> None:
        self.nonce = None
        self.source = "WebV2"
        self.id_dispositivo = "7115b259-b8ba-4c5c-8312-6c1bd2108411"
        self.token = None
        self.headers = {'Accept': 'application/json'}
        

    def _connect(self) -> None:
        body = {"user": os.getenv("USERNAME"), "source":"WebV2"}
        resp = requests.post(BALANZ_INIT_URL,data=body, headers=self.headers)
        self.nonce = resp.json().get("nonce") 

    def _login(self) -> bool:
        body = {
            "user": os.getenv("USERNAME"),
            "pass": os.getenv("PASSWORD"),
            "nonce": self.nonce,
            "source": self.source,
            "idDispositivo": self.id_dispositivo,
            "TipoDispositivo": "Web",
            "NombreDispositivo": "Chrome 119.0.0.0",
            "SistemaOperativo": "Linux",
            "VersionSO": "x86_64",
            "VersionAPP": "2.9.4"
        }
        resp = requests.post(BALANZ_LOGIN_URL, data=body, headers=self.headers)
        self.token = resp.json().get("AccessToken") 

    def get_rates(self, financial_instrument) -> list:
        self._connect()
        self._login()
        self.headers = {
            'Accept': 'application/json',
            'Authorization': self.token,
        }
        resp = requests.get(BALANZ_COTIZACIONES_URL.get(financial_instrument), headers=self.headers)
        return resp.json().get("cotizaciones")

    def make_logout(self):
        pass