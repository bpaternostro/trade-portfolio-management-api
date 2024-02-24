import os
import requests

from ..constants import BALANZ_INIT_URL, BALANZ_COTIZACIONES_URL, BALANZ_LOGIN_URL, BALANZ_LOGOUT_URL
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
        resp = requests.post(BALANZ_INIT_URL, data=body, headers=self.headers)
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
        if resp.status_code !=200:
            self.make_logout()
            raise Exception("It was impossible to login with balanz")
        self.token = resp.json().get("AccessToken") 

    def get_rates(self, financial_instrument) -> list:
        try:
            self._connect()
            self._login()
            self.headers = {
                'Accept': 'application/json',
                'Authorization': self.token,
            }
            resp = requests.get(BALANZ_COTIZACIONES_URL.get(financial_instrument), headers=self.headers)
            print(f"Balanz is returning {resp}")
            if resp.status_code !=200:
                raise Exception("It was impossible to connect with balanz")
        except Exception as e:
            return False
        else:
            return resp.json().get("cotizaciones")
        finally:
            self.make_logout()

    def make_logout(self):
        #body = {"normalizedNames": {},"lazyUpdate": None}
        #resp = requests.get(BALANZ_LOGOUT_URL, data=body)
        #if resp.status_code !=200:
        #    raise Exception("It was impossible to logout with balanz")
        pass