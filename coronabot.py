import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import json

# def data_web_scraping():
url = "https://todoscontraocorona.net.br/"
html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')
htmlUTF = html.decode("utf-8")

def sergipe_uti_enf():
	# Encontra o total e porcentagem de ocupação das utis públicas
									   
	totalUtiPublicoLinha = re.findall('<td style="width: 9.22056%; text-align: center;"><span style="color: #ffffff;">'r"\w+"'</span></td>',htmlUTF)
									 # ('<td style="width: 9.22056%; text-align: center;"><span style="color: #ffffff;">192</span></td>
	totalUtiPublico = re.findall(r"\d+",totalUtiPublicoLinha[0])[-1]

	#linhaPorcentagemUTIPublico = re.findall('<td class="'r"\w+"'" style="width: 11.5256%; text-align: center;" align="right"><span style="color: #ffffff;">'r"(\w+,?\w+?%)"'</span></td>',htmlUTF)
	linhaUTIPublicoOcupado = re.findall('<td style="height: 15pt; width: 21.3769%; text-align: center;" align="right" height="20"><span style="color: #ffffff;">'r"\w+"'</span></td>',htmlUTF)
	# utiPublico = re.findall(r"(\w+,?\w+?%)",linhaUTIPublicoOcupado[0])[0]
	soup = BeautifulSoup(linhaUTIPublicoOcupado[0],'html.parser')
	utiPublico = soup.findAll("span")[0].string
	# utiPublico = re.findall(r"(\d+)",linhaUTIPublicoOcupado[0])

	#Encontra o total e porcentagem de ocupação das utis privadas
	totalUtiPrivadoLinha = re.findall('<td style="width: 12.5583%; text-align: center; height: 24px;"><span style="color: #ffffff;">'r"\w+"'</span></td>',htmlUTF)
	totalUtiPrivado = re.findall(r"\d+",totalUtiPrivadoLinha[0])[-1]
	#linhaPorcentagemUTIPrivado = re.findall('<td class="xl66" style="width: 6.27915%; height: 24px; text-align: center;" align="right"><span style="color: #ffffff;">'r"(\w+,?\w+?%)"'</span></td>',htmlUTF)
	linhaUTIPrivadoOcupado = re.findall('<td style="width: 6.27915%; text-align: center;"><span style="color: #ffffff;">'r"\w+"'</span></td>',htmlUTF)
	soup = BeautifulSoup(linhaUTIPrivadoOcupado[1],'html.parser')
	# print(linhaUTIPrivadoOcupado)
	# utiPrivado = re.findall(r"(\w+,?\w+?%)",linhaUTIPrivadoOcupado[0])
	utiPrivado = soup.findAll("span")[0].string


	#Enfermarias públicas
	totalEnfPublicoLinha = re.findall('<td style="width: 9.22056%; text-align: center; height: 24px;"><span style="color: #ffffff;">'r"\w+"'</span></td>',htmlUTF)
	totalEnfPublico = re.findall(r"\d+",totalEnfPublicoLinha[0])[-1]

	# linhaPorcentagemEnfPublico = re.findall('<td style="width: 11.5256%; height: 24px; text-align: center;"><span style="color: #ffffff;">'r"(\w+,?\w+?%)"'</span></td>',htmlUTF)
	linhaEnfPublicoOcupado = re.findall('<td style="width: 21.3769%; height: 24px; text-align: center;"><span style="color: #ffffff;">'r"\w+"'</span></td>',htmlUTF)
	# enfPublico = re.findall(r"(\w+,?\w+?%)",linhaPorcentagemEnfPublico[0])[0]
	soup = BeautifulSoup(linhaEnfPublicoOcupado[0],'html.parser')
	enfPublicoOcupado = soup.findAll("span")[0].string

	# print(totalEnfPublico,enfPublico)

	#Enfermarias Privadas
	totalEnfPrivadoLinha = re.findall('<td style="width: 25.1166%; text-align: center;"><span style="color: #ffffff;">'r"\w+"'</span></td>',htmlUTF)
	totalEnfPrivado = re.findall(r"\d+",totalEnfPrivadoLinha[0])[-1]
	# linhaPorcentagemEnfPrivado = re.findall('<td style="width: 24.2424%; text-align: center;"><span style="color: #ffffff;">'r"(\w+,?\w+?%)"'</span></td>',htmlUTF)
	linhaEnfPrivadoOcupado = re.findall('<td style="width: 12.9954%; text-align: center;"><span style="color: #ffffff;">'r"\w+"'</span></td>',htmlUTF)
	# enfPrivado = re.findall(r"(\w+,?\w+?%)",linhaPorcentagemEnfPrivado[0])[0]
	soup = BeautifulSoup(linhaEnfPrivadoOcupado[1],'html.parser')
	enfPrivadoOcupado = soup.findAll("span")[0].string


	# print(totalEnfPrivado,enfPrivado)

	print(f'''Dados UTIs e Enfermarias em Sergipe: Total(ocupados %)

	UTI
	Pública: {totalUtiPublico} ({utiPublico})
	Privado: {totalUtiPrivado} ({utiPrivado})

	Enfermaria:
	Pública: {totalEnfPublico} ({enfPublicoOcupado})
	Privada: {totalEnfPrivado} ({enfPrivadoOcupado})
	''')

sergipe_uti_enf()

# with open('videos.csv', 'w', newline='') as csv_file:
#         fieldnames = ["Numero", "Titulo", "Views"]
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         writer.writeheader()

# text = re.findall('{"id":"Aracaju","title":"Aracaju","id_no_spaces":"Aracaju","status":"1","status_text":"Enabled","link":"","confirmados":"'r"\w+"'","obitos":"'r"\w+"'","letalidade":"'r"\w+[,\w+]?"'","incidencia":"'r"\w+,?\w+"'","mortalidade":"'r"\w+,\w+"'","isolamento_social":"'r"\w+%\"\}",str)
# res = json.loads(text[0])

# print(res['confirmados'],res['obitos'],res['isolamento_social'])

# print(f'''Coronavírus em Aracaju

# Casos confirmados: {res['confirmados']}
# Número de óbitos: {res['obitos']}
# Isolamento Social: {res['isolamento_social']}

# Fique em casa se puder. A luta contra o vírus ainda não acabou!''')



# def main():
#     api = create_api()
#     while True:
#         follow_followers(api)
#         logger.info("Waiting...")
#         time.sleep(60)

# if __name__ == "__main__":
#     main()