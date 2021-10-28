from facebook_scraper import get_posts
import numpy as np
import time
import json
import datetime

data = {}
data['ChickenLandAQP'] = []

def keyCheck(key, arr, default):
  if arr is None:
    return default
  else:
    if key in arr.keys():
      return arr[key]
    else:
      return default

for post in get_posts('ChickenLandAQP', cookies="cookies.json", pages=55, extra_info=True, options={"comments": True, "reactions": True}):
  data['ChickenLandAQP'].append({
    'url': post['post_url'],
    'date_post': '' if post['time'] is None else post['time'].isoformat(),
    'text': post['text'],
    'shares': post['shares'],
    'like': keyCheck('me gusta', post['reactions'], 0),
    'love': keyCheck('me encanta', post['reactions'], 0),
    'haha': keyCheck('me divierte', post['reactions'], 0),
    'care': keyCheck('me importa', post['reactions'], 0),
    'wow': keyCheck('me asombra', post['reactions'], 0),
    'sad': keyCheck('me entristece', post['reactions'], 0),
    'angry': keyCheck('me enfada', post['reactions'], 0),
    'video': post['video'],
    'image': post['image'],
    'gallery': post['images']
  })
  time.sleep(np.round(np.random.uniform(1.5, 3.5),2))

with open('data.json', 'w') as file:
  json.dump(data, file, indent=2)