import requests
from api_key import API_KEY1

def get_weather(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "ru"
    }
    
    try:
        response = requests.get(url, params=params, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            return {
                "город": data["name"],
                "температура": f"{data['main']['temp']}°C",
                "описание": data["weather"][0]["description"],
                "влажность": f"{data['main']['humidity']}%",
                "ветер": f"{data['wind']['speed']} м/с"
            }
        elif response.status_code == 401:
            return {"ошибка": "Неверный API-ключ"}
        elif response.status_code == 404:
            return {"ошибка": f"Город '{city}' не найден"}
        else:
            return {"ошибка": f"Ошибка HTTP {response.status_code}"}
            
    except requests.exceptions.Timeout:
        return {"ошибка": "Таймаут 5 секунд"}
    except requests.exceptions.ConnectionError:
        return {"ошибка": "Нет подключения к интернету"}
    except Exception as e:
        return {"ошибка": str(e)}
API_KEY = API_KEY1
    
print("Тестируем get_weather()...")
    
# Тест 1: Существующий город
result = get_weather("Moscow", API_KEY)
print("Город Москва:", result)
    
# Тест 2: Несуществующий город
result = get_weather("MPT", API_KEY)
print("Неверный город:", result)