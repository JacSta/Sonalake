from TestCases.Calculator.Lib import PageObjects as Page
from ..Lib.CalculatorTestSetup import CalculatorTestSetup
from ..TestData import test_data_calculate as Data

class TestCalculate(CalculatorTestSetup):

    __test__ = True

    def test_calculate(self):
        """
            1. Opens home page
            2. Types given password into Password input element
            3. Clicks 'Continue' button
            4. Checks if Main Page of shared folder is visible
        """
        cookies = Page.CookiesObject(self.driver)
        cookies.close_cookies_info()
        main = Page.MainPageObject(self.driver)
        Calc = Data.calculations()
        Expected_res = Data.expected_results()
        Expected_calc = Data.expected_calc()

        main.calculate(Calc["first_calc"])
        main.assert_calc_result(Expected_res["first_calc"])
        main.clear_display()
        main.select_deg_rad("Rad")
        main.calculate(Calc["second_calc"])
        main.assert_calc_result(Expected_res["second_calc"])
        main.clear_display()
        main.select_deg_rad("Deg")
        main.calculate(Calc["third_calc"])
        main.assert_calc_result(Expected_res["third_calc"])
        main.clear_display()
        main.assert_history_of_caclulations(Expected_calc)
