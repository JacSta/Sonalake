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
        self._test_window_size_type(window_size)

        # Sets browser window size.
        self._set_browser_window_size(window_size)

        # Opens desired URL address.
        self.driver.get(self.start_page_url)

    def _test_is_driver_set(self):
        # Test is web driver is set.
        if self.driver is None:
            raise ValueError("Browser instance (web driver) must be set.")

    def _test_window_size_type(self, window_size):
        # Test type of window_size attribute.
        if isinstance(window_size, tuple):
            # If window_size is type of tuple than checks tuple item type and tuple length.
            if len(window_size) != 2:
                self.driver.quit()
                raise IndexError("Attribute window_size must have only two items.")

            for item in window_size:
                if not isinstance(item, int):
                    self.driver.quit()
                    raise ValueError("Tuple item must be int or str.")

        elif isinstance(window_size, str):
            # If window_size is type of str than checks if is equal to "max".
            try:
                assert window_size.lower() in ("max", "full")
            except AssertionError:
                self.driver.quit()
                raise AssertionError("If window_size is type of str, only value that is accept is 'MAX'.")

        else:
            # Raise error if window_size is different type than tuple, str.
            self.driver.quit()
            raise TypeError("Attribute window_size must be type of tuple or string.")

    def _set_browser_window_size(self, window):
        # Sets browser window size depends on given params.
        if window == "max":
            self.driver.maximize_window()
        elif window == "full":
            self.driver.fullscreen_window()
        elif isinstance(window, tuple):
            self.driver.set_window_position(0, 0)
            self.driver.set_window_size(window[0], window[1])
