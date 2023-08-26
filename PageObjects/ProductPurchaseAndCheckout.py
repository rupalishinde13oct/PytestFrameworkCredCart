from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ProductPurchase:

    XPATH_Apple_MacBookPro = (By.XPATH , "//h3[text()='Apple Macbook Pro']")
    XPATH_Headphones = (By.XPATH , "//h3[text()='Headphones']")
    XPATH_Guitar = (By.XPATH , "//h3[text()='Acoustic Guitar']")
    XPATH_Ipad = (By.XPATH , "//h3[text()='Apple iPad Retina']")
    XPATH_Add_To_Cart = (By.XPATH , "//input[@value='Add to Cart']")
    XPATH_Continue_SHopping = (By.XPATH , "//a[text()='Continue Shopping']")
    XPATH_Proceed_To_Checkout = (By.XPATH , "//a[text()='Proceed to Checkout']")
    XPATH_FirstName = (By.ID , "first_name")
    XPATH_LastName = (By.ID , "last_name")
    XPATH_Phone = (By.ID , "phone")
    XPATH_Address = (By.ID , "address")
    XPATH_ZipCode = (By.ID , "zip")
    XPATH_State = (By.ID , "state")
    XPATH_Owner = (By.ID , "owner")
    XPATH_CVV = (By.ID , "cvv")
    XPATH_CardNumber = (By.ID , "cardNumber")
    XPATH_ExpiryYear = (By.ID , "exp_year")
    XPATH_ExpiryMonth= (By.ID, "exp_month")
    XPATH_Continue_To_Checkout = (By.XPATH , "//button[text()='Continue to checkout']")
    Success_MSG = (By.XPATH , "//p[text()='Your order has been placed successfully.']")


    def __init__(self , d):
        self.d = d

    def Click_On_Apple_MacBookPro(self):
        self.d.find_element(*ProductPurchase.XPATH_Apple_MacBookPro).click()

    def Click_On_HeadPhones(self):
        self.d.find_element(*ProductPurchase.XPATH_Headphones).click()

    def Click_On_Guitar(self):
        self.d.find_element(*ProductPurchase.XPATH_Guitar).click()

    def Click_On_IPad(self):
        self.d.find_element(*ProductPurchase.XPATH_Ipad).click()

    def Click_On_AddToCart(self):
        self.d.find_element(*ProductPurchase.XPATH_Add_To_Cart).click()

    def Click_On_Continue_SHopping(self):
        self.d.find_element(*ProductPurchase.XPATH_Continue_SHopping).click()

    def Click_On_Proceed_To_Checkout(self):
        self.d.find_element(*ProductPurchase.XPATH_Proceed_To_Checkout).click()

    def Enter_FirstName(self , firstname):
        self.d.find_element(*ProductPurchase.XPATH_FirstName).send_keys(firstname)

    def Enter_LastName(self , lastname):
        self.d.find_element(*ProductPurchase.XPATH_LastName).send_keys(lastname)

    def Enter_Phone(self , phone):
        self.d.find_element(*ProductPurchase.XPATH_Phone).send_keys(phone)

    def Enter_Address(self , address):
        self.d.find_element(*ProductPurchase.XPATH_Address).send_keys(address)

    def Enter_ZipCode(self , zip):
        self.d.find_element(*ProductPurchase.XPATH_ZipCode).send_keys(zip)

    def Select_State(self , stateindex):
        Select(self.d.find_element(*ProductPurchase.XPATH_State)).select_by_index(stateindex)

    def Enter_OwnerName(self , owner):
        self.d.find_element(*ProductPurchase.XPATH_Owner).send_keys(owner)

    def Enter_CVV(self , cvv):
        self.d.find_element(*ProductPurchase.XPATH_CVV).send_keys(cvv)

    def Enter_CardNumber(self , cardNumber):
        self.d.find_element(*ProductPurchase.XPATH_CardNumber).send_keys(cardNumber)

    def Enter_ExpiryYear(self , exp_Yearindex):
        Select(self.d.find_element(*ProductPurchase.XPATH_ExpiryYear)).select_by_index(exp_Yearindex)

    def Enter_ExpiryMonth(self , exp_Yearindex):
        Select(self.d.find_element(*ProductPurchase.XPATH_ExpiryMonth)).select_by_index(exp_Yearindex)

    def Click_On_Continue_To_Checkout(self):
        self.d.find_element(*ProductPurchase.XPATH_Continue_To_Checkout).click()

    def Success_Status(self):
        msg = self.d.find_element(*ProductPurchase.Success_MSG).text
        if msg == 'Your order has been placed successfully.':
            return True
        else:
            return False
