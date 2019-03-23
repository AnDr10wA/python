

from flask import Flask
#from flask_sslify import SSLify
from flask import request
from flask import jsonify
import requests
import json
from lxml import html

app = Flask(__name__)


bot_token = '637785423:AAFeE-YqiMuu6MS17C7IzxwDXglya-hgInc'
tel_api_url = "https://api.telegram.org/bot{}/"
methods = {'updates': 'GetUpdates'}

URL = 'https://api.telegram.org/bot637785423:AAFeE-YqiMuu6MS17C7IzxwDXglya-hgInc/'

#sslify = SSLify(app)



#https://api.telegram.org/bot637785423:AAFeE-YqiMuu6MS17C7IzxwDXglya-hgInc/setWebhook?url=https://3d81eb4e.ngrok.io/



def write_json(data, filename='answer.json'):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=2, ensure_ascii=False)


def send_message(chat_id, text = 'Pogodi minyty'):
	url = tel_api_url.format(bot_token) + 'sendmessage'
	answer = {'chat_id': chat_id, 'text' : text}
	r = requests.post(url, json=answer)
	return r.json()

def get_kyrs_usd():
	url_usd = 'http://www.nbrb.by/API/ExRates/Rates/145'
	price_usd = requests.get(url_usd).json()
	kyrs_usd = price_usd['Cur_OfficialRate']
	url_ryb = ('http://www.nbrb.by/API/ExRates/Rates/298')
	price_ryb = requests.get(url_ryb).json()
	kyrs_ryb = price_ryb['Cur_OfficialRate']
	url_eur = ('http://www.nbrb.by/API/ExRates/Rates/978?ParamMode=1')
	price_eur = requests.get(url_eur).json()
	kyrs_eur = price_eur['Cur_OfficialRate']
	url_jpy = ('http://www.nbrb.by/API/ExRates/Rates/392?ParamMode=1')
	price_jpy = requests.get(url_jpy).json()
	kyrs_jpy = price_jpy['Cur_OfficialRate']
	url_chf = ('http://www.nbrb.by/API/ExRates/Rates/130')
	price_chf = requests.get(url_chf).json()
	kyrs_chf = price_chf['Cur_OfficialRate']	
	
	prise = 'Доллар {}, Российский рубль {} Евро {} Иена {} Шфейцарский франк{}'.format(kyrs_usd, kyrs_ryb, kyrs_eur, kyrs_jpy, kyrs_chf)

	return prise

def url_pogoda():
	res = requests.get('https://api.openweathermap.org/data/2.5/forecast?q=Minsk&appid=e891e170e3cfa3e5cac77e6f59ecd9b3')
	return res.json()
def pogoda():

	data = url_pogoda()
	last_objekt = data['list'][0]

    
	temp = last_objekt['main']['temp']
	temp_min = last_objekt['main']['temp_min']
	temp_max = last_objekt['main']['temp_max']
	weather = last_objekt['weather'][0]['main']
	wind = last_objekt['wind']['speed']
	humidity = last_objekt['main']['humidity']
	sea_level = last_objekt['main']['sea_level']
	pressure = last_objekt['main']['pressure']
	pogoda = 'Температура воздуха {} Минимальная Температура {} Максимальная температура {} Погода {} Ветер {} Влажность {} Уровень моря {} Давление{}'.format(temp, temp_min,
		temp_max, weather, wind, humidity, sea_level, pressure)
	
	return pogoda

def afisha():


	movies_params = {
		'url':'https://afisha.tut.by/film/', 
		'current_events':'//div[@id="events-block"]',
		'events_list':'ul[@class="b-lists list_afisha col-5"]', 
		'film_name':'.//a[@class="name"]/span//text()',
		}

	tree = html.fromstring(requests.get(movies_params['url']).text)

	current_events = tree.xpath(movies_params['current_events'])[0]
	events_list = current_events.xpath(movies_params['events_list'])


	def create_movies_list():
		movies_list = []

		for movies_block in events_list:

			for movie in movies_block:

				movies_list += [movie.xpath(movies_params['film_name'])[0]]

		movies = '_'.join(movies_list)
		return movies
	return create_movies_list()

@app.route('/', methods=['POST', 'GET'])




def index():
	if request.method == 'POST':
		r = request.get_json()
		chat_id = r['message']['chat']['id']
		message = r['message']['text']
		if 'кино' in message:
			send_message(chat_id, text=afisha())
		if 'деньги' in message:
			send_message(chat_id, text=get_kyrs_usd())
		if 'погода' in message:
			send_message(chat_id, text=pogoda())

		#write_json(r)
		return jsonify(r)


	return '<hi> Bot WebHook</h1>'



if __name__ == '__main__':
	
	app.run()



