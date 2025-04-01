import requests
def get_weather (city):
    params={
         '?0':'',
        'lang':'en',
         '?M':'',
    }
    weather=requests.get(f'https://wttr.in/{city}',params=params)
    print (weather.text)
get_weather('lipitski')