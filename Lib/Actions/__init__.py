from .ElementVisibility import ElementVisibility
from .ElementAttributes import ElementAttributes
from .WaitFor import WaitFor
from .BaseActions import BaseActions


class Actions(BaseActions):
    # Contains all actions for page objects and tests.
    # Each new action must be imported and initialize in this class.

    def __init__(self, driver):
        super().__init__(driver)
        self.element_visibility = ElementVisibility(driver)
        self.element_attribute = ElementAttributes(driver)
        self.wait_for = WaitFor(driver)
