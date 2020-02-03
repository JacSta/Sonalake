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
            button.click()
        self.wait_for.element_invisible(self.locator.ELEMENT_history)

    def select_deg_rad(self, *args):
        Rad = self.wait_for.element_visible(self.locator.BUTTON_rad)
        Deg = self.wait_for.element_visible(self.locator.BUTTON_deg)
        if "Rad" in args:
            Rad.click()
        elif "Deg" in args:
            Deg.click()

    def clear_display(self):
        clear = self.wait_for.element_visible(self.locator.BUTTON_keypad.format('Clear'))
        clear.click()

    def assert_calc_result(self, expected):
        self.driver.refresh()
        result_locator = self.wait_for.element_visible(self.locator.RESULT_element)
        self.element_attribute.attribute_has_value(result_locator, "title", expected)

    def assert_history_of_caclulations(self, expected):
        calc_list = self.driver.find_elements_by_xpath(self.locator.CALCULATION_element)
        calc_value_list = []
        for item in calc_list:
            calc_value_item = self.element_attribute.has_attribute(item, "data-inp")
            calc_value_list.append(calc_value_item)
        calc_value_list.reverse()
        assert calc_value_list == expected
