
import requests,json,time

from boltiot import Bolt
import bolt_conf

buzzer=Bolt(bolt_conf.bolt_api_key,bolt_conf.device_id)

set_price=9164.62

def get_bitcoin_price():
	
	try:
		URL="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
		response=requests.request("GET",URL)
		response=json.loads(response.text)
		current_price=response["USD"]
		return current_price

	except Exception as e:
		print("Some error while connecting...")
		print(e)
		return -999 

def send_message(message):
	
	url = "https://api.telegram.org/" + bolt_conf.telegram_bot_id + "/sendMessage"
	data = {
        "chat_id": bolt_conf.telegram_chat_id,
        "text": message
    }
	try:
		response=requests.request("POST",url,params=data)
		print("Telegram Response from request:",response.text)
		telegram_response=json.loads(response.text)
		return telegram_response["ok"]
	except Exception as e:
		print("An error occured in sending price alert")
		print(e)
		return False

while True:
	
	if get_bitcoin_price() != set_price:
		
		message="Alert ! Price changed to: "+str(get_bitcoin_price())
		bit_amu_bot=send_message(message)
		print(bit_amu_bot)
		for i in range(1,10):
			if i%2==0:
				buzz_active=buzzer.digitalWrite("0","HIGH")
			else:
				buzz_active=buzzer.digitalWrite("0","LOW")
	time.sleep(30)

		





