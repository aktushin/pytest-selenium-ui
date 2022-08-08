import allure
import pytest

from pages.ui.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage
from cfg import config


@pytest.mark.ui
@allure.suite('Test Elements block')
class TestTextBox:
    @allure.title('Filling text box fields')
    @allure.description
    def test_filling_text_boxes(self, driver):
        """Filling all text fields"""

        text_box_page = TextBoxPage(driver)
        text_box_page.open(config.TEXT_BOX_URL)

        input_data = text_box_page.filling_fields()
        output_data = text_box_page.check_output_data()

        assert input_data == output_data, "input and output data don't match"

@pytest.mark.ui
@allure.suite('Test Elements block')
class TestCheckBox:
    @allure.title('Test check boxes')
    @allure.description
    def test_check_boxes(self, driver):
        """Select random check boxes and assert that output titles match"""

        check_box_page = CheckBoxPage(driver)
        check_box_page.open(config.CHECK_BOX_URL)

        check_box_page.select_random_check_boxes()
        selected_titles = check_box_page.get_selected_check_boxes_titles()
        output_titles = check_box_page.get_output_check_boxes_titles()

        assert selected_titles == output_titles, "Selected titles don't match with output titles"

@pytest.mark.ui
@allure.suite('Test Elements block')
class TestRadioButtons:
    @allure.title('Click on yes radiobutton')
    @allure.description
    def test_yes_radio_button(self, driver):
        """Check that 'Yes' radiobutton works"""

        rb_page = RadioButtonPage(driver)
        rb_page.open(config.RADIO_BUTTON_URL)
        output_result = rb_page.click_on_radiobutton('yes')

        assert output_result == 'Yes', "Radio button 'Yes' was not selected"

    @allure.title('Click on impressive radiobutton')
    @allure.description
    def test_impressive_radio_button(self, driver):
        """Check that 'Impressive' radiobutton works"""

        rb_page = RadioButtonPage(driver)
        rb_page.open(config.RADIO_BUTTON_URL)
        output_result = rb_page.click_on_radiobutton('impressive')

        assert output_result == 'Impressive', "Radio button 'Impressive' was not selected"

    @allure.title('Click on no radiobutton')
    @allure.description
    def test_no_radio_button(self, driver):
        """Check that 'No' radiobutton works"""

        rb_page = RadioButtonPage(driver)
        rb_page.open(config.RADIO_BUTTON_URL)
        output_result = rb_page.click_on_radiobutton('no')

        assert output_result == 'No', "Radio button 'No' was not selected"

@pytest.mark.ui
@allure.suite('Test Elements block')
class TestWebTables:
    @allure.title('Add new record in table')
    @allure.description
    def test_add_new_record(self, driver):
        """Adding new record and assert that it in table"""

        web_table_page = WebTablesPage(driver)
        web_table_page.open(config.WEB_TABLES_URL)

        new_record_data = web_table_page.add_new_record()
        table_data = web_table_page.get_table_data()

        assert new_record_data in table_data, 'New record not added'

    @allure.title('Search record')
    @allure.description
    def test_search_record(self, driver):
        """Search record in table by email"""

        web_table_page = WebTablesPage(driver)
        web_table_page.open(config.WEB_TABLES_URL)

        email = web_table_page.add_new_record()[3]
        search_result = web_table_page.search_record(email)

        assert email in str(search_result), 'Record was not found in table'

    @allure.title('Delete record from table')
    @allure.description
    def test_delete_record(self, driver):
        """Delete record from table"""

        web_table_page = WebTablesPage(driver)
        web_table_page.open(config.WEB_TABLES_URL)

        record_for_delete = web_table_page.add_new_record()[3]
        web_table_page.search_record(record_for_delete)
        web_table_page.delete_record()
        table_data = web_table_page.get_table_data()

        assert record_for_delete not in str(table_data), f'Record with data {record_for_delete} was not deleted'

    @allure.title('Edit record')
    @allure.description
    def test_edit_record(self, driver):
        """Edit record and check that fields are fields have changed in the table """

        web_table_page = WebTablesPage(driver)
        web_table_page.open(config.WEB_TABLES_URL)

        record_for_edit = web_table_page.add_new_record()[3]
        web_table_page.search_record(record_for_edit)
        new_data = web_table_page.edit_record()
        table_data = web_table_page.get_table_data()

        assert new_data in table_data, 'Data was not changed'

    @allure.title('Change rows count')
    @allure.description
    @pytest.mark.parametrize('input_rows_count', [5, 10, 20, 25, 50, 100])
    def test_change_rows_count(self, driver, input_rows_count):
        """Select rows count from 5 to 100 """

        web_table_page = WebTablesPage(driver)
        web_table_page.open(config.WEB_TABLES_URL)

        web_table_page.select_rows_count(input_rows_count)
        output_rows_count = web_table_page.check_rows_count()

        assert input_rows_count == output_rows_count

    @allure.title('Return back rows count')
    @allure.description
    @pytest.mark.parametrize('input_rows_count', [5, 10, 20, 25, 50, 100])
    def test_return_back_rows_count(self, driver, input_rows_count):
        """Select rows count from list and after trying to return them back"""

        web_table_page = WebTablesPage(driver)
        web_table_page.open(config.WEB_TABLES_URL)

        web_table_page.select_rows_count(input_rows_count)
        web_table_page.select_rows_count(10)
        output_rows_count = web_table_page.check_rows_count()

        assert output_rows_count == 10, 'Rows count was not returned back'

@pytest.mark.ui
@allure.suite('Test Elements block')
class TestButtons:
    click_type_and_expected_msg = [('double_click', 'You have done a double click'),
                                   ('right_click', 'You have done a right click'),
                                   ('click', 'You have done a dynamic click')]

    @allure.title('Test various clicks')
    @allure.description
    @pytest.mark.parametrize('click_type, exp_output_message', click_type_and_expected_msg)
    def test_various_clicks(self, driver, click_type, exp_output_message):
        """Testing doubleclick, right click and click buttons"""

        buttons_page = ButtonsPage(driver)
        buttons_page.open(config.BUTTONS_URL)

        output_message = buttons_page.do_click(click_type)

        assert output_message == exp_output_message, 'Wrong click type'

@pytest.mark.ui
@allure.suite('Test Elements block')
class TestLinks:
    @allure.title('New tab link')
    @allure.description
    def test_new_tab_link(self, driver):
        """Click on link which should open in a new tab """

        links_page = LinksPage(driver)
        links_page.open(config.LINKS_URL)
        links_page.new_tab_link()
        current_url = links_page.current_url()

        assert current_url == 'https://demoqa.com/', "Link was not opened in a new tab"
