from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BroswerUtili.browserutili import Repeat
from POM_GadgetBuying.Buying_shop_check import shop_check



class validation(Repeat):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.country=(By.CSS_SELECTOR,"#country")
        self.validation=(By.XPATH,"//a[text()='India']")
        self.checkbox=(By.XPATH,"//label[@for='checkbox2']")
        self.purchase=(By.XPATH,"//input[@value='Purchase']")
        self.alert_message=(By.CSS_SELECTOR,".alert")
        self.close=(By.CSS_SELECTOR,".close")
        self.shop=(By.XPATH,"(//a[@class='navbar-brand']) [2]")

    def submit_logic(self,country):
        self.driver.find_element(*self.country).send_keys(country)
        wait = WebDriverWait(self.driver, 10)
        value = wait.until(EC.presence_of_element_located((self.validation)))
        value.click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.purchase).click()
        print(self.driver.find_element(*self.alert_message).text)
        self.driver.find_element(*self.close).click()
        self.driver.find_element(*self.shop).click()
        self.driver.save_screenshot("submit.png")
        shopcheck = shop_check(self.driver)
        return shopcheck



