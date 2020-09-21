'''Обертки для удобного использования коробки'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException
import time
from selenium.webdriver.support.ui import WebDriverWait
import selenium
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

import Driver




class Actions(Driver.Driver):
    '''Работа с браузером'''
    def open_site(self,link):
        print('Открытие браузера')
        self.driver.maximize_window()
        self.driver.get(link)
        time.sleep(5)

    def close_site(self):
        print('Закрытие браузера')
        self.driver.quit()

    def refresh_the_page(self):
        print('Обновление страницы')
        self.driver.refresh()



    '''Работа с полями'''
    def add_text_to_the_field(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def clean_the_field(self, locator):
        self.driver.find_element(*locator).clear()

    #Нужно проверить можно ли забрать значение из поля после его ввода add_text_to_the_field методом save_string


    '''Работа с кнопками'''
    def click_the_button(self, locator):
        self.driver.find_element(*locator).click()




    '''Считывание данных'''
    def save_counter_meaning(self, locator):
        meaning_int = self.driver.find_element(*locator).text

        meaning_int = meaning_int.replace(' ', '')#удаляет пробелы
        if meaning_int.isdigit() == True:
            meaning_int = int(meaning_int)
            return meaning_int

    def save_string(self, locator):
        meaning_str = self.driver.find_element(*locator).text
        return meaning_str





    '''Управление задержками'''
    def wait_time(self, time_to_wait):#самый плохой вариант
        time.sleep(time_to_wait)

    #неявная задержка
    def implicit_time(self, time_to_wait=60):
        self.driver.implicitly_wait(time_to_wait)








    '''Проверки'''
    # Проверка на существование элемента по локатору
    def verify_existence(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    # Проверка на наличие alarm на странице
    def verify_alert_existence(self):
        try:
            self.driver.switch_to_alert()
            return True
        except NoAlertPresentException:
            return False

    #кликнуть да на alarm
    def accept_alarm(self):
        self.driver.switch_to_alert().accept()
