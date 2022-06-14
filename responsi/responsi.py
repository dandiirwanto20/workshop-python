import json
from urllib import request

url = "https://dekontaminasi.com/api/id/covid19/hospitals"

response = request.urlopen(url)

data = json.loads(response.read())

for post in data:
    print(f"- Nama Rumah Sakit: {post['name']}")
    print(f"- Provinsi: {post['province']}")
    print(f"- Alamat: {post['address']}")
    print("")