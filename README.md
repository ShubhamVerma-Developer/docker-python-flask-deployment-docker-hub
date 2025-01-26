```
docker build -t {docker-hub-username}/{image-name}:0.0.1.RELEASE .
```
```
docker container run -d -p 3000:3000 {docker-hub-username}/{image-name}:0.0.1.RELEASE
```

```
docker container stop {container-id}
```

```
docker push {docker-hub-username}/{image-name}:0.0.1.RELEASE
```