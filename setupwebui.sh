version=$(curl localhost:5001/webui/ -q  | cut -d/ -f3 | cut -d\" -f1);
url='https://ipfs.io/api/v0/get/'$version;
curl $url | tar -xf - ;
mv $version ./ipfsA/
docker-compose exec ipfsA ipfs add -r /data/ipfs/$version
docker-compose exec ipfsA ipfs config --json API.HTTPHeaders.Access-Control-Allow-Origin '["*"]'
docker-compose exec ipfsA ipfs config --json API.HTTPHeaders.Access-Control-Allow-Methods '["PUT", "GET", "POST"]'
