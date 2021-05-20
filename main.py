# https://www.youtube.com/watch?v=Gon0MvppfF8&t=245s

import pyowm
import eel

owm = pyowm.OWM('59ff4e66ae7a38fcb9a7a637165a4172')


@eel.expose
def get_weather():
    manager = owm.weather_manager()
    observation = manager.weather_at_place("Анапа, Россия")
    weather = observation.weather
    temp = weather.temperature('celsius')['temp']
    detailed = weather.clouds
    welcome_message = 'Добрый день! Добро пожаловать в Alean Family Resort & Spa Doville! Сегодня 20 мая, четверг. '
    weather_message = f'Погода на сегодня: +{str(round(temp))} C, облачность: {detailed}%'
    schedule_message = '16:00 - Водное поло в бассейне №4 18+, ' \
                       '17:00 - Семейные интерактивные игры 8+, ' \
                       '20:00 - Детская вечерняя программа 8+, ' \
                       '21:00 - Взрослая вечерняя развлекательная программа 18+. '
    return welcome_message


eel.init('web')
eel.start('main.html', size=(1200, 120))

