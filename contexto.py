#contexto solver

import requests
import subprocess
from colorama import Fore, Style, init
init(True)

HEADERS = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://contexto.me/',
        'Origin': 'https://contexto.me',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Priority': 'u=0',
    }

GAMEID = "755"

def req(option, type):
    global HEADERS, GAMEID
    if type == "guess":
        response = requests.get(f'https://api.contexto.me/machado/en/game/{GAMEID}/{option}', headers=HEADERS)
    elif type == "top":
        response = requests.get(f'https://api.contexto.me/machado/en/top/{GAMEID}', headers=HEADERS)
    elif type == "solve":
        response = requests.get(f'https://api.contexto.me/machado/en/giveup/{GAMEID}', headers=HEADERS)
    result = response.json()
    return result

def inputEx(prompt):
    var = input(prompt)
    print("\033[1A", end='')
    print(' ' * (len(prompt) + 50), end='\r') 
    return var

def main():
    DONE = False

    while not DONE:
        contexto = inputEx(Fore.LIGHTGREEN_EX + Style.BRIGHT + "|contexto|-> " + Style.NORMAL)
        cmd = (contexto.split())[0]
        try:
            if cmd == "guess":
                word = (contexto.split())[1]
                distance = (req(word, "guess"))["distance"]
                print(distance)
            elif cmd == "find":
                distance = (contexto.split())[1]
                word = ((req(None, "top"))[f"words"])[int(distance)]
                print(word)
            elif cmd == "solve":
                word = req(None, "solve")["word"]
                print(word)
            elif cmd == "clear":
                subprocess.run("powershell clear")
            elif cmd == "exit":
                exit()
        except Exception as e:
            print(f"error -> {e}")

if __name__ == "__main__":
    main()
