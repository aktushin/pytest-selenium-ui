import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage
from config.config import TEXT_BOX_URL, CHECK_BOX_URL, RADIO_BUTTON_URL


class TestElementsPage:
    class TestTextBox:
        def test_filling_text_boxes(self, driver):
            text_box_page = TextBoxPage(driver)
            text_box_page.open(TEXT_BOX_URL)
            input_data = text_box_page.filling_fields()
            output_data = text_box_page.check_output_data()

            assert input_data == output_data, "input and output data don't match"

    class TestCheckBox:
        def test_check_boxes(self, driver):
            check_box_page = CheckBoxPage(driver)
            check_box_page.open(CHECK_BOX_URL)

            check_box_page.select_random_check_boxes()
            selected_titles = check_box_page.get_selected_check_boxes_titles()
            output_titles = check_box_page.get_output_check_boxes_titles()

            assert selected_titles == output_titles

    class TestRadioButtons:
        def test_yes_radio_button(self, driver):
            rb_page = RadioButtonPage(driver)
            rb_page.open(RADIO_BUTTON_URL)
            output_result = rb_page.click_on_yes_rb()

            assert output_result == 'Yes'

        def test_impressive_radio_button(self, driver):
            rb_page = RadioButtonPage(driver)
            rb_page.open(RADIO_BUTTON_URL)
            output_result = rb_page.click_on_impressive_rb()

            assert output_result == 'Impressive'

        def test_no_radio_button(self, driver):
            rb_page = RadioButtonPage(driver)
            rb_page.open(RADIO_BUTTON_URL)
            output_result = rb_page.click_on_no_rb()

            assert output_result
