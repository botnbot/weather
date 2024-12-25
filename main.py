import os
from pprint import pprint

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значений переменных из .env-файла
api_key = os.getenv('API_key')
YOUR_ACCESS_TOKEN = os.getenv('YOUR_ACCESS_TOKEN')

def get_from_api(lat=59.2187, lon=39.8886):
    """Получает информацию о погоде от API"""
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(url)
    if response.status_code != 200: print(f'Ошибка получения ответа от API')
    data = response.json()
    return data.get(0)


def get_lat_lon_api(city):
    """Получает информацию о координатах по адресу"""
    url = f'https://us1.locationiq.com/v1/search?key={YOUR_ACCESS_TOKEN}&format=json&q={city}'
    response = requests.get(url)
    if response.status_code != 200: print(f'Ошибка получения ответа от API')
    data = response.json()
    if data:
        lat = data.get(0)['lat']
        lon = data.get(0)['lon']
    else:
        print('не удалось обнаружить координаты')
        lat = data.get(0)['lat']
        lon = data.get(0)['lon']
    return lat, lon


if __name__ == '__main__':
    obj = input('Введите наименование географического объекта ')
    lat, lon = get_lat_lon_api(obj)
    if lat and lon:
        weather = get_from_api(lat, lon)
    else:
        print('Неизвестный геграфический объект')
        if weather:
            pprint(weather)
        else:
            print('Не удалось получить данные о погоде')

