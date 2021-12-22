import requests
import datetime
import smtplib

def get_iss_location():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    return (int(data['iss_position']['latitude']), int(data['iss_position']['longitude']))

def get_sunrise_sunset():
    parameters = {
        "lat": 27.2046,
        "lng": 77.4977,
        "formatted": 0
    }
    response = requests.get(f'https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    sunrise = response.json()['results']['sunrise'].split('T')[1].split(':')[0]
    sunset = response.json()['results']['sunset'].split('T')[1].split(':')[0]
    return (int(sunrise), int(sunset))

def check_dark_sky():
    return True

# check if it's night
if check_dark_sky():
    # check if iss location is in vicinity [-5, 5] error in latitude
    pass
    # send mail that iss is overhead