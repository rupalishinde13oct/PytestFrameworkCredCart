import time

from selenium.webdriver.common.by import By

from PageObjects.LoginPage import LoginPage
from Utility.Logger import Logger
from Utility.readConfig import ReadConfig
from PageObjects.ProductPurchaseAndCheckout import ProductPurchase
class TestValidateCalculations:

    url = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = Logger.get_Logger()

    def test_Validate_Calculations_006(self , setup):
        self.log.info("test_Validate_Calculations_006 is Started")
        self.d = setup
        self.log.info("Launching Browser..!!")
        self.d.get(self.url)
        self.log.info("Go to-->" + self.url)

        lp = LoginPage(self.d)
        lp.Click_On_Login_Link()
        self.log.info("Clicking on Login Link")
        lp.Enter_Email(self.username)
        self.log.info("Entering Username-->" + self.username)
        lp.Enter_Password(self.password)
        self.log.info("Entering Password-->" + self.password)
        lp.Click_On_Login_Button()
        self.log.info("Clicking on Login Button")

        pp = ProductPurchase(self.d)
        pp.Click_On_Apple_MacBookPro()
        self.log.info("Clicking on Apple MacbookPro product")
        pp.Click_On_AddToCart()
        self.log.info("Added to Cart")
        pp.Click_On_Continue_SHopping()
        self.log.info("Clicked on Continue Shopping")
        pp.Click_On_Guitar()
        self.log.info("Clicking on Guitar")
        pp.Click_On_AddToCart()
        self.log.info("Added to Cart")
        pp.Click_On_Continue_SHopping()
        self.log.info("Clicked on Continue Shopping")
        pp.Click_On_HeadPhones()
        self.log.info("Clicking on HeadPhones")
        pp.Click_On_AddToCart()
        self.log.info("Added to Cart")
        pp.Click_On_Continue_SHopping()
        self.log.info("Clicked on Continue Shopping")
        pp.Click_On_IPad()
        self.log.info("Clicking on IPad")
        pp.Click_On_AddToCart()
        self.log.info("Added to Cart")
        time.sleep(5)

        rows = len(self.d.find_elements(By.XPATH , "//tbody/tr"))
        Actual_prices = []
        Expected_Prices = []
        for i in range(1,rows-2):
            cost = self.d.find_element(By.XPATH , "//tbody/tr["+str(i)+"]/td[4]").text
            cost = round(float(cost[1:]) , 2)
            Actual_prices.append(cost)
        print(Actual_prices)

        Actual_SubTotal = round(sum(Actual_prices) , 2)
        Actual_Tax = round(Actual_SubTotal *(13/100) , 2)
        Actual_GrandTotal =  Actual_SubTotal + Actual_Tax
        self.log.info("Creating list for Actual Prices")

        for i in range(rows-2,rows+1 ):
            cost = self.d.find_element(By.XPATH, "//tbody/tr[" + str(i) + "]/td[4]").text
            cost = cost[1:]
            cost = cost.replace(',' , '')
            Expected_Prices.append(float(cost))
        print(Expected_Prices)

        Expected_SubTotal = Expected_Prices[0]
        Expected_Tax = Expected_Prices[1]
        Expected_GrandTotal = Expected_Prices[2]
        self.log.info("Create list for Expected Prices")

        self.log.info("Compare Actual Prices with Expected ones")
        if Actual_SubTotal == Expected_SubTotal and Actual_Tax == Expected_Tax and Actual_GrandTotal == Expected_GrandTotal:
            print("Values are Matching--!!")
            self.log.info("Calculations are matched")
            self.log.info("test_Validate_Calculations_006 is Passed")
            self.d.save_screenshot \
                ("D:\\Rupali Prathamesh Pandit\\CredCart2\\Screenshots\\test_Validate_Calculations_006_Pass.png")
            assert True

        else:
            print("Values did not Matched--!!")
            self.log.info("Calculations did not matched")
            self.log.info("test_Validate_Calculations_006 is Failed")
            self.d.save_screenshot \
                ("D:\\Rupali Prathamesh Pandit\\CredCart2\\Screenshots\\test_Validate_Calculations_006_Fail.png")
            assert False
