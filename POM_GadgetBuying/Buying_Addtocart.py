from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BroswerUtili.browserutili import Repeat
from POM_GadgetBuying.Buying_checkout import checkout


class add_to_cart(Repeat):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.list_items=(By.XPATH,"//app-card-list[@class='row']/app-card")
        self.label_of_items=(By.XPATH,".//h4/a")
        self.cart_button=(By.XPATH,".//button[text()='Add ']")


    def cart_logic(self,Label_Match):
        wait = WebDriverWait(self.driver, 20)
        poi = wait.until(EC.presence_of_all_elements_located((self.list_items)))
        print(len(poi))
        for a in poi:
            sas = a.find_element(*self.label_of_items).text.strip()
            if sas == Label_Match :
                a.find_element(*self.cart_button).click()
                self.driver.save_screenshot("cart.png")
                break

        check=checkout(self.driver)
        return check
