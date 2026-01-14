from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from BroswerUtili.browserutili import Repeat


class shop_check(Repeat):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
        self.name=(By.XPATH,"(//input[@name='name'])[1]")
        self.email=(By.XPATH,"//input[@name='email']")
        self.pwd=(By.CSS_SELECTOR,"#exampleInputPassword1")
        self.checkeg=(By.CSS_SELECTOR,"#exampleCheck1")
        self.dropdown=(By.CSS_SELECTOR,"#exampleFormControlSelect1")
        self.radio=(By.CSS_SELECTOR,"#inlineRadio2")
        self.bday=(By.XPATH,"//input[@name='bday']")
        self.month=(By.XPATH,"//input[@type='submit']")


    def shop_logic(self,name,email,pwd,date):
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.pwd).send_keys(pwd)
        self.driver.find_element(*self.checkeg).click()
        self.driver.save_screenshot("shop1.png")

        er = Select(self.driver.find_element(*self.dropdown))
        er.select_by_index(1)

        self.driver.find_element(*self.radio).click()
        self.driver.find_element(*self.bday).send_keys(date)
        self.driver.find_element(*self.month).click()
        self.driver.save_screenshot("shop2.png")


