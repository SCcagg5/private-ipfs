# private-ipfs
```
docker-compose up -d
echo -e "/key/swarm/psk/1.0.0/\n/base16/\n$(tr -dc 'a-f0-9' < /dev/urandom | head -c64)" > data/ipfs/swarm.key
python3 conf.py
docker-compose restart
```
