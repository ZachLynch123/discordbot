import random
import os
from imgurpython import ImgurClient

imgur_id = os.environ.get('IMGUR_ID')
imgur_secret = os.environ.get('IMGUR_SECRET')
imgur = ImgurClient(imgur_id, imgur_secret)





url_list = []
i = 0
items = imgur.gallery()
for item in items: 
	url_list.append(item.link)
	i = i + 1
imglink = random.choice(url_list)
print(imglink)