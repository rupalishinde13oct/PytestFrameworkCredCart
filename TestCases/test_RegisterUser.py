import time
from PageObjects.RegisterPage import RegisterPage
from selenium import webdriver
from Utility.Logger import Logger
from Utility.readConfig import ReadConfig

class TestRegister:

    log = Logger.get_Logger()
    url = ReadConfig.getURL()

    def test_RegisterUser_001(self , setup):
        self.log.info("test_RegisterUser_001 is Started")
        self.d = setup
        self.log.info("Launching browser---!!")
        self.d.get(self.url)
        self.log.info("Go to --> " + self.url)

        rp = RegisterPage(self.d)
        rp.Click_On_RegisterLink()
        self.log.info("CLicked on registration link")
        rp.Enter_Name("Rupali")
        self.log.info("Entering Username..")
        rp.Enter_Email_Id("rupalirupali132111@gmail.com")
        self.log.info("Entering Email..")
        rp.Enter_Password("123456")
        self.log.info("Entering Password..")
        rp.Confirm_Password("123456")
        self.log.info("Confirming Password..")
        rp.Click_On_Register()
        self.log.info("Clicking on Register Button")

        if rp.Success_Status() == True:
            self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\CredCart2\\Screenshots\\test_RegisterUser_001_Pass.png")
            self.log.info("test_RegisterUser_001 is Passed")
            assert True
        else:
            self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\CredCart2\\Screenshots\\test_RegisterUser_001_Fail.png")
            self.log.info("test_RegisterUser_001 is Failed")
            assert False
        self.log.info("test_RegisterUser_001 is Completed")
        time.sleep(4)