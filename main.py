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
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f'Ошибка получения данных от OpenWeather API: {e}')
    except ValueError:
        print('Ошибка обработки JSON ответа о погоде')


def get_lat_lon_api(city):
    """Получает информацию о координатах по адресу"""
    url = f'https://us1.locationiq.com/v1/search?key={YOUR_ACCESS_TOKEN}&format=json&q={city}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data:
                lat = data[0].get('lat', 50)
                lon = data[0].get('lon', 40)
                if lat and lon:
                    return lat, lon
        else:
                print('не удалось обнаружить координаты')
                return None, None
    except requests.exceptions.RequestException as e:
        print(f'Ошибка получения координат от API: {e}')
        return None, None
    except ValueError:
        print('Ошибка обработки JSON данных из LocationIQ API.')
        return None, None



if __name__ == '__main__':
    obj = input('Введите наименование географического объекта ')
    lat, lon = get_lat_lon_api(obj)
    if lat and lon:
        weather = get_from_api(lat, lon)
        if weather:
            pprint(weather)
        else:
            print('Не удалось получить данные о погоде')
    else:
        print('Неизвестный геграфический объект')



