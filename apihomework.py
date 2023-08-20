import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
names_of_characters = ["Hulk", "Captain America", "Thanos"]
intelligence = {}

if response.status_code == 200:
    for character in response.json():
        if character['name'] in names_of_characters:
            intelligence[character['name']] = character['powerstats']['intelligence']
    print(max(intelligence, key=intelligence.get))
else:
    print("Ошибочка вышла")