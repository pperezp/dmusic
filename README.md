# dmusic
## Linux
### Build
```bash
docker build -t dmusic .
```

### Run
```bash
docker run -d -it --name dmusic -v $HOME/dmusic/music:/home/dmusic/music -v $HOME/dmusic/download.music:/home/dmusic/download.music dmusic
```

## Mac
### Build
```bash
docker build --platform linux/amd64 -t dmusic .
```

### Run
```bash
docker run -d -it --name dmusic -v $HOME/dmusic/music:/home/dmusic/music -v $HOME/dmusic/download.music:/home/dmusic/download.music --platform linux/amd64 dmusic
```

## Enter to container
```bash
docker exec -it dmusic /bin/bash
```

## Log container
```bash
docker logs dmusic
```

## Eliminar el container dmusic
```bash
docker rm -f dmusic
```