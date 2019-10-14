from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from math import sin, log


def calc(x):
    return log(abs(12 * sin(x)))


browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
