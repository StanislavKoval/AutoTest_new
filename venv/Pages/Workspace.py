import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

import Actions

class Workspace_Class(Actions.Actions_Class):


    GRID_COUNTER = (By.XPATH,"//h1[@class='typography__header--extra-large']")
    '''
    RESET_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/button[2]")
    DESCRIPTION_SEARCH_FIELD = (By.XPATH, "//input[@id='searchInput']")
    FROM_DATE_FIELD = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]")
    TO_DATE_FIELD = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[2]/input[1]")
    OPEN_CATEGORIES_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/span[1]")

    CATEGORIES_FILES_CHECKBOX = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
    CATEGORIES_FILES_COUNTER = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/div[4]")

    APPLY_FILTER_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/div[1]/div[2]/button[1]")

    MAIN_ELEMENT_COUNTER = (By.XPATH, "/html[1]/body[1]/div[1]/wa-root[1]/wa-workspace[1]/div[1]/div[2]/ws-tab[1]/div[1]/ws-datagrid[1]/div[1]/div[1]/span[1]")'''

    def save_grid_counter(self):
        counter = self.save_string(locator=Workspace_Class.GRID_COUNTER)
        counter = re.sub(r'Элементы','',counter)
        counter = re.sub(r'Events','',counter)
        counter = re.sub(r',','',counter)
        counter = re.sub(r' ','',counter)
        counter = re.sub(r':','',counter)

        counter = int(counter)
        return counter
    '''
    # применения фильтра категории
    def Apply_filter(self ):  # наверное лучше будет потом преобразовать его как применение фильтра категории #,checkbox_i_need, counter_i_need)
        if self.driver.current_url == First_time.Locators.Page_adresses.WORKSPACE_PAGE:
            all_elements = Actions.save_counter_meaning(self,
                                                        First_time.Locators.Workspace_Page_Locators.MAIN_ELEMENT_COUNTER)
            # print(all_elements)
            Actions.click_the_button(self,
                                     First_time.Locators.Workspace_Page_Locators.OPEN_CATEGORIES_BUTTON)  # поиграть с локаторами так чтобы сделать их зависисмыми от порядкого номера
            Actions.click_the_button(self, First_time.Locators.Workspace_Page_Locators.CATEGORIES_FILES_CHECKBOX)
            elements_in_filter = Actions.save_counter_meaning(self,
                                                              First_time.Locators.Workspace_Page_Locators.CATEGORIES_FILES_COUNTER)
            # print(elements_in_filter)

            # Применяем фильтр
            Actions.click_the_button(self, First_time.Locators.Workspace_Page_Locators.APPLY_FILTER_BUTTON)

            # Ожидание результата применения фильтра
            Actions.wait_time(self, time_to_wait=40)
            print('Фильтр применен')

            elements_after_filtration = Actions.save_counter_meaning(self,
                                                                     First_time.Locators.Workspace_Page_Locators.MAIN_ELEMENT_COUNTER)
            # print(elements_after_filtration)
            print('Проверка счетчиков')

            if elements_in_filter == elements_after_filtration:
                # Нажимаем кнопку сбросить
                Actions.click_the_button(self, First_time.Locators.Workspace_Page_Locators.RESET_BUTTON)

                # Ожидание результата после сброса фильтра
                Actions.wait_time(self, time_to_wait=15)

                all_elements_after_filtration = Actions.save_counter_meaning(self,
                                                                             First_time.Locators.Workspace_Page_Locators.MAIN_ELEMENT_COUNTER)

                if all_elements_after_filtration == all_elements:
                    print('Счетчики исправны')
                    Actions.wait_time(self, time_to_wait=3)
                    print('Фильтр успешно применен')
                    Actions.close_site(self)

                else:
                    # неплохо вставить скриншот
                    print('Счетчики сломаны!')
                    Actions.close_site(self)

            else:
                # неплохо вставить скриншот
                print('Счетчики сломаны!')
                Actions.close_site(self)

        else:
            print('Пользователь не находится на странице /workspace')

        # Нужно понять как удобно свести все else к одному удобному списку

    def Apply_search_description(self, text_to_the_field):
        if self.driver.current_url == First_time.Locators.Page_adresses.WORKSPACE_PAGE:

            all_elements = Actions.save_counter_meaning(self,
                                                        locator=First_time.Locators.Workspace_Page_Locators.MAIN_ELEMENT_COUNTER)
            Actions.clean_the_field(self, locator=First_time.Locators.Workspace_Page_Locators.DESCRIPTION_SEARCH_FIELD)
            text_to_the_field_check = text_to_the_field
            Actions.add_text_to_the_field(self,
                                          locator=First_time.Locators.Workspace_Page_Locators.DESCRIPTION_SEARCH_FIELD,
                                          text=text_to_the_field)  # почему-то после применения данного метода значение вводимое в поле текст изменяется
            Actions.click_the_button(self, First_time.Locators.Workspace_Page_Locators.APPLY_FILTER_BUTTON)

            # Ожидание результата применения фильтра
            Actions.wait_time(self, time_to_wait=60)
            print('Фильтр "Поиск по описанию" применен')

            # нужно написать алгоритм, который будет пробегать через конкретный параметр
            elem_of_grid = Actions.save_string(self, locator=("xpath",
                                                              "//div[@class='app-mailBox-contentTab']/div[1]//div[@class='app-mailBox-item-link']//div[1]//div[2]//div[1]"))
            # //div[@class='app-mailBox-contentTab']/div[@class='app-mailBox-item table-success']//div[@class='app-mailBox-item-link']//div[1]//div[2]//div[1]
            # div 8  это параметр
            # //div[@class='app-mailBox-contentTab']/div[8]//div[@class='app-mailBox-item-link']//div[1]//div[2]//div[1]

            Actions.wait_time(self, time_to_wait=20)
            print(elem_of_grid)

            # приведение к нижнему регистру
            elem_of_grid = elem_of_grid.lower()
            text_to_the_field = text_to_the_field.lower

            if elem_of_grid.find(text_to_the_field_check) != -1:
                print("В первом элементе есть слово из фильтра")
            else:
                print("В первом элементе нет слова из фильтра")
        else:
            print('Пользователь не находится на странице /workspace')'''