from .BaseActions import BaseActions


class ElementVisibility(BaseActions):
    """Class contains helpers to Test if element is visible or not.
    It's not waiter class, none of this methods should wait for element to be visible.
    If element is not visible for user then error will be raised."""

    def get_element_visibility(self, element):
        # Returns info about element visibility without raising error.
        try:
            return self.get_element_locator(element)
        except self.exception.NoSuchElementException:
            print("Given element {} is not visible".format(element))
            return False

    def is_element_visible(self, element, error_msg="Given element is not visible!"):
        # Checks if given element is visible. Returns True if element was visible.
        element_locator = self.get_element_visibility(element)

        def _raise_exception(_error_msg, _element):
            raise self.exception.ElementNotVisibleException(msg="{} | element: {}".format(_error_msg, _element))

        if isinstance(element_locator, bool):
            if not element_locator:
                _raise_exception(error_msg, element)
        elif not element_locator.is_displayed():
            _raise_exception(error_msg, element)

        return True

    def is_element_not_visible(self, element, error_msg="Given element is not visible!"):
        # Checks if given element is not visible. Returns True if element wasn't visible
        element_locator = self.get_element_visibility(element)

        def _raise_exception(_error_msg, _element):
            raise self.exception.NoSuchElementException(msg="{} | element: {}".format(_error_msg, _element))

        if isinstance(element_locator, bool):
            if element_locator:
                _raise_exception(error_msg, element)
        elif element_locator.is_displayed():
                _raise_exception(error_msg, element)

        return True
