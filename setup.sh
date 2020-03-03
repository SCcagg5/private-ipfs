echo -e "/key/swarm/psk/1.0.0/\n/base16/\n$(tr -dc 'a-f0-9' < /dev/urandom | head -c64)" > swarm.key
mkdir ipfsA ipfsB ipfsC
tee ipfsA/swarm.key ipfsB/swarm.key ipfsC/swarm.key <  swarm.key
docker-compose up -d ipfsA ipfsB ipfsC
docker-compose up -d clusterA clusterB clusterC

