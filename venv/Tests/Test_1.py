import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

import Driver
import Actions
import Pages.Space
import Pages.Login
#import Pages.Login
#import Pages.Space

bb = Actions.Actions()

bb.open_site(link=Pages.Space.Space.LOGIN_PAGE)
#bb.add_text_to_the_field(locator=Pages.Login.Login_Page_Locators.LOGIN_FIELD,text='dbadmin')
#bb.add_text_to_the_field(locator=Pages.Login.Login_Page_Locators.PASSWORD_FIELD,text='pwd1')
print(Pages.Login.Login_Page_Locators.LOGIN_FIELD)

bb.close_site()
#обновление локаторов на логин стр