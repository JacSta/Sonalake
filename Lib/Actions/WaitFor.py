from .BaseActions import BaseActions


class WaitFor(BaseActions):
    """Class contains methods that allow to wait for element visibility etc..."""

    def element_invisible(self, element, msg=None, timeout=30):
        # Waits for given element to be invisible.
        if msg is None:
            msg = "After {} second given element is still visible. Element: {}".format(timeout, element)

        element_locator = element if self.is_web_element_instance(element) else (self.by.XPATH, element)

        try:
            self.wait(self.driver, timeout, 0.25).until(
                self.expected_condition.invisibility_of_element_located(element_locator)
            )
        except self.exception.TimeoutException:
            raise self.exception.TimeoutException(msg=msg)

    def element_visible(self, element, msg=None, timeout=30):
        # Waits for given element to be visible.
        if msg is None:
            msg = "After {} second given element is still not visible. Element: {}".format(timeout, element)

        try:
            return self.wait(self.driver, timeout, 0.25).until(
                _VisibilityOfElementLocated(element, self.driver)
            )
        except self.exception.TimeoutException:
            raise self.exception.TimeoutException(msg=msg)

    def element_to_be_clickable(self, element, msg=None, timeout=30):
        # Waits until given element is clickable.
        if msg is None:
            msg = "Element is not clickable. Element: {}".format(element)

        try:
            return self.wait(self.driver, timeout, 0.2).until(
                _ElementToBeClickAble(element, self.driver)
            )
        except self.exception.TimeoutException:
            raise self.exception.TimeoutException(msg=msg)


class _VisibilityOfElementLocated(BaseActions):
    # Custom visibility of element located.

    from .ElementVisibility import ElementVisibility
    get_element_visibility = ElementVisibility.get_element_visibility

    def __init__(self, locator, driver):
        super().__init__(driver)
        self.locator = locator

    def __call__(self, driver):
        ec = self.exception
        locator = self.locator
        try:
            if not self.is_web_element_instance(locator):
                locator = self.driver.find_element_by_xpath(locator)
            return self.get_element_visibility(locator)
        except (ec.NoSuchElementException, ec.StaleElementReferenceException):
            return False


class _ElementToBeClickAble(BaseActions):
    # Custom check if element is clickable

    def __init__(self, locator, driver):
        super().__init__(driver)
        self.locator = locator

    def __call__(self, driver):
        locator = self.locator
        if not self.is_web_element_instance(locator):
            locator = self.driver.find_element_by_xpath(locator)

        if locator.is_enabled():
            return locator
        else:
            return False
