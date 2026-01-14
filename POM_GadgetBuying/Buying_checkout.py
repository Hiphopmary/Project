from selenium.webdriver.common.by import By

from BroswerUtili.browserutili import Repeat
from POM_GadgetBuying.Buying_submit import validation


class checkout(Repeat):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.checking=(By.XPATH,"//a[@class='nav-link btn btn-primary']")
        self.checkout=(By.XPATH,"//button[@class='btn btn-success']")

    def checkout_logic(self):
        self.driver.find_element(*self.checking).click()
        self.driver.find_element(*self.checkout).click()
        self.driver.save_screenshot("checkout.png")
        submit = validation(self.driver)
        return submit

