# Docker Commands Reference

## Images
```bash
docker pull nginx
docker images
docker build -t myapp:1.0 .
docker rmi myapp:1.0
```

## Containers
```bash
docker run -d -p 8080:80 nginx
docker run -it ubuntu bash
docker ps
docker ps -a
docker stop <id>
docker rm <id>
docker logs <id>
docker exec -it <id> bash
```

## Docker Compose
```bash
docker-compose up -d
docker-compose down
docker-compose logs -f
docker-compose ps
```
