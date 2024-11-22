import requests

def rates(currency="BTC", rate="USD"):
	response = requests.get(f"https://api.coinbase.com/v2/exchange-rates?currency={currency}").json()
	if response["data"]["rates"].get(f"{rate}") != None:
		msg = f"{currency}/{rate}\n\n🔥{response["data"]["rates"].get(f"{rate}")}$"
		return msg
	else:
		return "Не распознано"	
