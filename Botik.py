import requests


bot_token = '706178131:AAGPw9ekQgHSbNSSkYbw5mH5pSyaOZ3wdnY'
tel_api_url = "https://api.telegram.org/bot{}/"
methods = {'updates': 'GetUpdates'}


class mybot:


    def __init__(self, bot_token = None) :

        self.bot_token = bot_token


    def get_updates():
        res = requests.get(tel_api_url.format(bot_token) + methods['updates'])
        return res.json()

    print(get_updates())
    last_update_id = 0  
    
    

    def get_message_text():
    #Получать сообщения только от новых обновлений
    #Получать Update каджого обновления и записывать его в переменную
    #А затем сравнивать ее с Up_Date последнего сообщения

        data = get_updates()
        last_objekt = data['result'][-1]
        update_id = last_objekt['update_id']
        last_update_id
        if update_id != last_update_id:
            last_update_id = update_id

            text_answer = data['result'][-1]['message']['text']
            chat_id = data['result'][-1]['message']['chat']['id']
            message = {'chat_id': chat_id, 'text': text_answer}
        return message
        return None
    


    def send_message(chat_id, text_answer= 'Pogodi minyty'):
       url = tel_api_url.format(bot_token) + 'sendmessage?chat_id={}&text={}'.format(chat_id, text_answer)
       requests.get(url)
    

    def get_kyrs_usd():
        url_usd = 'http://www.nbrb.by/API/ExRates/Rates/145'
        price_usd = requests.get(url_usd).json()
        status_usd = requests.get(url_usd)
        kyrs_usd = price_usd['Cur_OfficialRate']
        print({'Курс Доллара' : kyrs_usd})
        if status_usd != 200:
            print('Не могу подлючится')
        return kyrs_usd 



    def get_kyrs_ryb():
        url_ryb = ('http://www.nbrb.by/API/ExRates/Rates/298')
        price_ryb = requests.get(url_ryb).json()
        kyrs_ryb = price_ryb['Cur_OfficialRate']
        print({'Курс россии': kyrs_ryb})
        return kyrs_ryb
  
   
    print(get_kyrs_ryb())

    def oldmes(mes):
        text_mes = data['result']['{}']['message']['text'].format(mes)    
        return text_mes

    def main():
        while True:
            answer = get_message_text()
            if answer != None:
                chat_id = answer['chat_id']
                text = answer['text']
                if text == '/usd' :
                    send_message(chat_id, get_kyrs_usd())
                if text == '/ryb':
                    send_message(chat_id, get_kyrs_ryb())
                if text == '-5':
                    send_message(shat_id, oldmes())
            else:
                continue
        
                
  

    main()
