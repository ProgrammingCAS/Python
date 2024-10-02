#IMPORTS
import requests; import json; from colorama import *; from colorama import init; from datetime import datetime; import time; import geocoder; import subprocess
#GLOBAL VARS
init(autoreset=True)
class ascii: 
    ascii_logo = """
     ________   _______  _______   ________  _______    _______   _______ 
    ╱  ╱  ╱  ╲╱╱       ╲╱       ╲╲╱        ╲╱    ╱  ╲╲╱╱       ╲╱╱       ╲
   ╱         ╱╱        ╱        ╱╱        _╱        ╱╱╱        ╱╱        ╱
  ╱╱        ╱        _╱         ╱╱       ╱╱         ╱        _╱        _╱ 
  ╲╲_______╱╲________╱╲___╱____╱ ╲_____╱╱ ╲___╱____╱╲________╱╲____╱___╱  
    """

    moonspinner = ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘", "🌘"]

    manual = Style.BRIGHT + Fore.LIGHTBLACK_EX + """
    __________________________________/""" + Fore.WHITE + Style.BRIGHT +  'Manual' + Style.BRIGHT + Fore.LIGHTBLACK_EX + """\\__________________________________
    @ Weather app,

    """ + Fore.WHITE + Style.BRIGHT +  '* Functionality: ' + Style.BRIGHT + Fore.LIGHTBLACK_EX + """
        - Description: Weather overview.
        - Temperature: Current temp in °C.
        - Feels Like: Perceived temp in °C.
        - Humidity: % of humidity.
        - Sunrise & Sunset: Local times.
        - Cloud Coverage: % of sky covered.
        - Wind Speed: Wind in mph.
        - Theres some other ones that can be seen only when putting -A to the end of your command

    """ + Fore.WHITE + Style.BRIGHT +  '* Usage: ' + Style.BRIGHT + Fore.LIGHTBLACK_EX + """
        - Set the longitude and lattitude:
            la -> x (sets lattitude to the value of x)
            lo -> x (sets the longtitude to the value of x)
                x is for any float value that exists as a cordinate
                e.g (lo -> 25.251)
            It is also possible to set both values simutaniously:
            la -> x | lo -> y (reverse order works as well)

   """ + Fore.WHITE + Style.BRIGHT +  '* Utilities: ' + Style.BRIGHT + Fore.LIGHTBLACK_EX + """
            exit (I wonder what this does, try it)
            clear (mhmmm, it clears the screen)
            reset (resets your api requests)
            save (saves the most recent information to a file, with all data included)

        Thats all, good luck
    """
#FUNCTIONS
def getweather(lat, lon, apitoken):
    cookies = {
        "Dont really want to show my cookies but you can get these by capturing the request from the api once logged in"
    }
    params = {
        'lat': f'{str(lat)}',
        'lon': f'{str(lon)}',
        'appid': f'{str(apitoken)}',
    }
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params, cookies=cookies)
    weather =  response.json()
    return weather
def get_params(weather):

    weather_dis = weather['weather'][0] 
    weather_main = weather_dis['main']
    weather_description = weather_dis['description']

    weather_param = weather['main']
    temp = weather_param['temp']
    feels_like = weather_param['feels_like']
    humidity = weather_param['humidity']
    
    weather_day = weather['sys']
    sunrise = weather_day['sunrise']
    sunset = weather_day['sunset']
    
    weather_clouds = weather['clouds']
    clouds = weather_clouds['all']
    
    wind_speed = weather['wind']['speed']
    wind_deg = weather['wind']['deg']
    
    rain_1h = weather.get('rain', {}).get('1h', 0) 
    return [weather_main, weather_description, temp, 
            feels_like, humidity, sunrise, sunset, clouds, 
            wind_speed, wind_deg, rain_1h]

def sun_rs(timestamp):
    utc_time = str(datetime.fromtimestamp(timestamp))
    time_n_date = utc_time.split()
    time = time_n_date[1]
    return time

def INPUT(prompt):
    var = input(prompt)
    print("\033[1A", end='')
    print(' ' * (len(prompt) + 50), end='\r') 
    return var

def get_current_coordinates():

    g = geocoder.ip('me')
    if g.latlng is not None:
        return g.latlng
    else:
        return None

