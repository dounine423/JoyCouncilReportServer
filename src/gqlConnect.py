import requests

url = 'https://joystream.yyagi.cloud/graphql'

def gqlQuery(query):
    headers = {'Accept-Encoding': 'gzip, deflate, br', 'Content-Type': 'application/json',
           'Accept': 'application/json',  'Connection': 'keep-alive', 'DNT': '1',
                   'Origin': 'https://query.joystream.org' }
    res=requests.post(url=url,headers=headers,json=query)
    return res.json()['data']