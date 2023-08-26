from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class RegisterPage:

    Link_Text_RegisterLink = (By.LINK_TEXT , "Register")
    Id_Name = (By.ID , "name")
    Id_Email = (By.ID , "email")
    XPATH_Password = (By.XPATH , "//input[@id='password']")
    Id_Confirm_Password = (By.ID , "password-confirm")
    XPATH_Register_Button = (By.XPATH , "//button[contains(text(),'Register')]")
    Success_MSG = (By.XPATH , "//h2[text()='CredKart']")

    def __init__(self , d):
        self.d = d

    def Click_On_RegisterLink(self):
        self.d.find_element(*RegisterPage.Link_Text_RegisterLink).click()

    def Enter_Name(self , name):
        self.d.find_element(*RegisterPage.Id_Name).send_keys(name)

    def Enter_Email_Id(self , email):
        self.d.find_element(*RegisterPage.Id_Email).send_keys(email)

    def Enter_Password(self , password):
        self.d.find_element(*RegisterPage.XPATH_Password).send_keys(password)

    def Confirm_Password(self , password):
        self.d.find_element(*RegisterPage.Id_Confirm_Password).send_keys(password)

    def Click_On_Register(self ):
        self.d.find_element(*RegisterPage.XPATH_Register_Button).click()

    def Success_Status(self):
        try:
            self.d.find_element(*RegisterPage.Success_MSG)
            return True
        except NoSuchElementException:
            return False
