"""
    Projet : restartRepeteur
    Date Creation : 01/10/2023
    Date Revision : 03/06/2024
    Entreprise : 3SC4P3
    Auteur: Florian HOFBAUER
    Contact :
    But : Reboot repeter
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import time
from pushbullet import Pushbullet

# Option for website (no screen open)
options = Options()
options.add_argument("--disable-popup-blocking")
# options.add_argument('--headless')

# Initiate the browser
browser = webdriver.Chrome(options=options)

ipNetgear = "http://192.168.1.28/"

link = ipNetgear + "backUpSettings.html"
# Open the Website
browser.get(link)

# Your  credentials
name = 'floflodu55@hotmail.fr'
mdp = 'Fouines55'

# API for notification
api_key = 'o.6RxYZlji3PYG1hlGhezV6pOGoH4VPucu'
pb = Pushbullet(api_key)

# Fill credentials
browser.find_element(by=By.NAME, value='email_auth').send_keys(name)
browser.find_element(by=By.NAME, value='passwd_auth').send_keys(mdp)

time.sleep(15)

# Click Log In
browser.find_element(by=By.ID, value='loginBt').click()
time.sleep(15)

try:
    # Essayez de trouver l'élément
    loginTest = browser.find_element(by=By.ID, value='loginBt')
except NoSuchElementException:
    loginTest = ''

if loginTest != '':
    loginTest.click()

time.sleep(15)

# Click restart
browser.find_element(by=By.ID, value='restartBt').click()
time.sleep(5)

browser.find_element(by=By.NAME, value='ROMRestart').click()

restartComplete = WebDriverWait(browser, 300).until(EC.visibility_of_element_located((By.ID, "connectedNetwork")))
time.sleep(30)

restartComplete.click()

time.sleep(150)
try:
    alert = browser.switch_to.alert
    alert.dismiss()
except UnexpectedAlertPresentException as e:
    print('[!] Error: ' + str(e))

link = ipNetgear + "logout.html"

time.sleep(10)
browser.get(link)
time.sleep(5)

notif = "Restart complete."
push = pb.push_note('Netgear Repeter', notif)

browser.close()
