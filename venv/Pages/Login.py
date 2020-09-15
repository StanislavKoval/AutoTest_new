import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Driver
import Actions

class Login_Page_Locators:

    '''Локаторы'''
    LOGIN_FIELD = (By.ID, 'login')
    PASSWORD_FIELD = (By.ID, "password")
    ENTER_BUTTON = (By.ID, "loginButton")
    #ALARM_INVALID_LOGIN_OR_PASSWORD = (By.XPATH, "//div[@class='alert alert-danger mt-2']")
    
'''    
    def Autorization(self, Login=First_time.Locators.LOGIN, Password=First_time.Locators.PASSWORD):
        Actions.open_site(self)
        Actions.add_text_to_the_field(self,
                                      locator=First_time.Locators.Login_Page_Locators.LOGIN_FIELD,
                                      text=Login)
        Actions.wait_time(self,
                          time_to_wait=1)
        Actions.add_text_to_the_field(self,
                                      locator=First_time.Locators.Login_Page_Locators.PASSWORD_FIELD,
                                      text=Password)
        Actions.wait_time(self, time_to_wait=1)
        Actions.click_the_button(self,
                                 locator=First_time.Locators.Login_Page_Locators.ENTER_BUTTON)
        Actions.wait_time(self, time_to_wait=2)

        # Проверка
        if self.driver.current_url == First_time.Locators.Page_adresses.CASES_PAGE:
            print('Успешная авторизация')
        else:
            print("Авторизация не удалась")
            
 '''
    