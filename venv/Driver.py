import selenium
from selenium import webdriver

class Driver:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/NewUser/Desktop/New folder/webdriver/chromedriver.exe")