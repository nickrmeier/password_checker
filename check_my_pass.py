import requests

url = 'https://api.pwnedpasswords.com/range/' + '5d414'
res =  requests.get(url)

print(res)
