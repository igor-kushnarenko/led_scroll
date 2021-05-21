# https://www.youtube.com/watch?v=Gon0MvppfF8&t=245s

import pyowm
import eel

owm = pyowm.OWM('59ff4e66ae7a38fcb9a7a637165a4172')

data = {
    'schedule_message': 'РАСПИСАНИЕ: 15:00 - Радио "Довиль" | '
                        '16:00 - Водное поло в бассейне №4 (18+) | '
                        '17:00 - Семейные интерактивные игры (8+) | '
                        '20:00 - Детская вечерняя программа (8+) | '
                        '20:30 - Шоу талантов | '
                        'Более подробно с расписанием анимационных мероприятий, вы можете ознакомиться '
                        'на информационном стенде при входе в ресторан Нормандия.',
    'welcome_message': 'Добрый день! Добро пожаловать в Alean Family Resort & Spa Doville! Сегодня 21 мая, пятница. ',
}


@eel.expose
def say_welcome():
    manager = owm.weather_manager()
    observation = manager.weather_at_place("Анапа, Россия")
    weather = observation.weather
    temp = weather.temperature('celsius')['temp']
    detailed = weather.clouds
    weather_message = f'Погода на сегодня: +{str(round(temp))} C, облачность: {detailed}%'
    return f'{data["welcome_message"]} | {weather_message}'


@eel.expose
def say_schedule():
    return data['schedule_message']


eel.init('web')
eel.start('main.html', size=(1200, 120))

