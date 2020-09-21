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


bb=Pages.Login.Login_Page_Class()

bb.system_Log_In()
bb.system_Log_Out()
bb.close_site()