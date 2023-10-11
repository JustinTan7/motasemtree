# motasemtree
Repo for assignment 1 for motasem's class

## For starting auth_service
cd into the "auth_service" directory

run:
```
docker build -t your-image-name
docker run -p 5002:5002 --name your-container-name your-image-name
or you can just run:
docker compose up
```
However, the port is still 5000 when the app loads up in the container. 
I don't know how because in the `dockerfile`, `docker-compose.yml`, and `app.py`, I HAVE SPECIFIED IT TO BE ON PORT 5002 >:[