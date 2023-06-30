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
    
link_profile = "C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data\\"
profile = "Default"

def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--user-data-dir="+link_profile)
    chrome_options.add_argument("--profile-directory="+profile)
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    prefs = {"profile.managed_default_content_settings.images":2}
    


    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver

def getGoogleHomepage(driver: webdriver.Chrome):
    driver.get("https://gmail.com")
    if(driver.find_element(By.XPATH,'//*[@id="identifierId"]')):
        print("Rớt đăng nhập cha r")
    else:
        print("Dell vào đc mail")
    print("mãi yêu")
    send_msg("Có task ở máy: lỏ rồi")
    
def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")
