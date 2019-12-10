import json
import os

MY_IP="51.91.252.29"

f=open("data/ipfs0/config", "r")
contents =f.read()
f.close()
data = json.loads(contents)
peer = data["Identity"]["PeerID"]
data["Bootstrap"] = ["/ip4/"+MY_IP+"/tcp/4001/ipfs/" + peer]
f = open("data/ipfs0/config","w+")
f.write(json.dumps(data, sort_keys=True, indent=4))
f.close()
