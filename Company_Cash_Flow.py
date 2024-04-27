import requests

url = "https://real-time-finance-data.p.rapidapi.com/company-cash-flow"

querystring = {"symbol":"AAPL:NASDAQ","period":"<REQUIRED>","language":"en"}

headers = {
	"X-RapidAPI-Key": "1c3463373cmsh7387f3f89c2b3fbp10b845jsnacee5fc7c035",
	"X-RapidAPI-Host": "real-time-finance-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())