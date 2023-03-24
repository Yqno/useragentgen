import random


# Liste der verfügbaren Betriebssysteme
os_list = [
    "Windows NT 10.0; Win64; x64", 
    "Macintosh; Intel Mac OS X 10_15_7",
    "iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X", # iPhone 13 Pro Max
    "iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X", # iPhone 12
    "iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X", # iPhone 11
    "iPhone; CPU iPhone OS 14_4 like Mac OS X",
    "Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv",
    "Linux; Android 11; Pixel 4 XL Build/RQ2A.210505.003",
    "Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv",
    "Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv",
    "X11; U; Linux armv7l like Android; en-us",
    "X11; Linux x86_64",
    "X11; Ubuntu; Linux x86_64; rv:15.0",
    "PlayStation; PlayStation 5/2.26",
    "PlayStation 4 3.11",
    "PlayStation Vita 3.61",
    "Windows NT 10.0; Win64; x64; Xbox; Xbox Series X",
    "Windows NT 10.0; Win64; x64; XBOX_ONE_ED",
    "Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One",
    "Nintendo Switch; WifiWebAuthApplet",
    "Nintendo WiiU",
    "Nintendo 3DS; U; ; en"


]

# Liste der verfügbaren Browser
browser_list = [
    "Chrome/48.0.2564.82 Safari/537.36 Edge/20.02",
    "NF/4.0.0.5.10 NintendoBrowser/5.1.0.13343"
    "NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US"
    "Safari/537.36",
    "Safari/605.1.15"
    "Firefox/87.0",
    "Chromium/88.0.4324.150"
]


webkit_list = [
    "AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148", # iPhone 11
    "AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 ", # Apple iPhone XS (Chrome)
    "AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372", # Apple iPhone X
    "AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f", # Apple iPhone 8
    "AppleWebKit/537.36",
    "AppleWebKit/601.3.9"
]

# Abfrage der Eingabe für das Betriebssystem
os_input = input(f"Wähle das OS (1-{len(os_list)}): ")
os_index = int(os_input) - 1
os = os_list[os_index]

# Abfrage der Eingabe für den Browser
browser_input = input(f"Wähle den Browser (1-{len(browser_list)}): ")
browser_index = int(browser_input) - 1
browser = browser_list[browser_index]

# Abfrage des AppleWebkit
webkit_input = input(f"Wähle dein AppleWebkit (1-{len(webkit_list)}): ")
webkit_index = int(webkit_input) - 1 
webkit = webkit_list[webkit_index]

user_agent = f"Mozilla/5.0 ({os}) {webkit} ({browser})"

print(user_agent)
