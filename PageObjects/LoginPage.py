from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:

    XPATH_LoginLink = (By.XPATH , "//a[text()='Login']")
    Id_Email = (By.ID , "email")
    Id_Password = (By.ID , "password")
    XPATH_Login_Button = (By.XPATH , "//button[contains(text(),'Login')]")
    XPATH_MenuButton = (By.XPATH , "//a[@href='#' and @class='dropdown-toggle']")
    XPATH_Logout_Button = (By.XPATH , "//a[contains(text(),'Logout')]")
    Success_MSG =  (By.XPATH , "//h2[normalize-space()='CredKart']")


    def __init__(self , d):
        self.d = d

    def Click_On_Login_Link(self):
        self.d.find_element(*LoginPage.XPATH_LoginLink).click()

    def Enter_Email(self , email):
        self.d.find_element(*LoginPage.Id_Email).send_keys(email)

    def Enter_Password(self , password):
        self.d.find_element(*LoginPage.Id_Password).send_keys(password)

    def Click_On_Login_Button(self):
        self.d.find_element(*LoginPage.XPATH_Login_Button).click()

    def Click_On_Menu_Button(self):
        self.d.find_element(*LoginPage.XPATH_MenuButton).click()

    def Click_On_Logout_Button(self):
        self.d.find_element(*LoginPage.XPATH_Logout_Button).click()

    def SUccess_Status(self):
        try:
            self.d.find_element(*LoginPage.Success_MSG)
            return True
        except NoSuchElementException:
            return False