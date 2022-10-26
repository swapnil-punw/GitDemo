from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    location = (By.XPATH, "//input[@id = 'country']")

    def Location(self):
        return self.driver.find_element(*CheckOutPage.location)

