# self.driver.find_element(By.XPATH, "//*[@class = 'btn btn-success']").click()

from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    checkOutButton = (By.XPATH, "//*[@class = 'btn btn-success']")

    def CheckButton(self):
        return self.driver.find_element(*ConfirmPage.checkOutButton)
