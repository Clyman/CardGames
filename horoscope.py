import requests

def checkhoroscope(sign):
    title = sign.capitalize()
    print(f"Your sign is {title}")
    r = requests.get(f"https://ohmanda.com/api/horoscope/{sign.lower()}")
    return r

sign = input("Please input your horoscope: ")
payloadjson = checkhoroscope(sign).json()
date = payloadjson["date"]
text = payloadjson["horoscope"]

print(f"Date Today : {date}")
print(f"Today's Horoscope : {text}")
