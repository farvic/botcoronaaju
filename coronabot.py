import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import json

def data_web_scraping():
	url = "https://todoscontraocorona.net.br/"
	html = urllib.request.urlopen(url).read()
	# soup = BeautifulSoup(html, 'html.parser')
	str = html.decode("utf-8")

	text = re.findall('{"id":"Aracaju","title":"Aracaju","id_no_spaces":"Aracaju","status":"1","status_text":"Enabled","link":"","confirmados":"'r"\w+"'","obitos":"'r"\w+"'","letalidade":"'r"\w+"'","incidencia":"'r"\w+,\w+"'","mortalidade":"'r"\w+,\w+"'","isolamento_social":"'r"\w+%\"\}",str)

	res = json.loads(text[0])

	return res['confirmados'],res['obitos'],res['isolamento_social']


# def main():
#     api = create_api()
#     while True:
#         follow_followers(api)
#         logger.info("Waiting...")
#         time.sleep(60)

# if __name__ == "__main__":
#     main()