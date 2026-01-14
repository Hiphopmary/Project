from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC

from BroswerUtili.browserutili import Repeat
from POM_GadgetBuying.sumtotal_veg import sumtotal


class vegcart(Repeat):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.keyword=(By.CSS_SELECTOR, ".search-keyword")
        self.button=(By.CSS_SELECTOR, ".search-button")
        self.condition=(By.XPATH, "//div[@class='product']")
        self.increment=(By.XPATH, ".//a[@class='increment']")
        self.addtocart=(By.XPATH, ".//button[text()='ADD TO CART']")
        self.option=(By.XPATH, "//img[@alt='Cart']")
        self.checkout=(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def vegsearch(self,value):
        self.driver.find_element(*self.keyword).send_keys(value)
        self.driver.find_element(*self.button).click()
        self.driver.save_screenshot("vegsearch.png")

    def vegcarting(self):
        wait=WebDriverWait(self.driver,10)
        veg = wait.until(EC.presence_of_all_elements_located((self.condition)))
        print(len(veg))
        for a in veg:
            a.find_element(*self.increment).click()
            a.find_element(*self.addtocart).click()
        self.driver.save_screenshot("vegcarting.png")

    def cartoption(self):
        self.driver.find_element(*self.option).click()
        self.driver.find_element(*self.checkout).click()
        self.driver.save_screenshot("cartoption.png")
        st=sumtotal(self.driver)
        return st


