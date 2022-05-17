import pytest

from pages.elements_page import TextBoxPage,CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage
from config import config


class TestTextBox:
    def test_filling_text_boxes(self, driver):
        text_box_page = TextBoxPage(driver)
        text_box_page.open(config.TEXT_BOX_URL)

        input_data = text_box_page.filling_fields()
        output_data = text_box_page.check_output_data()

        assert input_data == output_data, "input and output data don't match"


class TestCheckBox:
    def test_check_boxes(self, driver):
        check_box_page = CheckBoxPage(driver)
        check_box_page.open(config.CHECK_BOX_URL)

        check_box_page.select_random_check_boxes()
        selected_titles = check_box_page.get_selected_check_boxes_titles()
        output_titles = check_box_page.get_output_check_boxes_titles()

        assert selected_titles == output_titles, "Selected titles don't match with output titles"


class TestRadioButtons:
    def test_yes_radio_button(self, driver):
        rb_page = RadioButtonPage(driver)
        rb_page.open(config.RADIO_BUTTON_URL)
        output_result = rb_page.click_on_radiobutton('yes')

        assert output_result == 'Yes', "Radio button 'Yes' was not selected"

    def test_impressive_radio_button(self, driver):
        rb_page = RadioButtonPage(driver)
        rb_page.open(config.RADIO_BUTTON_URL)
        output_result = rb_page.click_on_radiobutton('impressive')

        assert output_result == 'Impressive', "Radio button 'Impressive' was not selected"

    def test_no_radio_button(self, driver):
        rb_page = RadioButtonPage(driver)
        rb_page.open(config.RADIO_BUTTON_URL)
        output_result = rb_page.click_on_radiobutton('no')

        assert output_result == 'No', "Radio button 'No' was not selected"


class TestWebTables:
    def test_add_new_record(self, driver):
        web_table_page = WebTablesPage(driver)
        web_table_page.open(config.WEB_TABLES_URL)

        new_record_data = web_table_page.add_new_record()
        table_data = web_table_page.get_table_data()

        assert new_record_data in table_data, 'New record not added'

    def test_search_record(self, driver):
        web_table_page = WebTablesPage(driver)
        web_table_page.open(config.WEB_TABLES_URL)

        email = web_table_page.add_new_record()[3]
        search_result = web_table_page.search_record(email)

        assert email in str(search_result), 'Record was not found in table'

    def test_delete_record(self, driver):
        web_table_page = WebTablesPage(driver)
        web_table_page.open(config.WEB_TABLES_URL)

        record_for_delete = web_table_page.add_new_record()[3]
        web_table_page.search_record(record_for_delete)
        web_table_page.delete_record()
        table_data = web_table_page.get_table_data()

        assert record_for_delete not in str(table_data), f'Record with data {record_for_delete} was not deleted'

    def test_edit_record(self, driver):
        web_table_page = WebTablesPage(driver)
        web_table_page.open(config.WEB_TABLES_URL)

        record_for_edit = web_table_page.add_new_record()[3]
        web_table_page.search_record(record_for_edit)
        new_data = web_table_page.edit_record()
        table_data = web_table_page.get_table_data()

        assert new_data in table_data, 'Data was not changed'

    @pytest.mark.parametrize('input_rows_count', [5, 10, 20, 25, 50, 100])
    def test_change_rows_count(self, driver, input_rows_count):
        web_table_page = WebTablesPage(driver)
        web_table_page.open(config.WEB_TABLES_URL)

        web_table_page.select_rows_count(input_rows_count)
        output_rows_count = web_table_page.check_rows_count()

        assert input_rows_count == output_rows_count

    @pytest.mark.parametrize('input_rows_count', [5, 10, 20, 25, 50, 100])
    def test_return_back_rows_count(self, driver, input_rows_count):
        web_table_page = WebTablesPage(driver)
        web_table_page.open(config.WEB_TABLES_URL)

        web_table_page.select_rows_count(input_rows_count)
        web_table_page.select_rows_count(10)
        output_rows_count = web_table_page.check_rows_count()

        assert output_rows_count == 10, 'Rows count was not returned back'


class TestButtons:
    @pytest.mark.parametrize('click_type, exp_output_message', [('double_click', 'You have done a double click'),
                                                                ('right_click', 'You have done a right click'),
                                                                ('click', 'You have done a dynamic click')])
    def test_various_clicks(self, driver, click_type, exp_output_message):
        buttons_page = ButtonsPage(driver)
        buttons_page.open(config.BUTTONS_URL)

        output_message = buttons_page.do_click(click_type)

        assert output_message == exp_output_message, 'Wrong click type'


class TestLinks:
    def test_new_tab_link(self, driver):
        links_page = LinksPage(driver)
        links_page.open(config.LINKS_URL)
        links_page.new_tab_link()
        current_url = links_page.current_url()

        assert current_url == 'https://demoqa.com/', "Link was not open in a new tab"
