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
    return f'Погода на сегодня: {str(round(temp))} C, облачность: {detailed}% '


eel.init('web')
eel.start('main.html', size=(1200, 120))

