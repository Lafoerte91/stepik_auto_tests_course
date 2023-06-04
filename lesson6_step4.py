import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math



link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    browser = webdriver.Chrome()
    browser.get(link)
    target_price = '$100'
    price = WebDriverWait(browser, 8).until(
        EC.text_to_be_present_in_element((By.ID, "price"), target_price)
    )
    button = browser.find_element(By.ID, "book")
    button.click()
    x = browser.find_element(By.ID, "input_value")
    x = int(x.text)
    result = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(result)
    final = browser.find_element(By.ID, "solve")
    final.click()    
finally:
    time.sleep(30)
    browser.quit()
