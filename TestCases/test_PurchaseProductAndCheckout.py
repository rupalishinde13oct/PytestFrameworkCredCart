import time

from PageObjects.LoginPage import LoginPage
from Utility.Logger import Logger
from Utility.readConfig import ReadConfig
from PageObjects.ProductPurchaseAndCheckout import ProductPurchase

class TestPurchaseProduct:

    url = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = Logger.get_Logger()

    def test_PurchaseProduct_005(self , setup):
        self.log.info("test_PurchaseProduct_005 is Started")
        self.d = setup
        self.log.info("Launching Browser..!!")
        self.d.get(self.url)
        self.log.info("Go to-->"+self.url)

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
        pp.Click_On_Proceed_To_Checkout()
        self.log.info("Clicking on Proceed to Checkout")

        pp.Enter_FirstName("Rupali")
        self.log.info("Entering First Name")
        pp.Enter_LastName("Pandit")
        self.log.info("Entering Last Name")
        pp.Enter_Phone(5895647852)
        self.log.info("Entering  Phone Number")
        pp.Enter_Address("Pune Maharashtra")
        self.log.info("Entering Address")
        pp.Enter_ZipCode(522365)
        self.log.info("Entering Zip Code")
        pp.Select_State(1)
        self.log.info("Selecting State")
        pp.Enter_OwnerName("Rupali")
        self.log.info("Entering Owner Name")
        pp.Enter_CVV("043")
        self.log.info("Entering CVV")
        pp.Enter_CardNumber("5281")
        pp.Enter_CardNumber("0370")
        pp.Enter_CardNumber("4891")
        pp.Enter_CardNumber("6168")
        self.log.info("Entering Card Number")
        pp.Enter_ExpiryYear(1)
        self.log.info("Entering Expiry Year")
        pp.Enter_ExpiryMonth(1)
        self.log.info("Entering Expiry Month")
        time.sleep(2)
        pp.Click_On_Continue_To_Checkout()
        self.log.info("Clicking on Continue to checkout")
        time.sleep(3)
        if pp.Success_Status() == True:
            self.log.info("test_PurchaseProduct_005 is Passed")
            self.d.save_screenshot\
                ("D:\\Rupali Prathamesh Pandit\\CredCart2\\Screenshots\\test_PurchaseProduct_005_Pass.png")
            assert True
        else:
            self.log.info("test_PurchaseProduct_005 is Failed")
            self.d.save_screenshot \
                ("D:\\Rupali Prathamesh Pandit\\CredCart2\\Screenshots\\test_PurchaseProduct_005_Fail.png")
            assert False
        self.log.info("test_PurchaseProduct_005 is Completed")

