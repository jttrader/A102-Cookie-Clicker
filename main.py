import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_driver_path = r'F:\Python\Udemy\DevelopmentSelenium\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

#Get cookie to click on.
cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 5
five_min = time.time() + 60*5 # Five minutes

while True:
    cookie.click()
    if time.time() > timeout:
        buyable = []
        store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
        for item in store[:-1]:
            if item.get_attribute('class') != "grayed":
                buyable.append(item)
        buyable[-1].click()
        timeout = time.time() + 5
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, value="cps").text
        print(cookie_per_s)
        break