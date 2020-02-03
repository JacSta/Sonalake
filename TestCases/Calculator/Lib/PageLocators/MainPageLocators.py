class MainPageLocators(object):
    CONTAINER = "//div[@id='calccontainer']"

    BUTTON_keypad = "//button[@id='Btn{}']"

    BUTTON_deg = "//label[@title='Degree']//input[@id='trigodeg']"
    BUTTON_rad = "//label[@title='Radian']//input[@id='trigorad']"

    INPUT_main = "//input[@id='input']"

    ELEMENT_history = "//button[contains(text(),'History')]"

    RESULT_element = "//div[@id='histframe']/ul/li[1]/p[@class='r']"
    CALCULATION_element = "//div[@id='histframe']/ul/li/p[@class='l']"
