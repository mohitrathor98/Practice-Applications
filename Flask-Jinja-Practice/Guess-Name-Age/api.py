import requests

def guessAge(name):
    res = requests.get("https://api.agify.io?name={0}".format(name))
    age = res.json()
    return age["age"]

def guessGender(name):
    res = requests.get("https://api.genderize.io?name={0}".format(name))
    gender = res.json()
    return gender["gender"]
