from selenium import webdriver
import time
from math import log, sin


def calc(x):
    return log(abs(12 * sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/alert_accept.html")

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    confirm = browser.switch_to.alert
    confirm.dismiss()

    button.click()
    confirm.accept()

    value = browser.find_element_by_id('input_value')
    x = int(value.text)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(calc(x)))

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(4)
    browser.quit()
