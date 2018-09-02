import requests
url = 'https://webhook.site/c56e4581-762a-45ca-8185-5e1c4b697462'
for x in range(0, 3):
   r = requests.get(url)
   print(r.headers.get('Date'))
