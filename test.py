from imgurpython import ImgurClient
import os
import random
client_token = os.environ.get('DISCORD_TOKEN')
imgur_id = os.environ.get('IMGUR_ID')
imgur_secret = os.environ.get('IMGUR_SECRET')
client = ImgurClient(imgur_id, imgur_secret)
i = 0
url_list = []
items = client.gallery()
for item in items:
		url_list.append(item.link) 
		i = i + 1
x = random.choice(url_list)
print(x)