def showinfo(info_stats, la, lo):

    print("\n    ", end=''); print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f"\033[1mWEATHER ({la}, {lo}):" + Back.RESET)
    print("        ", end=''); print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f"Discription:" + Back.RESET + Fore.MAGENTA + f" {info_stats[1]}")
    print("        ", end='');print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f"Tempature:" + Back.RESET + Fore.MAGENTA + f" {(float(info_stats[2]) - 273.15):.2f}°C")
    print("        ", end='');print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f"Feels-like:" + Back.RESET + Fore.MAGENTA + f" {(float(info_stats[3]) - 273.15):.2f}°C")
    print("        ", end='');print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f"Humidity:" + Back.RESET + Fore.MAGENTA + f" {info_stats[4]}%")
    print("        ", end='');print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f"Sunrise:" + Back.RESET + Fore.MAGENTA + f" {sun_rs(info_stats[5])}")
    print("        ", end='');print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f"Sunset:" + Back.RESET + Fore.MAGENTA + f" {sun_rs(info_stats[6])}")
    print("        ", end='');print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f"Clouds:" + Back.RESET + Fore.MAGENTA + f" {info_stats[7]}%")
    print("        ", end='');print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f"Wind:" + Back.RESET + Fore.MAGENTA + f" {info_stats[8]} mph")
    print()

def wait(lime):
    global ascii
    spinner = ascii.moonspinner
    j = 0
    p = 0
    t = int(float(lime) / 0.2) 
    while p != t + 1:
        print(Fore.LIGHTCYAN_EX + '    Fetching Info... ' + spinner[j], end='\r')
        time.sleep(0.1)
        p += 1
        j += 1
        if j == len(spinner):
            j = 0
    print(' ' * (len('    Fetching Info... ' + spinner[j]) + 20), end='\r')
def PRINT(prompt):
    print(prompt, end='\r')
# MAIN FUNCTION
def __init__():
    global ascii
    #VARIABLES
    token = 'YOU CAN GET THIS BY LOGGING INTO THE WEBSITE, otherwise ask me to show you'
    coordinates = get_current_coordinates()
    la, lo = coordinates
    weather = getweather(la, lo, token)
    info_stats = get_params(weather)
    print(ascii.ascii_logo)
    showinfo(info_stats, la, lo)
    i = 0
    while True:
        req = INPUT(f"/({la}, {lo})/>")
        cmd = req.split()
        try:
            if cmd[0] == "lo" and len(cmd) == 3:
                if cmd[1] == "->":
                    print(Style.BRIGHT + Fore.WHITE + f'lo -> {cmd[2]}', end='\r')
                    lo = float(cmd[2])
                    time.sleep(2)
                    print(' ' * (len(f"lo -> {cmd[2]}") + 50), end='\r') 
            elif cmd[0] == "la" and len(cmd) == 3:
                if cmd[1] == "->":
                    print(Style.BRIGHT + Fore.WHITE + f'la -> {cmd[2]}', end='\r')
                    la = float(cmd[2])
                    time.sleep(2)
                    print(' ' * (len(f"lo -> {cmd[2]}") + 50), end='\r') 
            elif cmd[0] == 'run': #la -> 21 lo -> 21
                wait(2)
                i+=1
                weather = getweather(la, lo, token)
                info_stats = get_params(weather)
                print("_" * 25, end=''); print(f"/{i}\\", end=''); print("_" * 25)
                showinfo(info_stats, la, lo)
            elif cmd[0] == "exit":
                break
            elif (cmd[0] == "la") and (cmd[4] == "lo"):
                if ((cmd[1] and cmd[5]) == "->") and (cmd[3] == "|"):
                    print(Style.BRIGHT + Fore.WHITE + f'la -> {cmd[2]}, lo -> {cmd[6]}', end='\r')
                    la = float(cmd[2])
                    lo = float(cmd[6])
                    time.sleep(2)
                    print(' ' * (len(f"la -> {cmd[2]}, lo -> {cmd[6]}") + 50), end='\r') 
            elif (cmd[0] == "lo") and (cmd[4] == "la"):
                if ((cmd[1] and cmd[5]) == "->") and (cmd[3] == "|"):
                    print(Style.BRIGHT + Fore.WHITE + f'lo -> {cmd[2]}, la -> {cmd[6]}', end='\r')
                    la = float(cmd[6])
                    lo = float(cmd[2])
                    time.sleep(2)
                    print(' ' * (len(f"la -> {cmd[2]}, lo -> {cmd[6]}") + 50), end='\r') 
            elif cmd[0] == "help":
                print(ascii.manual)
            elif cmd[0] == "clear":
                subprocess.run("powershell clear")
        except:
            i - 1

if __name__ == '__main__':
    __init__()
