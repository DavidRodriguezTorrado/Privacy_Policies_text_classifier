"""
This script automatically returns a txt file with apps from play store
given an url
"""
import requests
from bs4 import BeautifulSoup

# CONFIG

# Just define url and name of the file to be dumped
name = 'prueba1.txt'
# Some samples of url
#url = 'https://play.google.com/store/apps/collection/cluster?clp=SkMKNQovcHJvbW90aW9uX2ZhbWlseXNhZmVfZHVtYmxlc3RvcmVfaG9tZV9mcmVlX2FwcHMQShgDEgZGQU1JTFk6AggD:S:ANO1ljIPCiI&gsr=CkVKQwo1Ci9wcm9tb3Rpb25fZmFtaWx5c2FmZV9kdW1ibGVzdG9yZV9ob21lX2ZyZWVfYXBwcxBKGAMSBkZBTUlMWToCCAM%3D:S:ANO1ljL_MUU&hl=es&gl=US'
url = 'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcGdyb3NzaW5nX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljLe6QA&gsr=CiLSDh8KHQoXdG9wZ3Jvc3NpbmdfQVBQTElDQVRJT04QBxgD:S:ANO1ljKx5Ik&hl=es&gl=US'
#url = 'https://play.google.com/store/apps/collection/cluster?clp=ogooCAEaHAoWcmVjc190b3BpY191Y0lGYUVUUmVTMBA7GAMqAggBUgIIAg%3D%3D:S:ANO1ljKEE0E&gsr=CiuiCigIARocChZyZWNzX3RvcGljX3VjSUZhRVRSZVMwEDsYAyoCCAFSAggC:S:ANO1ljJcKlg&hl=es&gl=US'
#url = 'https://play.google.com/store/apps/collection/cluster?clp=ogoSCAESBkZBTUlMWSoCCANSAggB:S:ANO1ljL4ljc&gsr=ChWiChIIARIGRkFNSUxZKgIIA1ICCAE%3D:S:ANO1ljJuJgY&hl=es&gl=US'


f = open('./top_100_apps.txt', 'r')
test_list = f.readlines()
f.close()
print(test_list)

# CODE

# We get the content of the page parsed on BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
res = requests.get(url, headers)
soup = BeautifulSoup(res.content, 'html.parser')

# The apk package names are on the hrefs of the links of the titles of the apks
links = soup.find_all('a')
# The string that identifies a link as an apk link
key = '/store/apps/details?id='
# We get the apk links
apks = []
for link in links:
    if key in link.get('href'):
        # We extract the package name from the href and add a line jump for the file
        apks.append(link.get('href').replace(key, '') + '\n')
# Remove duplicates
apks = list(dict.fromkeys(apks))

final_list = [x for x in apks if x not in test_list]
print(final_list)

# We dump our list into a txt file with the name we indicated before
f = open(name, 'w', encoding='utf-8')
f.writelines(final_list)
f.close()