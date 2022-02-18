import requests
import subprocess
from bs4 import BeautifulSoup
import urllib.request, urllib.error
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from langdetect import detect

def is_english(text):
    try:
        language = detect(text)
    except Exception as e:
        print('There are no enough features!!', str(e))
        return 'unknown', False
    return language, True if language == 'en' else False

chromedriver_path = './../chromedriver'

def download_text(url):
    policy_text = None
    policy_html = None
    TIMEOUT = 20
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--enable-javascript")
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path=r'{}'.format(chromedriver_path), options=chromeOptions)
    try:
        WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.TAG_NAME, "html")))
        driver.get(url)
        element = driver.find_element_by_tag_name('html')
        policy_text = element.get_attribute('innerText')
        policy_html = driver.page_source
    except TimeoutException as e:
        reason = "HTML element has not been load after {} seconds".format(TIMEOUT)
        print(reason)
    except Exception as e:
        reason = "Error while downloading with Selenium"
        print(reason)
    finally:
        driver.close()
        return policy_text, policy_html

folder = './validation/landing_pages'
file = './validation/validation_apps.txt'

#apks = ['com.roblox.client', 'getfreedata.superfatiza.unlimitedjiodataprank', 'com.mozaix.simoneboard']
f = open('./{}'.format(file), 'r')
apks = f.readlines()
f.close()

privacy_links = []

for apk in apks:
    apk_name = apk[:-1]
    print('buscando apk: ', apk_name)
    url = 'https://play.google.com/store/apps/details?id=%s&hl=es_419&gl=US'%apk_name
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
    except Exception as e:
        print(str(e))
    try:
        href = soup.find_all('a', {'class': 'hrTbp'})[-3].get('href')
        privacy_links.append(href)
        policy_text, policy_html = download_text(href)  
        print(policy_text)
        f = open('./{}/{}.txt'.format(folder, apk_name), 'w')
        f.write(policy_text)
        f.close()
    except:
        f = open('./{}/{}.txt'.format(folder, apk_name), 'w')
        f.write('')
        f.close()
#print(privacy_links)

