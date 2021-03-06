from Lib.Actions import Actions
from ..PageLocators import MainPageLocators


class MainPageObject(Actions):
    def __init__(self, driver):
        super().__init__(driver)

        self.locator = MainPageLocators()
        self.container = self.wait_for.element_visible(self.locator.CONTAINER)

    def calculate(self, sequence):
        for item in sequence:
            button = self.wait_for.element_visible(self.locator.BUTTON_keypad.format(item))
            self.wait_for.element_to_be_clickable(button)
            button.click()
        self.wait_for.element_invisible(self.locator.ELEMENT_history)

    def select_deg_rad(self, *args):
        rad = self.wait_for.element_visible(self.locator.BUTTON_rad)
        deg = self.wait_for.element_visible(self.locator.BUTTON_deg)
        if "Rad" in args:
            rad.click()
        elif "Deg" in args:
            deg.click()

    def clear_display(self):
        clear = self.wait_for.element_visible(self.locator.BUTTON_keypad.format('Clear'))
        clear.click()

    def assert_calc_result(self, expected):
        self.driver.refresh()
        result_locator = self.wait_for.element_visible(self.locator.RESULT_element)
        self.element_attribute.attribute_has_value(result_locator, "title", expected)

    def assert_history_of_caclulations(self, expected):
        history= self.wait_for.element_visible(self.locator.BUTTON_history_list_down)
        history.click()
        calc_list = self.driver.find_elements_by_xpath(self.locator.CALCULATION_element)
        calc_value_list = []
        for item in calc_list:
            calc_value_item = self.element_attribute.has_attribute(item, "data-inp")
            calc_value_list.append(calc_value_item)
        calc_value_list.reverse()
        assert calc_value_list == expected
