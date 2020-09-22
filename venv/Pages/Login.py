import Actions
import Pages.Header

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
        self.open_site(link=Pages.Header.Header_Class.LOGIN_PAGE)
        self.add_text_to_the_field(locator=Login_Page_Class.LOGIN_FIELD, text=Login)
        self.add_text_to_the_field(locator=Login_Page_Class.PASSWORD_FIELD, text=Password)
        self.click_the_button(locator=Login_Page_Class.ENTER_BUTTON)
        print("Залогиниться в системе")
        self.wait_time(time_to_wait=3)
        if self.driver.current_url == Pages.Header.Header_Class.USERS_PAGE:
            print('Успешная авторизация')
        else:
            print("Авторизация не удалась")
        

