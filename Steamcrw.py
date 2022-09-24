import requests
from lxml.html import fromstring

def cortalinha():
    print('#' * 40)

#Inserção da URLSteam do jogo a ser procurado
urlsteam = 'https://store.steampowered.com/app/1811260/EA_SPORTS_FIFA_23/?l=brazilian'
response = requests.get(urlsteam)
root = fromstring(response.content)

#extração do nome do jogo
pathnm = root.xpath('//div[@class="apphub_AppName"]')
nomejogo = pathnm[1].text

#extração do lançamento do jogo
pathlanc = root.xpath('//div[@class="date"]')
datajogo = pathlanc[0].text

#extração da descrição do jogo
pathdesc = root.xpath('//div[@class="game_description_snippet"]')
descricaojogo = pathdesc[0].text

#extração do menor valor ativo
pathvl = root.xpath('//div[@class="game_purchase_price price"]')
valorjogo = pathvl[0].text

## apresentação dos resultados finais
cortalinha()
print(f'Central de informações:')
cortalinha()
print(f'Jogo Selecionado: {nomejogo}')
print(f'A partir de: {valorjogo.strip()}')
print(f'Data Lançamento: {datajogo}')
print(f'Descrição: {descricaojogo.strip()}')
cortalinha()


