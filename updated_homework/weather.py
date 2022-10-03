import requests

city=input('Введите название города на английском языке: ')

url='http://wttr.in/{}'.format(city)
res=requests.get(url)
print(res.text)