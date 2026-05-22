import keyboard
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


with open("url.txt", "r", encoding="utf-8") as file:
    url = file.read().strip()


options = Options()
options.add_argument("--kiosk")  

driver = webdriver.Chrome(options=options)

def amikor_lenyomjak():
    driver.get(url)

keyboard.add_hotkey("c", amikor_lenyomjak)

print("V")
keyboard.wait()