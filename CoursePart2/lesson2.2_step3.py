from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x,y):
  return str(int(x)+int(y))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome("/Users/katerina/Web/chromedriver")
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    z = calc(x,y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(z)


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


