import time

from Utility.readConfig import ReadConfig
from Utility.Logger import Logger
from PageObjects.LoginPage import LoginPage

class TestLoginWithParams:

    log = Logger.get_Logger()
    url = ReadConfig.getURL()

    def test_Login_With_Parameters_003(self , setup , readLoginData):
        self.log.info("test_Login_With_Parameters_003 is Started")
        self.d = setup
        self.log.info("Launching browser..!!")
        self.d.get(self.url)
        self.log.info("Go to -->"+self.url)
        # time.sleep(5)
        lp = LoginPage(self.d)
        lp.Click_On_Login_Link()
        # time.sleep(5)
        self.log.info("Clicking on Login link")
        lp.Enter_Email(readLoginData[0])
        self.log.info("Entring Email-->" + readLoginData[0])
        lp.Enter_Password(readLoginData[1])
        self.log.info("Entring password-->" + readLoginData[1])
        lp.Click_On_Login_Button()
        self.log.info("Clicking on Login Button")

        if lp.SUccess_Status() == True:
            if readLoginData[2] == "Pass":
                lp.Click_On_Menu_Button()
                # time.sleep(5)
                lp.Click_On_Logout_Button()
                self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\CredCart2\\Screenshots\\"+readLoginData[0]+"__"+readLoginData[1]+"test_Login_With_Parameters_003_Pass.png")
                self.log.info("test_Login_With_Parameters_003 is Passed")
                assert True
            else:
                self.d.save_screenshot(
                    "D:\\Rupali Prathamesh Pandit\\CredCart2\\Screenshots\\"+readLoginData[0]+"__"+readLoginData[1]+"test_Login_With_Parameters_003_Fail.png")
                self.log.info("test_Login_With_Parameters_003 is Failed")
                assert False
        else:
            if readLoginData[2] == "Fail":
                self.d.save_screenshot(
                    "D:\\Rupali Prathamesh Pandit\\CredCart2\\Screenshots\\"+readLoginData[0]+"__"+readLoginData[1]+"test_Login_With_Parameters_003_Pass.png")
                self.log.info("test_Login_With_Parameters_003 is Passed")
                assert True
            else:
                self.d.save_screenshot(
                    "D:\\Rupali Prathamesh Pandit\\CredCart2\\Screenshots\\"+readLoginData[0]+"__"+readLoginData[1]+"test_Login_With_Parameters_003_Fail.png")
                self.log.info("test_Login_With_Parameters_003 is Failed")
                assert False
        self.d.close()
        self.log.info("test_Login_With_Parameters_003 is Completed")

