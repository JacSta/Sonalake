from Lib.Actions import Actions
from ..PageLocators import CookiesLocators


class CookiesObject(Actions):
    """
        Class contains locators for cookies policy element.
    """
    def __init__(self, driver):
        super().__init__(driver)

        cookies_locator = CookiesLocators()
        self.container = self.wait_for.element_visible(cookies_locator.CONTAINER_cookies)
        self.close_button = self.driver.find_element_by_xpath(cookies_locator.BUTTON_accept_cookies)

    def close_cookies_info(self):
        self.close_button.click()
        self.wait_for.element_invisible(self.container)
