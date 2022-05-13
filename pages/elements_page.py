import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data.data import InputData


class TextBoxPage(BasePage):
    input_data = InputData()

    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    OUTPUT_NAME = (By.CSS_SELECTOR, 'p[id="name"]')
    OUTPUT_EMAIL = (By.CSS_SELECTOR, 'p[id="email"]')
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'p[id="currentAddress"]')
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'p[id="permanentAddress"]')

    def filling_fields(self):
        full_name = self.input_data.NAME
        email = self.input_data.EMAIL
        current_address = self.input_data.ADDRESS.replace('\n', ' ')
        permanent_address = self.input_data.ADDRESS.replace('\n', ' ')
        self.send_keys(self.FULL_NAME, full_name)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.CURRENT_ADDRESS, current_address)
        self.send_keys(self.PERMANENT_ADDRESS, permanent_address)
        self.is_visible(self.SUBMIT_BUTTON).click()
        input_data = [full_name, email, current_address, permanent_address]

        return input_data

    def check_output_data(self):
        output_full_name = self.is_visible(self.OUTPUT_NAME).text.split(':')[1]
        output_email = self.is_visible(self.OUTPUT_EMAIL).text.split(':')[1]
        output_current_address = self.is_visible(self.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]
        output_permanent_address = self.is_visible(self.OUTPUT_PERMANENT_ADDRESS).text.split(':')[1]
        expected_data = [output_full_name, output_email, output_current_address, output_permanent_address]

        return expected_data


class CheckBoxPage(BasePage):
    EXPAND_BUTTON = (By.CSS_SELECTOR, 'button[class="rct-option rct-option-expand-all"]')
    ALL_CHECK_BOXES = (By.CSS_SELECTOR, 'span[class="rct-checkbox"]')
    SELECTED_CHECK_BOXES_TITLES = (By.XPATH, '//*[@class="rct-icon rct-icon-check"]/ancestor::label/child::span[@class="rct-title"]')
    OUTPUT_CHECK_BOXES_TITLES = (By.CSS_SELECTOR, 'span[class="text-success"]')

    def select_random_check_boxes(self):
        self.is_present(self.EXPAND_BUTTON).click()
        check_boxes = self.are_present(self.ALL_CHECK_BOXES)
        check_boxes_count = len(check_boxes)
        count = 0
        while count != check_boxes_count:
            random_number = random.randint(0, check_boxes_count - 1)
            random_check_box = check_boxes[random_number]
            random_check_box.click()
            count += 1

    def get_selected_check_boxes_titles(self):
        titles = self.are_present(self.SELECTED_CHECK_BOXES_TITLES)
        titles_list = []

        for title in titles:
            title_refactor = title.text.lower().replace('.doc', '').replace(' ', '')
            titles_list.append(title_refactor)

        return titles_list

    def get_output_check_boxes_titles(self):
        titles = self.are_present(self.OUTPUT_CHECK_BOXES_TITLES)
        titles_list = []

        for title in titles:
            title_refactor = title.text.lower()
            titles_list.append(title_refactor)

        return titles_list


class RadioButtonPage(BasePage):
    YES_RB = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
    IMPRESSIVE_RB = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
    NO_RB = (By.CSS_SELECTOR, 'label[for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')

    def click_on_radiobutton(self, radio_button):
        rb_name = {'yes': self.YES_RB,
                   'impressive': self.IMPRESSIVE_RB,
                   'no': self.NO_RB}

        self.is_clickable(rb_name[radio_button]).click()
        output_result = self.is_present(self.OUTPUT_RESULT).text

        return output_result


class WebTablesPage(BasePage):
    input_data = InputData()

    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT = (By.CSS_SELECTOR, 'input[id="department"]')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')
    TABLE_DATA = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')

    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'span[class="input-group-text"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    EDIT_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')

    def __fill_form_fields(self):
        first_name = self.input_data.FIRST_NAME
        last_name = self.input_data.LAST_NAME
        email = self.input_data.EMAIL
        age = self.input_data.AGE
        salary = self.input_data.SALARY
        department = self.input_data.DEPARTMENT

        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.AGE, age)
        self.send_keys(self.SALARY, salary)
        self.send_keys(self.DEPARTMENT, department)

        return [first_name, last_name, str(age), email, str(salary), department]

    def add_new_record(self):
        self.is_present(self.ADD_BUTTON).click()
        new_record_data = self.__fill_form_fields()
        self.is_clickable(self.SUBMIT_BUTTON).click()

        return new_record_data

    def get_table_data(self):
        table_elements = self.are_present(self.TABLE_DATA)
        table_data = []
        for row in table_elements:
            table_data.append(row.text.splitlines())

        return table_data

    def search_record(self, keys):
        self.send_keys(self.SEARCH_FIELD, keys)
        self.is_present(self.SEARCH_BUTTON).click()
        search_result = self.get_table_data()

        return search_result

    def delete_record(self):
        self.is_present(self.DELETE_BUTTON).click()

    def edit_record(self):

        self.is_present(self.EDIT_BUTTON).click()
        new_record_data = self.__fill_form_fields()
        self.is_clickable(self.SUBMIT_BUTTON).click()

        return new_record_data
