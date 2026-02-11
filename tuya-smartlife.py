#!/usr/bin/env python3
"""
Tuya Smartlife Integration para OpenClaw
Control de dispositivos domóticos (luces, enchufes, etc)
"""

import json
import hashlib
import hmac
import time
import subprocess
from datetime import datetime

class TuyaAPI:
    def __init__(self, client_id, client_secret, endpoint="https://openapi.tuya.com"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.endpoint = endpoint
        self.access_token = None
        self.token_expire = 0
    
    def _sign(self, method, path, body=""):
        """Genera firma HMAC-SHA256 para requests"""
        t = str(int(time.time() * 1000))
        
        if body:
            body_hash = hashlib.sha256(body.encode()).hexdigest()
            sign_str = f"{method}\n{path}\n\n{body_hash}"
        else:
            sign_str = f"{method}\n{path}\n"
        
        sign = hmac.new(
            self.client_secret.encode(),
            sign_str.encode(),
            hashlib.sha256
        ).hexdigest().upper()
        
        # DEBUG
        if path == "/v1.0/token?grant_type=1":
            print(f"DEBUG Sign: t={t}, sign_str={repr(sign_str)}, sign={sign}")
        
        return t, sign
    
    def _request(self, method, path, body="", use_token=False):
        """Ejecuta request HTTP contra Tuya"""
        t, sign = self._sign(method, path, body)
        
        headers = [
            "-H", f"client_id: {self.client_id}",
            "-H", f"t: {t}",
            "-H", f"sign: {sign}",
            "-H", "sign_method: HMAC-SHA256",
            "-H", "Content-Type: application/json"
        ]
        
        if use_token and self.access_token:
            headers.extend(["-H", f"Authorization: Bearer {self.access_token}"])
        
        cmd = ["curl", "-s", "-X", method, f"{self.endpoint}{path}"] + headers
        
        # DEBUG
        if path == "/v1.0/token?grant_type=1":
            print(f"DEBUG curl cmd: {' '.join(cmd[:5])}... headers: {headers}")
        
        if body:
            cmd.extend(["-d", body])
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            if path == "/v1.0/token?grant_type=1":
                print(f"DEBUG curl stdout: {repr(result.stdout[:500])}")
                print(f"DEBUG curl stderr: {repr(result.stderr[:500])}")
                print(f"DEBUG curl returncode: {result.returncode}")
            
            if not result.stdout:
                return {"error": "Empty response from curl"}
            try:
                return json.loads(result.stdout)
            except json.JSONDecodeError:
                print(f"DEBUG: Invalid JSON response: {result.stdout[:500]}")
                return {"error": f"Invalid JSON: {result.stdout[:200]}"}
        except Exception as e:
            return {"error": str(e)}
    
    def get_access_token(self):
        """Obtiene access token de Tuya"""
        path = "/v1.0/token?grant_type=1"
        resp = self._request("GET", path)
        
        if resp.get("success"):
            self.access_token = resp["result"]["access_token"]
            self.token_expire = time.time() + resp["result"]["expire_time"]
            return self.access_token
        else:
            print(f"Error obteniendo token: {resp}")
            return None
    
    def get_devices(self):
        """Lista todos los dispositivos vinculados"""
        if not self.access_token:
            self.get_access_token()
        
        path = "/v2.0/cloud/thing"
        resp = self._request("GET", path, use_token=True)
        
        if resp.get("success"):
            return resp["result"]
        else:
            print(f"Error listando dispositivos: {resp}")
            return None
    
    def control_device(self, device_id, command_code, value):
        """Envía comando a un dispositivo"""
        if not self.access_token:
            self.get_access_token()
        
        path = f"/v1.0/iot-03/devices/{device_id}/commands"
        body = json.dumps({
            "commands": [
                {
                    "code": command_code,
                    "value": value
                }
            ]
        })
        
        resp = self._request("POST", path, body, use_token=True)
        return resp.get("success", False)


if __name__ == "__main__":
    # Cargar credenciales
    with open("/home/pablo/clawd/.tuya-credentials.json") as f:
        creds = json.load(f)
    
    # Crear instancia
    api = TuyaAPI(
        client_id=creds["access_id"],
        client_secret=creds["access_secret"],
        endpoint="https://openapi.tuya.com"  # Western America
    )
    
    print("🔌 Conectando a Tuya...")
    if api.get_access_token():
        print("✓ Token obtenido")
        
        print("\n📱 Listando dispositivos...")
        devices = api.get_devices()
        if devices:
            print(json.dumps(devices, indent=2, ensure_ascii=False))
        else:
            print("No hay dispositivos")
    else:
        print("✗ No se pudo obtener token")
