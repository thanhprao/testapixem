from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests

frequency = 800
duration = 15000

token = "6240340749:AAGafHc3cj6bVPFfahbXlqKApn1FNFFhTxA"
chat_id = "6292735293"
def send_msg(text):
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id=" + chat_id + "&text="+text
    results = requests.get(url_req)
    return results.json()


def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    prefs = {"profile.managed_default_content_settings.images":2}
    


    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver

def getGoogleHomepage(driver: webdriver.Chrome):
    driver.get("https://www.kenh14.vn")
    elem = driver.find_element(By.XPATH,'//*[@id="searchinput"]')
    elem.send_keys("ca2")
    searchButton= driver.find_element(By.XPATH,'/html/body/form/div[2]/div[2]/div[1]/div/div/a/span')
    searchButton.click()
    print("mãi yêu")
    send_msg("Có task ở máy: "+ name_server.get())
    
def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")
