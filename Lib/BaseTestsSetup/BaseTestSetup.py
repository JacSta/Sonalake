from ..DriverSession.Driver import Driver
from ..Actions.BaseActions import BaseActions
from settings import start_url


class BaseTestSetup(Driver):
    """Base class for setting up tests. All Test setup class (for selenium tests) must inherit from this!"""

    def __init__(self, window_size):
        super().__init__()

        self.start_page_url = start_url

        self.action = BaseActions(self.driver)

        # Test basic parameters.
        self._test_is_driver_set()

        # Sets browser window size to full screen
        self.driver.maximize_window()

        # Opens desired URL address.
        self.driver.get(self.start_page_url)

    def _test_is_driver_set(self):
        # Test is web driver is set.
        if self.driver is None:
            raise ValueError("Browser instance (web driver) must be set.")
