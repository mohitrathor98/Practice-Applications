import requests
import datetime as dt
import smtplib

latitude = 27.2046
longitude = 77.4977

def get_iss_location():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    return (int(data['iss_position']['latitude']), int(data['iss_position']['longitude']))

def get_sunrise_sunset():
    parameters = {
        "lat": latitude,
        "lng": longitude,
        "formatted": 0
    }
    response = requests.get(f'https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    # times in utc
    sunrise = response.json()['results']['sunrise'].split('T')[1].split(':')[0]
    sunset = response.json()['results']['sunset'].split('T')[1].split(':')[0]
    return (int(sunrise), int(sunset))

def check_dark_sky():
    sun_timings = get_sunrise_sunset() 
    current_time = str(dt.datetime.utcnow())
    current_time = int(current_time.split(' ')[1].split(':')[0])
    
    # current time is post sunset or pre sunrise
    # then it is a dark sky
    if current_time>sun_timings[1] or current_time<sun_timings[0]:
        return True
    return False


def is_iss_overhead():
    iss_location = get_iss_location()
    # latitude check
    if (
        (iss_location[0]>(latitude-5)) and
        (iss_location[0]<(latitude+5)) and
        (iss_location[1]>(longitude-5)) and
        (iss_location[1]>(longitude+5)) 
        ):
        send_mail()
    else:
        print("NOT OVERHEAD YET")
        

def send_mail():
    my_email = "mohitdemo7@gmail.com"
    password = "demopassword"

    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls() 
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="mohitdemo7@yahoo.com", 
            msg=f"Subject:ISS Overhead"+
            "Hi,\n\nInternational space station is overhead."+
            "GO and See."
        )

# check if it's night
if check_dark_sky():
    # check if iss location is in vicinity [-5, 5] error in latitude
    if is_iss_overhead():
        send_mail()