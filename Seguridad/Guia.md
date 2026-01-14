  <h3 align="center">DEVNET</h3>

<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" height="80" alt="Linux Logo" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="80" alt="Python Logo" />
  
  <br />

  <h1>🚀 Automatización y Virtualización de Infraestructura</h1>
</div>
---

## 📋 Script administración de cuentas en texto plano

1 - Ejecución de script

```
python3 Pass_plano.py
```
* Desde otra terminal crear cuenta de usuario admin
```
curl -k -X POST https://localhost:5000/signup/v1   -d "username=admin"   -d "password=password123" 
```
* Para validar cuenta de usuario
```
curl -k -X POST https://localhost:5000/login/v1 -d "username=admin" -d "password=password123" 
```

---

## 📋 Script administración de cuentas con password cifrada

2 - Ejecución de script

```
python3 Pass_hash.py
```
* Desde otra terminal crear cuenta de usuario admin
```
curl -k -X POST https://localhost:5000/signup/v2   -d "username=adminhash"   -d "password=password123
```
* Para validar cuenta de usuario
```
curl -k -X POST https://localhost:5000/login/v2   -d "username=adminhash"   -d "password=password123"
```
---
## 🚀 Verificación en Base de datos

3 - Instalación de sqlite
```
apt install sqlite3
```
```
sqlite3 test.db
sqlite> SELECT * FROM USER_PLAIN;
admin|password123

sqlite> SELECT * FROM USER_HASH;
adminhash|ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
```
