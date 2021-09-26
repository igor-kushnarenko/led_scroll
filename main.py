import pyowm
import eel

from scripts.parser import get_weekday_date, get_show

owm = pyowm.OWM('59ff4e66ae7a38fcb9a7a637165a4172')

data = {
    'schedule_message': f'РАСПИСАНИЕ: Детская программа "{get_show()[0]}" - 20:00, '
                        f'Взрослая вечерняя программа "{get_show()[1]}" - 21:00.',
    'stand': 'Более подробно с расписанием анимационных мероприятий, вы можете ознакомиться '
             'на информационном стенде при входе в ресторан Нормандия',
    'welcome_message': 'Добро пожаловать!',
    'weekday_and_date': get_weekday_date()
}


@eel.expose
def say_welcome():
    manager = owm.weather_manager()
    observation = manager.weather_at_place("Анапа, Россия")
    weather = observation.weather
    temp = weather.temperature('celsius')['temp']
    detailed = weather.clouds
    weather_message = f'Погода: +{str(round(temp))} C, облачность: {detailed}%'
    return f'{data["welcome_message"]} {data["weekday_and_date"]} | {weather_message}'


@eel.expose
def say_schedule():
    return f'{data["schedule_message"]} {data["stand"]}'


eel.init('web')
eel.start('main.html', size=(1200, 120))
