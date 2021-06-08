from selenium import webdriver
import time
import os

try:
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome("/Users/katerina/Web/chromedriver")
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("test@test.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    print(file_path)
    input4 = browser.find_element_by_css_selector('input[type="file"]')
    print(input4)
    input4.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла