from Utility.readConfig import ReadConfig
from Utility.Logger import Logger
from PageObjects.LoginPage import LoginPage

class TestLogin:

    log = Logger.get_Logger()
    url = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_Login_002(self , setup):
        self.log.info("test_Login_002 is Started")
        self.d = setup
        self.log.info("Launching browser..!!")
        self.d.get(self.url)
        self.log.info("Go to -->"+self.url)

        lp = LoginPage(self.d)
        lp.Click_On_Login_Link()
        self.log.info("Clicking on Login link")
        lp.Enter_Email(self.username)
        self.log.info("Entring Email-->" + self.username)
        lp.Enter_Password(self.password)
        self.log.info("Entring password-->" + self.password)
        lp.Click_On_Login_Button()
        self.log.info("Clicking on Login Button")

        if lp.SUccess_Status() == True:
            lp.Click_On_Menu_Button()
            self.log.info("Clicking on Menu Button")
            lp.Click_On_Logout_Button()
            self.log.info("Clicking on Logout Button")
            self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\CredCart2\\Screenshots\\test_Login_002_Pass.png")
            self.log.info("test_Login_002 is Passed")
            assert True
        else:
            self.d.save_screenshot(
                "D:\\Rupali Prathamesh Pandit\\CredCart2\\Screenshots\\test_Login_002_Fail.png")
            self.log.info("test_Login_002 is Failed")
            assert False
        self.log.info("test_Login_002 is Completed")