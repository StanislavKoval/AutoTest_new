import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Driver
import Actions
import Pages.Space

class Login_Page_Class(Actions.Actions):
    '''Данные авторизации'''
    LOGIN="dbadmin"
    PASSWORD="pwd1"

    '''Локаторы страницы'''
    LOGIN_FIELD = (By.ID, "login")
    PASSWORD_FIELD = (By.ID, "password")
    ENTER_BUTTON = (By.ID, "loginButton")
    #ALARM_INVALID_LOGIN_OR_PASSWORD = (By.XPATH, "//div[@class='alert alert-danger mt-2']")
    
    
    def system_Log_In (self, Login=LOGIN, Password=PASSWORD):
        self.open_site(link=Pages.Space.Space_Class.LOGIN_PAGE)
        self.add_text_to_the_field(locator=Pages.Login.Login_Page_Class.LOGIN_FIELD, text=Login)
        self.add_text_to_the_field(locator=Pages.Login.Login_Page_Class.PASSWORD_FIELD, text=Password)
        self.click_the_button(locator=Pages.Login.Login_Page_Class.ENTER_BUTTON)
        print("Залогинится из системе")
        self.wait_time(time_to_wait=5)
        
        '''Решить вопрос с dbadmin
        if self.driver.current_url == Pages.Space.Space_Class.USERS_PAGE:
            print('Успешная авторизация')
        else:
            print("Авторизация не удалась")'''
        
    def system_Log_Out(self):
        self.click_the_button(locator=Pages.Space.Space_Class.LOG_OUT_BUTTON_1)
        self.click_the_button(locator=Pages.Space.Space_Class.LOG_OUT_BUTTON)
        print("Разлогинится из системы")
        self.wait_time(time_to_wait=5)

        
    
    
    
    
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
    