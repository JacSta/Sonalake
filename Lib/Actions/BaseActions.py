import time
from selenium.common import exceptions
from selenium.webdriver.common import (keys, action_chains, by)
from selenium.webdriver.support import (select, expected_conditions, wait)
from selenium.webdriver.remote.webdriver import WebElement


class BaseActions(object):
    """Base class with selenium and helpers actions."""

    def __init__(self, driver):
        self.driver = driver

        # selenium.common
        self.exception = exceptions

        # selenium.webdriver.common
        self.action_chains = action_chains.ActionChains(self.driver)
        self.key = keys.Keys()
        self.by = by.By()

        # selenium.webdriver.support
        self.select = select.Select
        self.wait = wait.WebDriverWait
        self.expected_condition = expected_conditions

        # other libs
        self.time = time

    @staticmethod
    def is_web_element_instance(element):
        # Checks if given element was already found by `find_element` (etc...).
        # Returns True/False if element is or isn't instance of WebElement.
        return isinstance(element, WebElement)

    def get_element_locator(self, element):
        """
        Gets element locator.
        Checks if given element is web element instance, if not searches for it with find_element_by_xpath method.
        """
        return element if self.is_web_element_instance(element) else self.driver.find_element_by_xpath(element)
