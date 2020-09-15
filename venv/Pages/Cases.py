import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Case_Page_Locators:
    CASE_COUNTER = (By.XPATH,"//span[@class='app-content-title-count']")
    ADD_CASE_BUTTON = (By.XPATH, "//div[@class='dataTableSort-addTrigger']")
    QUICKFILTER_FIELD = (By.XPATH, "//input[@id='flt']")

    PERSON_COUNTER = (By.XPATH,"//div[@class='app-contentPage-sideBarSubTitle']")
    NUMBER_FIELD = (By.XPATH,"//input[@id='editableNumber']")
    NAME_FIELD = (By.XPATH,"//input[@id='editableName']")
    ADD_BUTTON = (By.XPATH,"//button[@id='btn-case']")
    PERSON_TAB = (By.XPATH,"//div[@class='app-contentPage']//li[2]//span[1]")
    CASE_TAB = (By.XPATH,"//li[@class='active']//span[@class='c-tab__link']")
    THREE_DOT_BUTTON = (By.XPATH,"//div[@class='barMenu-trigger']")
    FROM_CASES_TO_WORKSPACE_BUTTON = (By.XPATH, "//div[@class='barMenu-window barMenu--open']/button[1]")
    FROM_CASES_TO_FILES_BUTTON = (By.XPATH, "//div[@class='barMenu-window barMenu--open']/button[2]")
    DELETE_CASE_BUTTON = (By.CSS_SELECTOR, "div.app-wrapper:nth-child(1) div.pageContainer.casesPage div.app-contentPage:nth-child(2) div.app-rightSideBar div.rightSideBar--box div.sidebarHead div.barMenu.barMenuDeadZone div.barMenu-window.barMenu--open > button.barMenu-link:nth-child(3)")

    def Create_case(self, Case_number, Case_name, delete=False):

        if self.driver.current_url == First_time.Locators.Page_adresses.CASES_PAGE:
            Actions.click_the_button(self, locator=First_time.Locators.Case_Page_Locators.ADD_CASE_BUTTON)
            Actions.add_text_to_the_field(self, locator=First_time.Locators.Case_Page_Locators.NUMBER_FIELD,
                                          text=Case_number)
            Actions.add_text_to_the_field(self, locator=First_time.Locators.Case_Page_Locators.NAME_FIELD,
                                          text=Case_name)
            Actions.click_the_button(self, locator=First_time.Locators.Case_Page_Locators.ADD_BUTTON)
            Actions.wait_time(self, time_to_wait=1)

            # остановился тут
            if Actions.verify_alert_existence(self) == True:
                if self.driver.switch_to_alert().text == 'Данное дело уже существует':
                    return print('Данное дело уже существует')

            # Задержка на время создания
            # Actions.implicit_time(self)
            Actions.wait_time(self, time_to_wait=10)

            # перед тем как выводить лог сделать проверку + учесть счетчик
            print('Дело создано')

            if delete == True:
                print('Удаляем созданное тестовое дело')
                Actions.click_the_button(self, locator=First_time.Locators.Case_Page_Locators.THREE_DOT_BUTTON)
                Actions.click_the_button(self, locator=First_time.Locators.Case_Page_Locators.DELETE_CASE_BUTTON)  # !
                Actions.accept_alarm(self)
                Actions.wait_time(self, time_to_wait=5)
                print('Удалено')

        else:
            print("Пользователь не находится на странице /cases")