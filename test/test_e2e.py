import pytest

from pageObject.CheckoutPage import CheckOutPage
from pageObject.ConfirmPage import ConfirmPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# driver = None

class TestOne(BaseClass):
    def test_e2e(self):
        homePage = HomePage(self.driver)
        # homePage.shopItem().click()
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Shop')]").click()
        # mobiles = self.driver.find_elements(By.XPATH, "//div [@class='card h-100']")
        mobiles = homePage.getTittles()
        for mobile in mobiles:
            if mobile.find_element(By.XPATH, "div[1]/h4/a").text == "Blackberry":
                mobile.find_element(By.XPATH, "div[2]/button").click()
                break

        # self.driver.find_element(By.XPATH, "//a[@class = 'nav-link btn btn-primary']").click()
        homePage.checkOutButton().click()

        # self.driver.find_element(By.XPATH, "//*[@class = 'btn btn-success']").click()
        confirmPage = ConfirmPage(self.driver)
        confirmPage.CheckButton().click()

        # self.driver.find_element(By.XPATH, "//input[@id = 'country']").send_keys("Ind")

        checkPage = CheckOutPage(self.driver)
        checkPage.Location().send_keys("Ind")

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='India']")))
        self.verifyElement("//*[text()='India']")
        self.driver.find_element(By.XPATH, "//*[text()='India']").click()
        self.driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@type= 'submit']").click()
        massage = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

        assert "Success" in massage
