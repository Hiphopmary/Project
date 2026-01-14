from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from BroswerUtili.browserutili import Repeat
from POM_GadgetBuying.Buying_Addtocart import add_to_cart



class login_page(Repeat):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.username=(By.CSS_SELECTOR,"#username")
        self.password=(By.CSS_SELECTOR,"#password")
        self.dropdown=(By.XPATH,"//select[@data-style='btn-info']")
        self.terms=(By.CSS_SELECTOR,"#terms")
        self.button=(By.CSS_SELECTOR,"#signInBtn")

    def login(self,username,paswwrod):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(paswwrod)
        obj1 = Select(self.driver.find_element(*self.dropdown))
        obj1.select_by_index(0)
        self.driver.find_element(*self.terms).click()
        self.driver.find_element(*self.button).click()
        self.driver.save_screenshot("login.png")
        cart=add_to_cart(self.driver)
        return cart














