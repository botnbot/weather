from pprint import pprint
from src.API import get_lat_lon_from_api, get_weather_from_api

def main():
        obj = input("Введите наименование географического объекта ")
        lat, lon = get_lat_lon_from_api(obj)
        if lat and lon:
            weather = get_weather_from_api(lat = float(lat), lon = float(lon))
            if weather:
                pprint(weather)
            else:
                print("Не удалось получить данные о погоде")
        else:
            print("не удалось получить координаты места")
