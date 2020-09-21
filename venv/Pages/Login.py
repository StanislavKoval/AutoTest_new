import Actions
import Pages.Space
from selenium.webdriver.common.by import By

class Login_Page_Class(Actions.Actions_Class):
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
        print("Залогиниться в системе")
        self.wait_time(time_to_wait=5)
        
        '''Проверка: Решить вопрос с dbadmin
        if self.driver.current_url == Pages.Space.Space_Class.USERS_PAGE:
            print('Успешная авторизация')
        else:
            print("Авторизация не удалась")'''
        
    def system_Log_Out(self):
        self.click_the_button(locator=Pages.Space.Space_Class.LOG_OUT_BUTTON)
        self.click_the_button(locator=Pages.Space.Space_Class.LOG_OUT_BUTTON_EXIT)
        print("Разлогинится из системы")
        self.wait_time(time_to_wait=5)
