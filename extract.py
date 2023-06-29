from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template , request


def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True


    chrome_options.add_experimental_option("prefs", prefs)
    chrome_option.add_argument("--user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data\\")
    chrome_option.add_argument("--profile-directory=Profile 1")
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver

def getGoogleHomepage(driver: webdriver.Chrome) -> str:
    checkweb = driver.get("https://www.google.com")
    return checkweb

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")
