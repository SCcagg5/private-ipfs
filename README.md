# private-ipfs
```
docker-compose up -d
echo -e "/key/swarm/psk/1.0.0/\n/base16/\n$(tr -dc 'a-f0-9' < /dev/urandom | head -c64)" > swarm.key
python3 conf.py
cp swarm.key ./data/ipfs0
cp swarm.key ./data/ipfs1
cp swarm.key ./data/ipfs2
docker-compose restart
```
