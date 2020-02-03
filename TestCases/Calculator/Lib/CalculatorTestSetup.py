import Lib as Setup
import unittest


class CalculatorTestSetup(unittest.TestCase):

    __test__ = False
    window_size = "max"  # Can be set to 'max', 'full', (width, height).

    def setUp(self):
        # Setup method is launched to create browser session, with given params.

        setup = Setup.BaseTestSetup(self.window_size)

        self.action = setup.action
        self.driver = setup.driver

    def tearDown(self):
        # Tear down method it's launched to close browser session when Test has ended or failed.
        self.driver.quit()
