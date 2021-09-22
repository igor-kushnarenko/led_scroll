import pyowm
import eel

owm = pyowm.OWM('59ff4e66ae7a38fcb9a7a637165a4172')

data = {
    'schedule_message': 'РАСПИСАНИЕ: Мини-диско 19:30 | Награждение 19:50 | '
                        'Детская развлекательная программа "Гарри Поттер" 20:00 | '
                        'Взрослая развлекательная программа "Чародеи" 21:00 | '
                        'Более подробно с расписанием анимационных мероприятий, вы можете ознакомиться '
                        'на информационном стенде при входе в ресторан Нормандия.',
    'welcome_message': 'Добрый день! Добро пожаловать! Сегодня 22 сентября, среда. ',
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
