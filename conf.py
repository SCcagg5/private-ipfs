import json

MY_IP="51.91.252.29"

f=open("data/ipfs/config", "r")
contents =f.read()
f.close()
data = json.loads(contents)
peer = data["Identity"]["PeerID"]
print(peer)
data["API"] = {"HTTPHeaders": {
  "Access-Control-Allow-Methods": [
    "PUT",
    "GET",
    "POST"
  ],
 "Access-Control-Allow-Origin": [
    "http://"+MY_IP+":5001",
    "http://127.0.0.1:5001",
    "https://webui.ipfs.io"
  ]
  }
}
data["Bootstrap"] = ["/ip4/"+MY_IP+"/tcp/4001/ipfs/" + peer]
f = open("data/ipfs/config","w+")
f.write(json.dumps(data, sort_keys=True, indent=4))
f.close()

