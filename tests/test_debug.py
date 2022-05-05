import time

from pages.elements_page import TextBoxPage, CheckBoxPage
from config.config import TEXT_BOX_URL, CHECK_BOX_URL


class TestElementsPage:
    def test_check_boxes(self, driver):
        check_box_page = CheckBoxPage(driver)
        check_box_page.open(CHECK_BOX_URL)

        check_box_page.select_random_check_boxes()
        selected_titles = check_box_page.get_selected_check_boxes_titles()
        output_titles = check_box_page.get_output_check_boxes_titles()

        assert selected_titles == output_titles

