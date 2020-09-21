import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Actions


'''Здесь локаторы и функции для элементов без страницы (хедеры)'''

class Space_Class(Actions.Actions_Class):
    '''Адреса страниц'''
    LOGIN_PAGE = "http://192.168.4.222/login"
    CASES_PAGE = "http://192.168.4.222/lk/cases"
    USERS_PAGE = "http://192.168.4.222/lk/admin"
    WORKSPACE_PAGE = "http://192.168.4.222/lk/workspace/main"
    COMMON_DATA_PAGE = "http://192.168.4.222/lk/workspace/common"




    """Верхний хедер"""
    LOG_OUT_BUTTON = (By.XPATH, "//a[@class='bar__link']")
    LOG_OUT_BUTTON_EXIT = (By.XPATH, "//div[@class='drop-menu__outer drop-menu__outer--right']//a[@class='drop-menu__item']")

    WORKSPACE_BUTTON = (By.XPATH, "//li[@class='bar__item']//a[@href='/lk/workspace/main']")

#Переделать
    def open_workspace(self,Workspace=WORKSPACE_BUTTON,Check=WORKSPACE_PAGE):
        self.wait_time(time_to_wait=2)
        self.click_the_button(locator=Workspace)

        self.wait_time(time_to_wait=2)

        if self.driver.current_url == Check:
            print('Успешное открытие Рабочего простраства')
        else:
            print("Открытие Рабочего простраства не удалось")
            

"""Нижний хедер"""
'''
    DEVICES_PAGE = "http://192.168.4.222/devices"
    DICTIONARY_PAGE = "http://192.168.4.222/dicts"
    TAGS_PAGE = "http://192.168.4.222/tags"
    FILES_PAGE = "http://192.168.4.222/workspace/1"
    MAPS_PAGE = "http://192.168.4.222/workspace/0"'''

'''
    CASE_BUTTON = (By.XPATH, "//a[@class='app-header-content-topMenu-ul-li-link active']")
    LIBRARY_BUTTON = (By.XPATH,"//div[@class='app-header-content-topMenu-ul-li-link']//span[@class='app-header-content-topMenu-ul-li-link-label']")
    DEVICES_BUTTON = (By.XPATH, "//li[@class='app-header-content-topMenu-ul-li topMenu-li']//li[1]//span[1]")
    DICTS_BUTTON = (By.XPATH, "//li[@class='app-header-content-topMenu-ul-li topMenu-li']//li[3]//span[1]")
    TAGS_BUTTON = (By.XPATH,"/html[1]/body[1]/div[1]/wa-root[1]/wa-cases[1]/div[1]/wa-header[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[3]/div[2]/nav[1]/li[4]/span[1]")
    SYS_JOURNAL_BUTTON = (By.XPATH, "//li[5]//span[1]")'''

'''
    def Go_to_Cases(self, time_to_wait=3):

        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.CASE_BUTTON)
        Actions.wait_time(self, time_to_wait=time_to_wait)
        # проверка
        if self.driver.current_url == First_time.Locators.Page_adresses.CASES_PAGE:
            print('Переход на страницу Дела')
        else:
            print('Переход на страницу Дела не удался')

    def Go_to_Workspace(self, time_to_wait=3):
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.WORKSPACE_BUTTON)
        Actions.wait_time(self, time_to_wait=time_to_wait)
        # проверка
        if self.driver.current_url == First_time.Locators.Page_adresses.WORKSPACE_PAGE:
            print('Переход на страницу Рабочее пространство')
        else:
            print('Переход на страницу Рабочее пространство не удался')

    def Go_to_Devices(self, time_to_wait=3):
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.LIBRARY_BUTTON)
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.DEVICES_BUTTON)
        Actions.wait_time(self, time_to_wait=time_to_wait)
        if self.driver.current_url == First_time.Locators.Page_adresses.DEVICES_PAGE:
            print('Переход на страницу Устройства')
        else:
            print('Переход на страницу Устройства не удался')

    def Go_to_Dictionaries(self, time_to_wait=3):
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.LIBRARY_BUTTON)
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.DICTS_BUTTON)
        Actions.wait_time(self, time_to_wait=time_to_wait)
        if self.driver.current_url == First_time.Locators.Page_adresses.DICTIONARY_PAGE:
            print('Переход на страницу Словари')
        else:
            print('Переход на страницу Словари не удался')

    def Go_to_Tags(self, time_to_wait=3):
        print('Переход на страницу Теги')
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.LIBRARY_BUTTON)
        Actions.click_the_button(self, locator=First_time.Locators.Navigation_Locators.TAGS_BUTTON)
        Actions.wait_time(self, time_to_wait=time_to_wait)
        if self.driver.current_url == First_time.Locators.Page_adresses.TAGS_PAGE:
            print('Переход на страницу Теги')
        else:
            print('Переход на страницу Теги не удался')

        '''
        

        
        
        
            
            
            
            
        