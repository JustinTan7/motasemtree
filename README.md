# motasemtree
Repo for assignment 1 for motasem's class

### New File Structure
Going forward all the dockerfiles will be in their respective sub directories. When you make the dockerfiles, add the configuration to the `docker-compose.yml.` 
The 'login' directory will contian **ALL** the web app pages, and functionality for them. The `app.py` within 'login' will contain all the functions and routes to go between the web apps. Other services can probably go within their own sub directories.

To build the images, ontainers, and network easily, run:

```
docker compose up --build
```

To easily remove everything besides the images, run:

```
docker compose down -v
```