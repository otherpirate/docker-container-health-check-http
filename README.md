# docker-container-health-check-http
Simple HTTP health-check for containers in same host

# How to use


```
git clone https://github.com/otherpirate/docker-cotainer-health-check-http.git
cd docker-cotainer-health-check-http
docker build -t http-hc .
docker run --name=http-hc -d -v /var/run/docker.sock:/var/run/docker.sock -p 5000:5000 http-hc:latest

curl http://127.0.0.1:5000/health-check/
### curl http://127.0.0.1:5000/<CONTAINER_ID_OR_NAME>/health-check/
curl http://127.0.0.1:5000/http-hc/health-check/
### curl http://127.0.0.1:5000/<CONTAINER_ID_OR_NAME>/info/
curl http://127.0.0.1:5000/http-hc/info/
```

