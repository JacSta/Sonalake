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
