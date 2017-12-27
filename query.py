import random

def query(search): 
	url_list = []
	items = client.gallery_search(search) # Searches Imgur for all the items with the query
	i = 0
	for item in items: 
		url_list.append(item.link)
		i = i + 1
	img = random.choice(url_list)
	return img
	