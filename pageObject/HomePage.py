from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(text(), 'Shop')]")
    checkOut = (By.XPATH, "//a[@class = 'nav-link btn btn-primary']")
    gettittles = (By.XPATH, "//div [@class='card h-100']")

    def shopItem(self):
        return self.driver.find_element(*HomePage.shop)

    def checkOutButton(self):
        return self.driver.find_element(*HomePage.checkOut)

    def getTittles(self):
        return self.driver.find_elements(*HomePage.gettittles)



