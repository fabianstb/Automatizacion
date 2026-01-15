echo "FROM python" > Dockerfile
echo "RUN apt-get update -y" >> Dockerfile
echo "RUN apt-get install -y python3-pip" >> Dockerfile
echo "RUN pip install flask" >> Dockerfile
echo "COPY ./static /home/myapp/static/ " >> Dockerfile
echo "COPY index.html /home/myapp/templates/ " >> Dockerfile
echo "COPY server.py /home/myapp/ " >> Dockerfile
echo "EXPOSE 8000 " >> Dockerfile
echo "CMD python3 /home/myapp/server.py" >> Dockerfile

docker build -t app .
docker run -t -d -p 8000:8000 --name app app
docker ps -a