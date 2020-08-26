import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

#from urllib import request, parse, error

# import urllib.request

print("hello")
url = "https://todoscontraocorona.net.br/"
html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')
str = html.decode("utf-8")
# print(str)
# print(type(soup))
# print(soup.get_text())

# print(soup)

#Retrieve all of the anchor tags
# tags = soup('script')
# for tag in tags:
#     print(tag)

# text = re.findall("""{
#   "id": "Aracaju",
#   "title": "Aracaju",
#   "id_no_spaces": "Aracaju",
#   "status": "1",
#   "status_text": "Enabled",
#   "link": "",
#   "confirmados": "\w+",
#   "obitos": "\w+",
#   "letalidade": "\w",
#   "incidencia": "\w",
#   "mortalidade": "\w",
#   "isolamento_social": "38%"
# }""",soup)

# text= re.findall(
# 	'''{
#   "id": "Aracaju",
#   "title": "Aracaju",
#   "id_no_spaces": "Aracaju",
#   "status": "1",
#   "status_text": "Enabled",
#   "link": "",
#   "confirmados": "\w+",
#   "obitos": "\w+",
#   "letalidade": "\w",
#   "incidencia": "\w",
#   "mortalidade": "\w",
#   "isolamento_social": "38%"
# }'''

# 	,str)

import json

text = re.findall('{"id":"Aracaju","title":"Aracaju","id_no_spaces":"Aracaju","status":"1","status_text":"Enabled","link":"","confirmados":"'r"\w+"'","obitos":"'r"\w+"'","letalidade":"'r"\w+"'","incidencia":"'r"\w+,\w+"'","mortalidade":"'r"\w+,\w+"'","isolamento_social":"'r"\w+%\"\}",str)

res = json.loads(text[0])
# txt = '{"name":1}'
# res = json.loads(txt)
# print(res)
# print(text[0],type(text[0]))
print(res,type(res))

print()