from selenium import webdriver
from .BaseDriver import BaseDriver


class Driver(BaseDriver):
    """Class creates webdriver session based on given parameters from BaseDriver class."""

    def __init__(self):
        super().__init__()
        self.driver = self._session()  # Webdriver Session.

    def _session(self):
        # Creates browser session based on given config.
        _opt = self._headless_browser()

        # Creates local session.
        _session = webdriver.Chrome(options=_opt)
        _session.set_page_load_timeout(30)
        _session.set_script_timeout(30)

        return _session

    def _headless_browser(self):
        # Returns headless browser option if proper setting is True.

        _options = None
        if self.is_session_headless:

            # CHROME headless browser.
            args = ['--headless', '--no-sandbox', '--window-size=1366x768', '--disable-gpu',
                        '--ignore-certificate-errors', '--disable-extensions']

            # Adds arguments to chrome options.
            _options = webdriver.ChromeOptions()
            [_options.add_argument(arg) for arg in args]

        return _options
