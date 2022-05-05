import time

from pages.elements_page import TextBoxPage
from config.config import TEXT_BOX_URL


class TestElementsPage:
    def test_filling_text_boxes(self, driver):
        page = TextBoxPage(driver)
        page.open(TEXT_BOX_URL)
        input_data = page.filling_fields()
        output_data = page.check_output_data()

        assert input_data == output_data

        time.sleep(4)
