import requests

class Horoscopeinputs:
    def __init__(self):
        pass

    @staticmethod
    def checkhoroscope(fn):
        def wrapper(self):
            result = fn(self)
            if isinstance(result, str):
                r = requests.get(f"https://ohmanda.com/api/horoscope/{result.lower()}")
                return r
            elif isinstance(result, tuple) and len(result) == 2:
                sign1 = result[0]
                sign2 = result[1]
                r = requests.get(f"https://json.astrologyapi.com/v1/zodiac_compatibility/:{sign1.lower()}/:{sign2.lower()}")
                return r
            
        return wrapper 
    

    @checkhoroscope
    def checksign(self):
        sign = str(input(f"Please Enter your Astrology Sign"))
        return sign
    
    @checkhoroscope
    def checkcompatibility(self):
        sign1 = str(input(f"Please Enter the first Astrology Sign: "))
        print(f"First Sign is {sign1}")
        sign2 = str(input(f"Please Enter the second Astrology Sign: "))
        print(f"Second Sign is {sign2}")
        return sign1, sign2 
    
    def logic(self):
        print("Welcome to the Horoscope Engine")
        print("Please choose one of the options available: ")
        print("1. Your horoscope details today")
        print("2. Compatibility Horoscope")
        choice = int(input(f"Choice: "))
        if choice == 1:
            detail = self.checksign()
            data = detail.json()
            print(data["horoscope"])

        elif choice == 2:
            detail = self.checkcompatibility()
            print(detail.json())
            data = detail.json()

output = Horoscopeinputs()
output.logic()

