
  <h3 align="center">DEVNET</h3>

<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" height="80" alt="Linux Logo" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="80" alt="Python Logo" />
  
  <br />
  <h1>🚀 Automatización y Virtualización de Infraestructura</h1>
</div>

## 📋 Script bash automatización de contenedor

1 - Script Bash

```
echo "FROM python" > Dockerfile
echo "RUN apt-get update -y" >> Dockerfile
echo "RUN apt-get install -y python3-pip" >> Dockerfile
echo "RUN pip install flask" >> Dockerfile
echo "COPY index.html /home/myapp/templates/ " >> Dockerfile
echo "COPY server.py /home/myapp/ " >> Dockerfile
echo "EXPOSE 8000 " >> Dockerfile
echo "CMD python3 /home/myapp/server.py" >> Dockerfile

docker build -t app .
docker run -t -d -p 8000:8000 --name app app
docker ps -a
```
2 - Agregar Script de python con Flask (server.py)

```
from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8000)
```
3 - Agregar plantilla html (index.html)

```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Título de la Página</title>
</head>
<body>
    <div class="container">
        <h1>Título de la Página</h1>
        <div class="divider"></div>
        <p class="subtitle">Página web básica con diseño moderno</p>
    </div>
</body>
</html>
```
4 - Realizar despliegue de prueba
```
chmod u+x script.sh
./script.sh
```
---
## 🧠 Configuración de GIT

1 - Configuración
```
git config --global user.name "xxxxxx"
git config --global user.email xxxxxx

git init
git remote add origin https://github.com/xxxxxxxx

git add .
git status
git commit -m "Agregando xxxxxxxxx"

git push origin master
```
---
## 🚀 Integración y Despliegue con Jenkins

1 - Instalación de imagen desde docker
```
docker pull jenkins/jenkins:lts
```

2 - Despliegue de Imagen
```
docker run --rm -u root -p 8080:8080 -v jenkins-data:/var/jenkins_home -v $(which docker):/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock -v "$HOME":/home --name jenkins_server jenkins/jenkins:lts
```

