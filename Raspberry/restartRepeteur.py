"""
    Projet : restartRepeteur
    Date Creation : 01/10/2024
    Date Revision : 03/01/2024
    Entreprise : 3SC4P3
    Auteur: Florian HOFBAUER
    Contact :
    But : Reboot repeter
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pushbullet import Pushbullet

# Option for website (no screen open)
options = Options()
options.add_argument('--headless')
options.add_argument("-disable-gpu")
options.add_argument("--disable-popup-blocking")
options.add_argument("--start-maximized")

path = '/usr/bin/chromedriver'
service = Service(executable_path=path)

# Initiate the browser
browser = webdriver.Chrome(service=service, options=options)

# Open the Website
browser.get('http://192.168.1.43/backUpSettings.html')

# Your  credentials
name = 'floflodu55@hotmail.fr'
mdp = 'Fouines55'

# API for notification
api_key = 'o.6RxYZlji3PYG1hlGhezV6pOGoH4VPucu'
pb = Pushbullet(api_key)

# Fill credentials
browser.find_element(by=By.NAME, value='email_auth').send_keys(name)
browser.find_element(by=By.NAME, value='passwd_auth').send_keys(mdp)

time.sleep(5)

# Click Log In
browser.find_element(by=By.ID, value='loginBt').click()
time.sleep(5)

# Click restart
browser.find_element(by=By.ID, value='restartBt').click()
time.sleep(5)

browser.find_element(by=By.NAME, value='ROMRestart').click()

restartComplete = WebDriverWait(browser, 300).until(EC.visibility_of_element_located((By.ID, "connectedNetwork")))
time.sleep(30)

restartComplete.click()
time.sleep(60)

time.sleep(150)
try:
    alert = browser.switch_to_alert()
    alert.dismiss()
except UnexpectedAlertPresentException as e:
    print('[!] Error: ' + str(e))

time.sleep(10)
browser.get('http://192.168.1.43/logout.htm')
time.sleep(5)

notif = "Restart complete."
push = pb.push_note('Netgear Repeter', notif)

browser.close()
