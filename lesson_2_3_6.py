from selenium import webdriver
import time
from math import log, sin


def calc(x):
    return log(abs(12 * sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element_by_css_selector('button.trollface')
    button.click()

    new_window_name = browser.window_handles[1]
    browser.switch_to.window(new_window_name)

    value = browser.find_element_by_id('input_value')
    x = int(value.text)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(calc(x)))

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(4)
    browser.quit()
