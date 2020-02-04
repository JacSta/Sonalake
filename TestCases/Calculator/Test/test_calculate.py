from TestCases.Calculator.Lib import PageObjects as Page
from ..Lib.CalculatorTestSetup import CalculatorTestSetup
from ..TestData import test_data_calculate as Data


class TestCalculate(CalculatorTestSetup):

    __test__ = True

    def test_calculate(self):
        """
            1. Opens start page set in settings.py
            2. Performs calculation with first data set
            3. Asserts result
            4. Changes radio button from Degree to Radian
            5. Performs calculation with second data set
            6. Asserts result
            7. Changes radio button from Radian to Degree
            6. Performs calculation with third data set
            7. Asserts result
            8. Checks if 'History' drop down list contains proper calculations
        """
        cookies = Page.CookiesObject(self.driver)
        cookies.close_cookies_info()

        main = Page.MainPageObject(self.driver)
        expected_calc = Data.expected_calc()

        self._calculation("first_calc")
        main.select_deg_rad("Rad")
        self._calculation("second_calc")
        main.select_deg_rad("Deg")
        self._calculation("third_calc")
        main.assert_history_of_caclulations(expected_calc)

    def _calculation(self, number_calc):
        calc = Data.calculations()
        expected_res = Data.expected_results()
        main = Page.MainPageObject(self.driver)
        main.calculate(calc[number_calc])
        main.assert_calc_result(expected_res[number_calc])
        main.clear_display()
