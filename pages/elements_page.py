import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data.data import TextBoxData


class TextBoxPage(BasePage):
    input_data = TextBoxData()

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
