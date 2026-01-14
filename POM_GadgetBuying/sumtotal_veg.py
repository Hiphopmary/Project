from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BroswerUtili.browserutili import Repeat


class sumtotal(Repeat):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.price_list=(By.XPATH, "//table[@class='cartTable']/tbody/tr/td[5]")
        self.validation=(By.XPATH, "//span[@class='totAmt']")
        self.invalid_promo=(By.XPATH, "//input[@class='promoCode']")
        self.invalid_promoclick=(By.XPATH, "//button[@class='promoBtn']")
        self.invalid_msg=(By.XPATH, "//span[text()='Invalid code ..!']")
        self.clear=(By.XPATH, "//input[@class='promoCode']")
        self.valid_promo = (By.XPATH, "//input[@class='promoCode']")
        self.valid_promoclick = (By.XPATH, "//button[@class='promoBtn']")
        self.valid_msg = (By.XPATH,"//span[text()='Code applied ..!']")
        self.discount=(By.XPATH,"//span[@class='discountPerc']")
        self.total=(By.XPATH,"//span[@class='discountAmt']")
        self.order_place=(By.XPATH,"//button[text()='Place Order']")
        self.sumtotal=0
        self.count = 0


    def summation(self):

        price_item = self.driver.find_elements(*self.price_list)
        print(f"There is {len(price_item)} in the table or selected items")


        for p in price_item:
            self.sumtotal = self.sumtotal + int(p.text)
            self.count  = self.count  + 1
        print(f"The total sum of {len(price_item)} is {self.sumtotal}")
        print(f"The count are : {self.count}")

        assert int(self.driver.find_element(*self.validation).text) == self.sumtotal
        print("total sum is matching from  list")
        self.driver.save_screenshot("summation.png")

    def message(self,invalid_promo_name,valid_promo_name):

        self.driver.find_element(*self.invalid_promo).send_keys(invalid_promo_name)
        self.driver.find_element(*self.invalid_promoclick).click()
        wait = WebDriverWait(self.driver, 10)
        message1 = wait.until(EC.presence_of_element_located((self.invalid_msg))).text
        print(message1)
        self.driver.save_screenshot("message1.png")




        self.driver.find_element(By.XPATH,"//input[@class='promoCode']").clear()

        self.driver.find_element(*self.valid_promo).send_keys(valid_promo_name)
        self.driver.find_element(*self.valid_promoclick).click()
        wait = WebDriverWait(self.driver, 10)
        message2 = wait.until(EC.presence_of_element_located((self.valid_msg))).text
        print(message2)
        self.driver.save_screenshot("message2.png")


    def cal(self):

        discount= self.driver.find_element(*self.discount).text
        print(f"the discount value is : {discount}")
        val=int(discount.strip("%"))
        v=float((self.sumtotal*val)/100)

        Cal=float(self.sumtotal)-v
        compare=float(self.driver.find_element(*self.total).text)
        print(Cal)
        print(compare)


        assert Cal == compare
        print(f"total amount :{Cal} is matching form list{compare}")

        self.driver.find_element(*self.order_place).click()
        self.driver.save_screenshot("cal.png")











